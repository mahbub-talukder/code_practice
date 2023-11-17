#!/usr/bin/expect -f
echo 'testpass'
spawn ssh -p 9859 test@100.117.182.97
expect "assword:"
send "testpass\r"
interact