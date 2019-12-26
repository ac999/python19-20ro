import re

def word_extractor(text):
    return re.findall('\w+', text)

def apply_re_len(r, text, length):
    try:
        return [word for word in re.findall(r, text) if len(word)==length]
    except:
        return "Invalid regex." 
