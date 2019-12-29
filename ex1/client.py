import socket, sys

if len(sys.argv) != 3:
    print("use: {} addr port".format(__file__))
    exit()
# it will not check if the address is correct
addr = sys.argv[1]
try:
    port = int(sys.argv[2])
except Exception as e:
    print(e)
    exit()

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
try:
    s.connect((addr,port))
    s.close()
except Exception as e:
    print(e)
    exit()
