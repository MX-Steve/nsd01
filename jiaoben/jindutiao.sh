#!/bin/bash
echo ""
jindu(){
while :
do
	echo -ne '\033[34m[]\033[0m'
	sleep 0.3
done
}
echo ""
jindu &
cp -r $1 $2
kill $! 
