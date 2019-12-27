import re, functools, os

def word_extractor(text):
    return re.findall('\w+', text)

def apply_re_len(r, text, length):
    try:
        return [word for word in re.findall(r, text) if len(word)==length]
    except:
        return "Invalid regex."

def apply_listre(text, listre):
    return set.intersection(*[set(re.findall(regex,text)) for regex in listre])

def xml_parse(xmlDocumentPath,**attrs):
    buffer_size = 1024
    try:
        file = open(xmlDocumentPath,"r")
    except:
        return "Cannot open {}.".format(xmlDocumentPath)
    _set = set()
    _keys = attrs.keys()
    while True:
        _buffer = file.read(buffer_size)

        _set=_set.union(*[
        set(re.findall(
        "{0}\s*=\s*\"{1}\"".format(key,attrs[key]),_buffer
        ) )
        for key in _keys] )

        if not _buffer:
            break
    return _set

def cens_repl(m):
    censorship = list(m.group(1))
    for i in range(len(censorship)):
        if i%2 != 0:
            censorship[i]="*"
    return "*"+"".join(censorship)

def censure(text):
    return re.sub(r"\b[aeiouAEIOU](\w+)\b",cens_repl,text)
    # (Note that \b is used to represent word boundaries, and means “backspace”
    # only inside character classes.)

def cnp(_cnp):
    _control="279146358279"
    _sum=0
    result = re.search(r"([12])(\d{11})(\d)",_cnp)
    if not result:
        return "{} is not a valid CNP.".format(_cnp)
    _sum+=int(result.group(1))*int(_control[0])
    _sum+=sum(
    [int(result.group(2)[i])*int(_control[i+1]) for i in range(len(_control)-1)]
    )
    if result.group(3)==str(_sum%11)[0]:
        return "{} is a valid CNP.".format(_cnp)
    else:
        return "{} is not a valid CNP (control number error).".format(_cnp)

def condition(regex, file):
    buffer_size = 2096
    ok = 0
    result = re.search(regex,file)
    if not result:
        return None
    if result == os.path.splitext(file)[0]:
        ok = 1
    fo = open(file,"r")
    while True:
        try:
            _buffer = fo.read(buffer_size)
            if re.search(regex,_buffer):
                if ok == 1:
                    ok = 3
                else:
                    ok = 2
                break
        except:
            _buffer = None

        if not _buffer:
            break
    if ok==0:
        return None
    if ok==1:
        return ("name_match", file)
    if ok==2:
        return ("content_match", file)
    if ok==3:
        return ("both", ">>"+file)

def the_directory_scrolls(regex, _dir = "."
, _dict = {"name_match": list(), "content_match": list(), "both": list() }
):

    if os.path.isfile(_dir):
        _result = condition(regex,_dir)
        if _result:
            _dict[_result[0]].append(_result[1])

    if os.path.isdir(_dir):

        [ the_directory_scrolls(regex,os.path.join(_dir,node) )
        for node in os.listdir(_dir) ]
    return _dict
