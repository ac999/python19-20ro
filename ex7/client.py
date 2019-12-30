import socket, sys, time

HOST = "127.0.0.1"
PORT = 7778

if len(sys.argv) != 2:
    print ("use: {} number sequence like (1|2|3|4.)".format(__file__) )
    exit()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(sys.argv[1].encode("UTF-8"))
    response = s.recv(100).decode("UTF-8")
    print("Received: ", response )

except Exception as e:
    print("Error -> ", e)
    exit()
finally:
    print("Closing socket.")
    s.close()
WAIT = 1
