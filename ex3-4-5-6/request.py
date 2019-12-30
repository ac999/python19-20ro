from urllib import request

print(request.urlopen("http://127.0.0.1:5555").read().decode("UTF-8"))
