#!/bin/bash

echo "Test01: test tcp_v4_send_reset()  reset reason: NO_SOCKET"
python helper-script/test01-client.py

echo "Test02: test tcp_v4_send_reset()  reset reason: TCP_TIMEWAIT_SOCKET"
python helper-script/test02-server.py &
SERVER_PID=$!
sleep 1
python helper-script/test02-client.py
kill -9 $SERVER_PID

echo "Test03: test tcp_v6_send_reset() reset reason: NO_SOCKET"
python helper-script/test03-client.py