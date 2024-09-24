#!/bin/bash
ftp -nv 192.168.1.105 << EOF
quote USER anonymous
quote PASS me@email.com
passive
put go_doom
bye
EOF
