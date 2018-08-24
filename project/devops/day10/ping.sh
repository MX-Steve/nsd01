#!/bin/bash
date
for ip in 176.4.13.{1..254}
do
    ping -c2 $ip &>/dev/null && echo "$ip : up" || echo "$ip : down"
done