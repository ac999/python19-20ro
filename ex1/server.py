import socket, datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",7777))
s.listen(5)
(connection, address) = s.accept()
connection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print( "{} : {}".format( connection_time, s.getpeername() ) )
