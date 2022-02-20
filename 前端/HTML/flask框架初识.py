from flask import Flask,request

app = Flask(__name__)


# 当前url既可以支持get请求也可以支持post请求  如果不写默认只能支持get请求
@app.route("/index/", methods=["GET", "POST"])
def index():
    print(request.form)
    print(request.files)
    file_obj=request.files.get("myfile")
    print(file_obj.name)
    file_obj.save(file_obj.name+"01.jpg")
    return "OK"


if __name__ == '__main__':
    app.run()
