#!/usr/bin/expect -f
echo 'M!m3erp@P@ss21'
spawn ssh -p 3232 mime-erp@103.117.192.110
expect "assword:"
send "M!m3erp@P@ss21\r"
interact