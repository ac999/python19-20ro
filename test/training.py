import re, hashlib, os
from urllib import request

def hash(_string, hashtype):
    hashtype.update(_string)
    return hashtype.digest()
def hashFile(filep, hashtype=hashlib.md5()):
    try:
        with open(filep, "r") as f:
            chunk = f.read(2048).encode("utf-8")
            while chunk:
                hashtype.update(chunk)
                chunk = f.read(2048)
        return hashtype.digest()
    except Exception as e:
        raise Exception("hashFile: {}".format(e))
def problema1(s):
    return sorted(re.split(r'\W+', s))
def problema2(s, url):
    try:
        response = request.urlopen(url).read()
        content = response.decode("utf-8")
        return not(content.find(s)==-1)
    except Exception as e:
        return "problema2: {}".format(e)
def problema3(path):
    try:
        hash_list=[]
        for root, dirs, files in os.walk(path):
            for file in files:
                hash_list.append(hashFile(os.path.join(root,file)))
        return hash_list
    except Exception as e:
        return "problema3: {}".format(e)
