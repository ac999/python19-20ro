import socket, re

HOST = "127.0.0.1"
PORT = 7778

def check_data(data):
    ex = r"(\d\|)*\d\."
    if re.search(ex, data):
        return True
    return False

def do_sum(data):
    try:
        to_sum = map(int, data.split(".")[0].split("|"))
        return str(sum(to_sum))
    except Exception as e:
        print(__name__, " -> Error -> ", e)
        return 0

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # next line to avoid [Errno 98] Address already in use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    (connection, address) = s.accept()
    print("Connected address:", address)
    while True:
        data = connection.recv(100).decode("UTF-8")
        if not data: break
        print("Received: ",data)
        if check_data(data):
            response = do_sum(data).encode("UTF-8")
            connection.send( response )
        else:
            response = "Invalid data.".encode("UTF-8")
            connection.send( response )
        print("Sent: ", response )
        # if "." in data: break
    connection.close()
    print("Server closed")

except Exception as e:
    print("Error -> ", e)
    s.close()
