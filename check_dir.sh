#!/bin/bash

set -e
set -u
set -o pipefail

directory=$1

if [ -d $1 ]; then
	echo "{$1} Directory found"
else
	mkdir $1
	echo "{$1} Directory created"
fi
