from urllib import request
import sys, re

re_rule = r"<img.*src=\"(http[s].+)(?<!\")\" .*>"

def save_image(image_url):
    image_name = image_url.split("/")[-1]
    f = open(image_name, 'wb')
    f.write(request.urlopen(image_url).read())
    f.close()

if len(sys.argv) != 2:
    print( "use: {} url".format(__file__) )
    exit()

url = sys.argv[1]
try:
    response = request.urlopen(url).read()
    content = response.decode("utf-8")
except Exception as e:
    print("Error -> ", e)
    exit()

image_url = re.findall(re_rule, content)

try:
    [save_image(img_url) for img_url in image_url]
except Exception as e:
    print("save_image error -> ", e)
