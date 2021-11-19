import requests

image_url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&hs=0&pn=17&spn=0&di=228580&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=3044261220%2C3500389775&os=4030793474%2C2538774645&simid=4284591613%2C553437318&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=%E5%9B%BE%E7%89%87&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fimg.pconline.com.cn%2Fimages%2Fupload%2Fupc%2Ftx%2Fphotoblog%2F1501%2F04%2Fc4%2F1470032_1420372871085_mthumb.jpg%26refer%3Dhttp%3A%2F%2Fimg.pconline.com.cn%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1629713821%26t%3D3a766f9d56c8937bd9613c6d9e62b1bd&fromurl=ippr_z2C%24qAzdH3FAzdH3F1r_z%26e3Brv5gstgj_z%26e3Bv54_z%26e3BvgAzdH3Fri5p5AzdH3Fstfp_n9mcl9l_z%26e3Bip4s%3F61%3Da_z%26e3Bmd9ac0a8n8m00nd9&gsm=4&islist=&querylist='
res = requests.get(image_url)
print(res.content)

with open('花.jpg', 'wb') as file:
    file.write(res.content)
