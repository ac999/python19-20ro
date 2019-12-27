# Lab 12
https://sites.google.com/site/fiipythonprogramming/laboratories/lab-12

# Exercise 1
a. Implement using the socket module (TCP), a server that writes when a client connects to it the following data: the connection time in human-readable format, the address, and the port of the client.

b. Implement a client for the deployed server at 1a: a script that receives from the command line a string addr and an integer port and connects through TCP to the addr address at the port port.

# Exercise 2
a. Implement using the socket module (UDP), a server that when is receiving a UDP packet (datagram) writes in a text file the following information: time and date, address, port, length, md5 hash of the content in hex format, sha256.

b. Implement a client for the deployed server at 2a: a script that receives from the command line an addr string, a port integer, and a string msg, and sends a UDP packet to the addr address, the port port, and the msg content.

# Exercise 3
Start a server to expose the files and directories in the current directory. Access that server from a browser, and then using a python HTTP client (urllib.request)

# Exercise 4
Once the server from 3 is started, extract the .txt file names and write to the console.

# Exercise 5
Write a script that receives a URL from the command line (as an argument) and downloads all images (img src) to the current directory.

# Exercise 6
Write a script that receives a URL from the command line (as argument) and writes the following information into a file: response status, response size, response type (if known), md5 hash for each fragment of maximum 1000 bytes of response and server response time.

# Exercise 7
Write 2 scripts, server.py and client.py. Using socket module, both the server and the client will bind/connect to IP 127.0.0.1 and port 1234. The client will send to the server a list of numbers. Each number is followed by "|" character. After the the client sent all the numbers it will send a final character ".". The server will receive all the numbers and will send back to the client the sum of the numbers. The client will display this sum.

# Exercise 8
Write 2 scripts, server.py and client.py. Using socket and json modules, the client will read from a file a dictionary in JSON format and it will send the dictionary to the server alongisde a string representing a key. The server will send back to the client the value of the key from the given dictionary. If the key does not exist, the client will display an error message.
