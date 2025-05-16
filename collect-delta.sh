#!/bin/bash

TRACE_PIPE="/sys/kernel/debug/tracing/trace_pipe"

sum=0
count=0

# capture Ctrl+C signal
trap 'echo -e "\n----   Result   ----"
      echo "The sum of delta : ${sum}"
      echo "Count            : ${count}"
      exit 0' INT

while IFS= read -r line; do
    if [[ $line =~ delta:[[:space:]]*([0-9]+) ]]; then
        delta=${BASH_REMATCH[1]}
        sum=$((sum + delta))      # $$sum = sum + delta$$
        count=$((count + 1))
    fi
done < "$TRACE_PIPE"