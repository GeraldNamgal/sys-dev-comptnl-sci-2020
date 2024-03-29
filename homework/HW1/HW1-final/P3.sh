#!/bin/bash
grep [0-9] apollo13.txt | wc -l
grep --help | grep "\-\-\c\o\u\n\t"
find . -maxdepth 1 -type f -name "*.py" | wc -l
find . -type f ! -perm -o=r,o=w | wc -l
find . -maxdepth 1 ! -perm -o=r,o=w | wc -l

# References:
# 1. https://stackoverflow.com/questions/7715485/how-to-only-find-files-in-a-given-directory-and-ignore-subdirectories-using-bas
# 2. https://ostechnix.com/find-files-based-permissions/ && https://unix.stackexchange.com/questions/425205/how-can-i-find-all-files-i-do-not-have-write-access-to-in-specific-folder