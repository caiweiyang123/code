#!/bin/bash

funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算。。。"
    echo "输入第一个数字："
    read num1
    echo "输入第二个数字："
    read num2
    echo "两个数字分别是${num1}和${num2}!"
    return $(($num1+$num2))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
