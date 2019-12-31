import socket, json, sys

HOST = "127.0.0.1"
PORT = 7779

def open_dict(json_path):
    try:
        data = open(json_path,"rt").read()
        return data
    except Exception as e:
        print( "{}: Error -> {}".format( __name__, e ) )
        return json.dumps(dict())

def handshake(sock, message):
    length = len(message)
    try:
        sock.send( message.encode( "utf-8" ) )
        received = sock.recv( 100 ).decode( "utf-8" )
        print("{} received: {}. Should've received: {}"
        .format( __file__, received, length ) )
        if str(length) == received:
            return True
        else:
            return False
    except Exception as e:
        print( "{}: Error -> {}".format( __name__, e ) )
        return False

if len(sys.argv) != 3:
    print ("use: {} dict.json key".format(__file__) )
    exit()

_dict = open_dict( sys.argv[1] )
_key = sys.argv[2]

received = "nothing."

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    if handshake(s, _dict):
        if handshake(s, _key):
            received = s.recv(100).decode("utf-8")
    print("Received: ", received )

except Exception as e:
    print("Error -> ", e)
    exit()
finally:
    print("Closing socket.")
    s.close()
