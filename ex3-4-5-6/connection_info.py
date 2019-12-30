from urllib import request
import hashlib
import sys

if len(sys.argv) != 2:
    print( "use: {} url".format(__file__) )
    exit()

_url = sys.argv[1]

def write_data(url, status, size, type, date, fragment):
    try:
        with open (url.split("://")[1].split(".")[0]+".txt", "w+") as fileObject:
            fileObject.write("URL: {}\n".format(url) )
            if status:
                fileObject.write("Status: {}\n".format(status) )
            if size:
                fileObject.write("Size: {}\n".format(size) )
            if type:
                fileObject.write("Type: {}\n".format(type) )
            if date:
                fileObject.write("Date: {}\n".format(date) )
            if fragment:
                fileObject.write("MD5: {}\n".format(fragment) )
    except Exception as e:
        print(e)


# https://developer.mozilla.org/en-US/docs/Web/HTTP

try:
    response = request.urlopen(_url)

    _status = response.getcode()
    # The Content-Length entity header indicates the size of the entity-body,
    # in bytes, sent to the recipient.
    _size = response.getheader("Content-Length")
    # The Content-Type entity header is used to indicate the media type of the
    # resource.
    _type = response.getheader("Content-Type")
    # The Date general HTTP header contains the date and time at which the
    # message was originated.
    _date = response.getheader("Date")
    _frag_md5 = None
    if int(_size) <= 1000:
        _frag_md5 = hashlib.md5( response.read() ).hexdigest()

except Exception as e:
    print("Error -> ", e)
    exit()

write_data(_url, _status, _size, _type, _date, _frag_md5)
