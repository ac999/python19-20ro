from urllib import request
from os import path

def filter_rule(file_name):
    if path.splitext(file_name)[1] == ".txt":
        return True
    return False

try:
    response = request.urlopen("http://127.0.0.1:5555").read()
    text = response.decode("utf-8")
    # get ordered list:
    li = text.split("<ul>")[1].split("</ul>")[0].splitlines()
    # get item names and put them into list
    it_l = [it.split("href=\"")[1].split("\">")[0] for it in li[1:]]
    print ([item for item in filter(filter_rule,it_l)])
except Exception as e:
    print("Error -> ",e )
    exit()
