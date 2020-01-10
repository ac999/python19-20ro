import zipfile, hashlib, datetime, sqlite3
from os.path import splitext, isdir, isfile, abspath, dirname
from os import listdir

def hasExtension(f_path, extension):
    return splitext(f_path)[1]==".{}".format(extension)

def ex1(a_path, ext, fa_path = None):
    if fa_path:
        archive_path = fa_path
    else:
        archive_path = "the.zip"

    if not isdir(a_path):
        raise Exception("ex1: a_path must be a directory.")

    z = zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED)

    [ z.write( _file ) for _file in listdir(a_path) if hasExtension(_file, ext)  ]

    z.close()

def ex2(a_path):
    try:
        z = zipfile.ZipFile(a_path)
    except Exception as e:
        return list()
    return [_file.filename for _file in z.infolist()]

def ex3(a_path, to_hextract):
    try:
        z = zipfile.ZipFile(a_path)
    except Exception as e:
        return None
    try:
        f = z.open(to_hextract)
    except Exception as e:
        return None

    buffer_size = 2096

    try:
        c = hashlib.md5()
        while(True):
            data = f.read(buffer_size)
            c.update(data)
            if not data:
                break
        return c.hexdigest()

    except Exception as e:
        raise ("ex3: hashing error ->", e)

def ex4(a_path, db_path):
    if isfile(db_path):
        create_table = True
    else:
        create_table = False

    if not isdir(a_path):
        raise Exception("ex4: a_path must be a directory.")

    run_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(db_path)

    c = conn.cursor()

    if create_table:
        c.execute('''CREATE TABLE files
        (file_name text, parrent_folder text, date text)''')

    c.execute('''INSERT INTO files)
    # [fileObject.writelines("{} , {} , {}\n"
    # .format(
    # _file
    # , dirname( abspath(_file) )
    # , run_time
    # )) for _file in listdir(a_path)]

def ex5(db_path):
    conn = sqlite3.connect(db_path)
    # c.execute('')
    list( map( lambda x: str.strip(x), fileObject.readlines() ) )
