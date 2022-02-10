#!/bin/bash

#echo "请输入1到4之间的数字："
#echo "你输入的数字为："
#read NUM
#case ${NUM} in 
#    1)  echo "你选择了1" ;;
#    2)  echo "你选择了2" ;;
#    3)  echo "你选择了3" ;;
#    4)  echo "你选择了4" ;;
#    *)  echo "你没有选择1到4之间的数字" ;;
#esac

echo "请输入喜欢的网址域名："
echo "你输入的域名为："
read site

case ${site} in 
    "runoob") echo "菜鸟教程";;
    "baidu") echo "百度";;
    "taobao") echo "淘宝";;
    *) echo "您选择的不在范围内";;
esac
