#!/bin/bash

for file in $(find $1 -name "*.txt"); do
	python ./transforms/process_data.py $file
done
