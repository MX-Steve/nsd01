#!/bin/bash
#冒泡排序
read -p "输入要比较的数字: " arr
array=($arr)
#count:数组成员个数
count=${#array[*]}
for i in `seq $[count-1]`
do
	for j in `seq $[count-i]`
	do
		if [ ${array[j-1]} -gt ${array[j]} ];then
			tmp=${array[j]}
			array[j]=${array[j-1]}
			array[j-1]=$tmp
		fi		
	done
done
echo 排序后的结果为：${array[@]}
