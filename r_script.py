import script

def try_ex1():
    a_path = "."
    ext = "py"
    archive_path = "test.zip"
    try:
        script.ex1(a_path, ext, archive_path)
    except Exception as e:
        print("Error - >", e)

try_ex1()
