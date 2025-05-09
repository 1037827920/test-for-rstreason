#!/bin/bash

echo "Test04: test tcp_send_active_reset()  reset reason: TCP_STATE"
nc -l 8080 > /dev/null 2>&1 &
NC_PID=$!
sleep 1
python helper-script/test04-client.py

echo "Test05: test tcp_send_active_reset()  reset reason: TCP_ABORT_ON_CLOSE"
python helper-script/test05-server.py &
sleep 1
python helper-script/test05-client.py