#!/usr/bin/expect -f
send_user "pnetdev0ps@2024\n"
spawn ssh root@103.117.192.89
expect "assword:"
send "pnetdev0ps@2024\r"