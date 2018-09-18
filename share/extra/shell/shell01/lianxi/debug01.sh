#!/bin/bash
#trap 开始跟踪它之后的所有行
trap 'echo "before execute line:$LINENO, a=$a,b=$b,c=$c"' DEBUG
a=2
if [ "$a" -eq 1 ];then
	b=2
else
	b=1
fi
c=3
exit
