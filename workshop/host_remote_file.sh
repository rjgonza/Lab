#!/bin/bash
function usage {
	echo "Usage: $0 <host> <full qualified path file> [ip] [port]"
	exit 1
}

[[ $# -lt 2 ]] && usage

corectl=/data/coreCtl
host=$1
file=$2
[[ -n $3 ]] && ip=$3 || ip="0.0.0.0"
[[ -n $4 ]] && port=$4 || port=15358

echo "Connection opened:"
echo "Going to host $file on $host over $ip:$port"
$corectl $host <<here
cat $file | nc -l $ip $port 
here
echo "Connection closed"
