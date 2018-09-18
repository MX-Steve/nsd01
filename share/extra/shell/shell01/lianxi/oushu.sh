#!/bin/bash
#打开调试
#function DEBUG () { true && $@; }
#关闭
function DEBUG () { false && $@; }
id=(1 2 3 4 5 6 7 8 9)
len=${#id[@]}
for ((i=0;i<$len;i++));do
	DEBUG	echo " line==${LINENO} i==${i}, ${#id[@]}"
	if (($((id[i]%2))));then
		unset id[i]
	fi
done
echo ${id[@]}
