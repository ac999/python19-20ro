import socket, json

def getValue(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None

HOST = "127.0.0.1"
PORT = 7779

response = "Error."

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # next line to avoid [Errno 98] Address already in use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    (connection, address) = s.accept()
    print("Connected address:", address)
    while True:
        _dictionary = connection.recv( 100 ).decode( "utf-8" )
        if not _dictionary: break
        connection.send( str( len( _dictionary ) ).encode( "utf-8" ) )
        _dictionary = json.loads(_dictionary)
        print(_dictionary)
        _key = connection.recv( 100 ).decode( "utf-8" )
        if not _key: break
        connection.send( str( len( _key ) ).encode( "utf-8" ) )
        print(_key)
        response = getValue(_dictionary, _key).encode( "utf-8" )
        connection.send( response )
        print("Sent: ", response )
    connection.close()
    print("Server closed")

except Exception as e:
    print("Error -> ", e)
    s.close()
