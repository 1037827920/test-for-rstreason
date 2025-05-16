#!/bin/bash

# 设置循环次数，这里设为1000次，可根据需要修改
LOOP_TIMES=1000

for ((i=1; i<=$LOOP_TIMES; i++))
do
    echo "Count: $i"
    echo "Test: test tcp_v4_send_reset()  reset reason: NO_SOCKET"
    python helper-script/test01-client.py
    echo "--------------------------------"
done
