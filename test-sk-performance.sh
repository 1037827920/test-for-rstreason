#!/bin/bash

# 设置循环次数，这里设为1000次，可根据需要修改
LOOP_TIMES=1000

for ((i=1; i<=$LOOP_TIMES; i++))
do
    echo "Count: $i"
    echo "Test: test tcp_send_active_reset()  reset reason: TCP_STATE"
    nc -l 8080 > /dev/null 2>&1 &
    NC_PID=$!
    python helper-script/test04-client.py
    echo "--------------------------------"
done