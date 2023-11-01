#!/usr/bin/expect -f
echo 'M!m3erp@L!ve@P@ss'
spawn ssh -p 3232 erp@103.117.192.120
expect "assword:"
send "M!m3erp@L!ve@P@ss\r"
interact