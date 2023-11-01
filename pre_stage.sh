#!/usr/bin/expect -f
echo 'M!m3pr3@P@ss21'
spawn ssh -p 3232 mime@103.117.192.97
expect "assword:"
send "M!m3pr3@P@ss21\r"
interact