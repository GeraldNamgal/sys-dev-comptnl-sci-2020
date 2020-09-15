#!/bin/bash
for file in *; do
    if [ -f $file ]; then
        echo "$file $(< $file wc -l)"
    fi
done

# References:
# 1. https://unix.stackexchange.com/questions/351210/loop-through-files-excluding-directories
# 2. https://unix.stackexchange.com/questions/126998/getting-the-line-count-and-storing-in-a-result-set