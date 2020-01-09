import script

def try_ex1():
    a_path = "."
    ext = "py"
    archive_path = "test.zip"
    try:
        script.ex1(a_path, ext, archive_path)
    except Exception as e:
        print("Error - >", e)

def try_ex2():
    a_path = "test.zip"
    print("ex2({}): {}".format(a_path, script.ex2(a_path) ) )

def try_ex3():
    a_path = "test.zip"
    to_hextract = "script.py"
    print("ex3({}, {}): {}".format(a_path, to_hextract
    , script.ex3(a_path, to_hextract)) )

try_ex1()
try_ex2()
try_ex3()
