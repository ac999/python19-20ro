import script

_text = '''<h2>Als ter verdeeld mee gesticht interest verleden</h2>

<p>Onder staat later ik komst en banka te. Tonnen en tengka spuwen is
en ad. Toekomst aan heb verbindt zandlaag hen landbouw men. Al werkten
ontdekt ze te na valorem. Eischen was dit planter per aan zooveel. Ton
producten vernieuwd provincie die. Dier daad dure af te. Dieren dus den
omtrek der als eerste. Binnenste voorkomen is nabijheid ingenieur in
zuidgrens.</p>'''

# Exercise 1:
print("Exercise 1:")
print(script.word_extractor(_text))

# Exercise 2:
r = '\w+'
print("Exercise 2:")
print(script.apply_re_len(r,_text,6))

# Exercise 3:
