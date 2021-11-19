import re

r = re.match("[A-Z][a-z]*", "MnnM")
print(r.group())

r = re.match("[A-Z]*[a-z]*[A-Z]*", "AASDasdasASDAS")
print(r.group())


