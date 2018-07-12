#!/bin/bash
read -p "请出拳：[石头，剪刀，布]" n
j=$[RANDOM%3+1]
if [ $j -eq 1 ];then
 j="石头"
elif [ $j -eq 2 ];then
 j='剪刀'
elif [ $j -eq 3 ];then
 j="布"
else
 echo "出错了，推出"
 exit 2
fi

if [ $j == $n ];then
 echo "平局"
else
 if [ $n == "石头" ];then
	if [ $j == "剪刀" ];then
		echo "你赢了"
	else
		echo "你输了"
	fi
 elif [ $n == "剪刀" ];then
	if [ $j == "布" ];then
		echo "你赢了"
	else
		echo "你输了"
	fi
 else
	if [ $j == "石头" ];then
		echo "你赢了"
	else
		echo "你输了"
	fi
 fi
fi
