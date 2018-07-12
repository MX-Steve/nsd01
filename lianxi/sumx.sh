#!/bin/bash
read -p "输入一个数字：" num
num=${num:-1}
sum=0;i=1
while [ $i -le $num ]
do
	let sum+=i
	let i++
done
echo $sum
