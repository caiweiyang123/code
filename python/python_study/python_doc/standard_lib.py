import os
import random
import statistics
import sys
from pprint import pprint

print(os.getcwd())
# os.system("dir")
print(sys.argv)
a= random.choice(['apple', 'pear', 'banana'])
print(a)
b = random.sample(range(100), 5)
print(b)
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
from datetime import date
now = date.today()
str_now = str(now)
print(now,type(now))
print(str_now,type(str_now))
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))