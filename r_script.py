import script

def try_ex1():
    a_path = "."
    ext = "py"
    archive_path = "test.zip"
    try:
        script.ex1(a_path, ext, archive_path)
    except Exception as e:
        print("ex 1. Error ->", e)

def try_ex2():
    a_path = "test.zip"
    print("ex2({}): {}".format(a_path, script.ex2(a_path) ) )

def try_ex3():
    a_path = "test.zip"
    to_hextract = "script.py"
    try:
        print("ex3({}, {}): {}".format(a_path, to_hextract
        , script.ex3(a_path, to_hextract)) )
    except Exception as e:
        print("ex 3. Error ->", e)

def try_ex4():
    a_path = "."
    db_path = "db.sqlite"
    try:
        script.ex4(a_path, db_path)
    except Exception as e:
        print("ex 4. Error ->", e)

def try_ex5():
    db_path = "db.sqlite"
    try:
        for element in script.ex5(db_path):
            print("{}".format(element) )
    except Exception as e:
        print("ex 5. Error ->", e)

try_ex1()
try_ex2()
try_ex3()
try_ex4()
try_ex5()
