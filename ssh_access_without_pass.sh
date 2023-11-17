#!/usr/bin/expect -f
echo 'testpass'
spawn ssh -p 3232 mime@103.117.192.97
expect "assword:"
send "testpass\r"
interact