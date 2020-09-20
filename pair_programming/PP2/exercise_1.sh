#!/bin/bash
read -r -p 'Enter a file to commit: ' filename
git add $filename
git status
read -r -p 'Do you wish to continue? ('Y' or 'N'): ' choice
if [ "$choice" = "N" ]; then
    exit 1
elif [ "$choice" = "Y" ]; then
    read -r -p 'Please enter a commit message: ' message
else
    echo "Invalid response entered. Quitting..."
    exit 1
fi
git commit -m "$message"
git status
read -r -p 'Do you wish to continue? ('Y' or 'N'): ' choice
if [ "$choice" = "N" ]; then
    exit 1
elif [ "$choice" = "Y" ]; then
    git push
else
    echo "Invalid response entered. Quitting..."
    exit 1
fi
