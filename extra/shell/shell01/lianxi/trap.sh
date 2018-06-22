#!/bin/bash
function exittrap(){
	echo "$0 exit status $?"
	#$0
}
function foo(){
	echo is foo
	return 1
}
trap 'exittrap' ERR EXIT


foo


sleep 3

echo the end
exit 0
