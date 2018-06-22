#!/bin/bash
#定义trap函数，跟踪状态变化
function exittrap(){
	echo "$0 exit status $?"
	#$0
}
#自定义函数
function foo(){
	echo is foo
	return 1
}
#执行trap函数，跟踪捕捉ERR和EXIT状态变化
trap 'exittrap' ERR EXIT


foo


sleep 3

echo the end
exit 0
