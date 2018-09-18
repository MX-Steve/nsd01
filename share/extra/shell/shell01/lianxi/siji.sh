#!/bin/bash
function exittrap(){
	echo "$0 exit status $?"
	$0
}
function foo(){
	echo is foo
	return 0	
}
trap 'exittrap' EXIT

sleep 1

foo

sleep 3

echo the end
exit 1
