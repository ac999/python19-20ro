import re, functools

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
