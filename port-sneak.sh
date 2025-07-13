#!/bin/bash

# Simple stealthy port scan
for ip in $(cat ips.txt); do
  for port in 21 22 23 80 443; do
    (echo > /dev/tcp/$ip/$port) > /dev/null 2>&1 && echo "$ip:$port open"
  done
done
