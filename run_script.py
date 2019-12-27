import script as scr

_text = '''<h2>Als ter verdeeld mee gesticht interest verleden</h2>

<p>Onder staat later ik komst en banka te. Tonnen en tengka spuwen is
en ad. Toekomst aan heb verbindt zandlaag hen landbouw men. Al werkten
ontdekt ze te na valorem. Eischen was dit planter per aan zooveel. Ton
producten vernieuwd provincie die. Dier daad dure af te. Dieren dus den
omtrek der als eerste. Binnenste voorkomen is nabijheid ingenieur in
zuidgrens.</p>'''

# Exercise 1:
print("Exercise 1:")
print(scr.word_extractor(_text))

# Exercise 2:
r1 = r'\w+'
print("Exercise 2:")
print(scr.apply_re_len(r1,_text,6))

# Exercise 3:
r2 = r'[a-t]+'
print("Exercise 3:")
print(scr.apply_listre(_text,[r1,r2]))

# Exercise 4:
_attrs = {
"id": "bk104",
"version": "1.0"
}
print("Exercise 4:")
print(scr.xml_parse("./books.xml",**_attrs))

# Exercise 6:
print("Exercise 6:")
print(scr.censure(_text))

# Exercise 7:
print("Exercise 7:")
print(scr.cnp("1860331405413"))
print(scr.cnp("1631006221137"))

# Exercise 8:
print("Exercise 8:")
print(scr.the_directory_scrolls(r2,"."))
