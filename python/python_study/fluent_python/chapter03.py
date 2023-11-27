a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a)
print(b)
print(c)
print(d)
print(e)
print(a == b == c == d == e)

# 3.1 字典推导的应用
DIAL_CODES = [(86, 'CHINA'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakiston')]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
print({country.upper(): code for country, code in country_code.items() if code < 60})
