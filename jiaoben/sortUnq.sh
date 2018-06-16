#!/bin/bash
#排序并去重
#arr==>要排序的数组
arr=(11 87 12 11 87 6 5 2 3 2 4 3 5 2 6)
#count==>数组中成员个数
count=${#arr[@]}
#new==>排序去重后存放在该数组
new=()
#cn==>排序去重后新数组成员个数
cn=${#new[@]}
#去重
for i in `seq $count`
do
	tmp=${arr[$i-1]}
	c=0
	for j in `seq ${#new[@]}`
	do
		if [ $tmp == ${new[j-1]} ];then
			break
		fi
		let c++
	done	
	if [ $c -eq ${#new[@]} ];then
		new[$cn]=${arr[$i-1]}
		let cn++
	fi
done
#排序
for i in `seq $[cn-1]`
do
        for j in `seq $[cn-i]`
        do
                if [ ${new[j-1]} -gt ${new[j]} ];then
                        tmp=${new[j]}
                        new[j]=${new[j-1]}
                        new[j-1]=$tmp
                fi
        done
done
echo 排序去重后的数组： ${new[*]}
