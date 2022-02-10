#!/bin/bash

while :
do
    echo -n "输入1到5之间的数字："
    read NUM
    case ${NUM} in
	1|2|3|4|5) echo "你输入的数字为：${NUM}";;
	*) echo "你输入的数字不是在1到5之间"
		continue
	    	echo "游戏结束";;
    esac
done

#while :
#do
#    echo -n "输入1到5之间的数字："
#    read NUM
#    case ${NUM} in
#        1|2|3|4|5) echo "你输入的数字为：${NUM}";;
#        *) echo "你输入的数字不是在1到5之间 游戏结束"
#                break ;;
#    esac
#done

