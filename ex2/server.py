import datetime as dt
import hashlib as hl
import socket, sys

def write_text(text, WandF):
    if WandF[0] and WandF[1]:
        try:
            fo = open(WandF[1], "a")
            fo.write(text)
            fo.close()
        except Exception as e:
            print(e)
            exit()
    else:
        print(text)

def helper(args):
    _help = "use {} -o file ( where file is the output file)".format(__file__)

    write_to_file = False
    _file = None

    if len(args) > 3:
        print ( _help )
        exit()

    if len(args) == 1:
        pass
    else:
        if args[1] == "-o":
            write_to_file = True
            _file = args[2]

        else:
            print( _help )
            exit()

    return (write_to_file, _file)

# from lab 11:
def hash_text(_text, _hash):
    try:
        _hash.update(_text)
        return _hash.hexdigest()
    except Exception as e:
        print(e)
        return ""

def create_result(data):
    _date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _len = len(data)
    _md5 = hash_text(data, hl.md5())
    _sha256 = hash_text(data, hl.sha256())
    return ( _date, _len, _md5, _sha256 )

def create_output(result, addr):
    return '''
    Date: {}
    Client address: {}
    Client port:    {}
    Length of data: {}
    MD5 of data:    {}
    SHA256 of data: {}
    ---------------------------'''.format(
    result[0], addr[0], addr[1], result[1], result[2], result[3]
    )

cl_buffer_size = 4096
HOST = "127.0.0.1"
PORT = 6666

_WandF = helper(sys.argv)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # next line to avoid [Errno 98] Address already in use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        while True:
            data, addr = s.recvfrom(cl_buffer_size)
            write_text(
            create_output(
            create_result(data), addr
            ), _WandF
            )
except Exception as e:
    print(e)
    exit()
