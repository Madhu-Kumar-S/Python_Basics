# Python | Check for URL in a String
import re

ex = 'I am a blogger at https://geeksforgeeks.org'

symbols = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

url = re.findall(symbols, ex)

for i in url:
    print(i)
    break