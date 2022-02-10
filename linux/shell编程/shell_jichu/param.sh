#!/bin/bash
# M'r cai
# invest_cai@163.com

#echo "shell 传递参数实例";
#echo "执行的文件名为：$0";
#echo "第一个参数为：$1";

#echo "传递的参数个数为：$#";
#echo "传递的参数作为一个字符串显示：$*";
#echo "当前脚本运行的进程号为：$$";
#echo "后台最后一个进程号为：$!";

echo "--- \$* 演示 ---"
for i in "$*";do
    echo $i
done

echo "--- \$@ 演示 ---"
for i in "$@";do
    echo $i
done

