#!/bin/bash
for i in {1..254}
do
ping -i 0.1 -c2 176.4.16.$i &>/dev/null
if [ $? -eq 0 ];then
	echo 176.4.16.$i ok
fi
done
