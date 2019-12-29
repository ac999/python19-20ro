import socket, datetime

HOST = "127.0.0.1"
PORT = 7777
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # next line to avoid [Errno 98] Address already in use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            connection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Time: {}.\nClient address: {}.\nClient port: {}"
            .format( connection_time, addr[0], addr[1] ) )
            conn.close()
except Exception as error:
    print(error)
    exit()
