#!/usr/bin/expect -f
echo 'M!m3erp@L!ve@P@ss'
spawn ssh -p 3232 mime@103.117.192.76
expect "assword:"
send "M!m3erp@L!ve@P@ss\r"
interact