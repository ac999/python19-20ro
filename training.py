import re, hashlib, os, sys, datetime, sqlite3, zipfile
from urllib import request

def hash(_string, hashtype):
    hashtype.update(_string)
    return hashtype.hexdigest()
def hashFile(filep, hashtype=hashlib.md5()):
    try:
        with open(filep, "rb") as f:
            for chunk in iter(lambda: f.read(2048), b""):
                hashtype.update(chunk)
        return hashtype.hexdigest()
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
        print("problema2: {}".format(e))
        return False

def problema3(path):
    try:
        hash_list=[]
        for root, dirs, files in os.walk(path):
            for file in files:
                hash_list.append(hashFile(os.path.join(root,file)))
        return sorted(hash_list)
    except Exception as e:
        print("problema3: {}".format(e))
        return []

def problema4():
    try:
        _dir = sys.argv[1]
        return sorted(list({os.path.getsize(file) for file in os.listdir(_dir)
        if os.path.isfile(file)}))
    except Exception as e:
        print("problema4: {}".format(e))
        return []

def instrepl(matchobj):
    instr={
    "egal": '=',
    "plus": '+=',
    "minus": '-=',
    "impartit": '//=',
    "inmultit": '*='
    }
    return matchobj.group(1)+instr.get(matchobj.group(2))+matchobj.group(3)

def problema5(cod):
    try:
        loc = {}
        new_code=""
        for line in cod.splitlines():
            new_code+=re.sub(r'(x)\s*(\w+)\s*(\d+)', instrepl, line)+'\n'
        exec(new_code, globals(), loc)
        return loc.get('x')
    except Exception as e:
        print("prolema5: {}".format(e))
        return -1

def str_to_date(date_string):
    expr = r'(\d\d)\/(\d\d)\/(\d\d\d\d)\_(\d\d)\.(\d\d)\.(\d\d)'
    m = re.match(expr, date_string)
    return datetime.datetime(
    int(m.group(3))      # year
    , int(m.group(1))    # month
    , int(m.group(2))    # day
    , int(m.group(4))    # hour
    , int(m.group(5))    # minute
    , int(m.group(6))    # second
    )

def get_dates(_list):
    return list(sorted(map(str_to_date, _list), reverse=True))

def problema7():
    try:
        dates = get_dates(sys.argv[1:])
        min_date = max_date = dates[0]
        for date in dates:
            if date < min_date:
                min_date = date
            if date > max_date:
                max_date = date

        return [list(sorted(map(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"), dates), reverse = True))
        , int((max_date-min_date).total_seconds())]
    except Exception as e:
        print("problema7: {}".format(e))
        return []


def search_for_zip(path):
    for root, dir, file in os.walk(path):
        for name in file:
            if zipfile.is_zipfile(os.path.join(root,name)):
                return os.path.join(root,name)


def problema8(path, low, high, file_name="sample.sqlite"):
    try:
        low = int(low)
        high = int(high)
        f_path = search_for_zip(path)
        if not f_path:
            raise Exception("Archive not found.")
        z = zipfile.ZipFile(f_path)
        found = False
        for _file in z.namelist():
            if _file.rfind(file_name)!=-1:
                db_file = _file
                found = True
                break

        if not found:
            raise Exception("No db file found.")

        z.extract(db_file)

        data = list()

        with sqlite3.connect(db_file) as conn:
            c = conn.cursor()

            query = '''SELECT AlbumId, Name, GenreId
            FROM tracks
            WHERE Milliseconds BETWEEN {0} and {1}'''.format(low, high)

            c.execute(query)

            while(True):
                result = c.fetchone()
                if not result:
                    break
                data.append(result)


            genre_dict=dict()
            album_dict=dict()

            new_data = list()

            for song in data:
                album_id = song[0]
                genre_id = song[2]

                if album_id not in album_dict.keys():
                    query_albums = '''SELECT title FROM albums
                    WHERE AlbumId == {}'''.format(album_id)
                    c.execute(query_albums)
                    album_dict[album_id] = c.fetchone()[0]
                album = album_dict[album_id]

                if genre_id not in genre_dict.keys():
                    query_genres = '''SELECT name FROM genres
                    WHERE GenreId == {}'''.format(genre_id)
                    c.execute(query_genres)
                    genre_dict[genre_id] = c.fetchone()[0]
                genre = genre_dict[genre_id]

                new_data.append((album, song[1], genre))

        return list(sorted(new_data))

    except Exception as e:
        print("Error->", e)

def getIp(line):
    expr = r'(\d+\.\d+\.\d+\.\d)'
    m = re.split(expr, line)
    return m[1]

def file_get_ip(file):
    _dict = dict()
    with open(file, "r") as f:
        chunk = f.read(2048)
        while(chunk):
            for line in chunk.splitlines():
                _dict[getIp(line)] = _dict.get(getIp(line),0)+1
            chunk = f.read(2048)
    return _dict

def get_most_7_ips(_dict):
    return [k for k, v in sorted(
    _dict.items(), key = lambda ap: ap[1], reverse = True) ] [:7]

def problema9(path, file_name="access.log"):
    try:
        isDirectory = False
        if os.path.isdir(path):
            isDirectory = True
        if isDirectory:
            _dict = dict()
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file==file_name:
                        ips = file_get_ip(os.path.join(root, file))
                        i = 0
                        for k, v in sorted(ips.items()
                        , key = lambda ap:ap[1], reverse = True ):
                            i += 1
                            if i >= 7: break
                            _dict[k]=_dict.get(k,0) + v
            return get_most_7_ips(_dict)


        else:
            return get_most_7_ips(file_get_ip(path))
    except Exception as e:
        print("problema9: {}".format(e))
        return "error."
