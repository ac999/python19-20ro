import sys, socket

if len(sys.argv) != 4:
    print("use: {} addr port msg(string)".format(__file__))
    exit()
# it will not check if the address is correct
addr = sys.argv[1]
message = sys.argv[3].encode("UTF-8")
try:
    port = int(sys.argv[2])
except Exception as e:
    print(e)
    exit()

s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
try:
    s.sendto( message , (addr, port) )
    s.close()
except Exception as e:
    print(e)
    exit()
