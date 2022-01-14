import subprocess

obj = subprocess.Popen("dir D:",shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       )
res = obj.stdout.read()
print(res.decode("gbk"))
# err_res = obj.stdout.read()
# print(err_res.decode("utf-8"))