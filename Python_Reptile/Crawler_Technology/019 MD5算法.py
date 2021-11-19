import hashlib

str01 = "pythsddsssssdfsdsdfsdfsdfsdfsdon123456"

md5 = hashlib.md5()

md5.update(str01.encode())

result = md5.hexdigest()
print(result)

