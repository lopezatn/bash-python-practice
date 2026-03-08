#!/bin/bash

path=$1

if [ -f ${path} ]; then
	mv ${path} ${path}.log.bak
	touch ${path}
else
	echo "File ${1} does not exist"
	exit 1
fi


