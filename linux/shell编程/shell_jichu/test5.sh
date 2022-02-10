#!/bin/bash
#string="abcd"
#echo ${#string}
string="runoob is a great site"
#echo ${string:1:4} # 输出unoo
echo `expr index "$string" i`
