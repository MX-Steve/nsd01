#!/bin/bash
for i in `seq 9`
do
 for j in `seq $i`
 do
	msg=$i*$j=$[i*j]
	if [ ${#msg} -eq 5 ];then
 		echo -n $i*$j=$[i*j]"    "
	else
		echo -n $i*$j=$[i*j]"   "
	fi
 done
	echo 
done
