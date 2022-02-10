#!/bin/bash

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第九个参数为 $9 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总共有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
    echo "当前进程号为 $$ "
    echo "最后一个进程ID号为 $! "
}
funWithParam 1 2 3 4 5 6 7 8 29 200 22
