#!/bin/bash
printf `tput setaf 2; tput bold` "color show" `tput sgr0`

for i in `seq 7`;do
	echo `tput setaf $i` "show me the money " `tput sgr0`
done

printf '\n'`tput setaf 2;tput setab 0;tput bold`"background color" `tput sgr0` '\n\n'

for i in `seq 7`;do
	echo `tput setab $i` "show me the money" `tput sgr0`
done

exit 0
