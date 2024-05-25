#!/bin/bash

# Run main.py
python auto-hansard/main.py > debug.txt

# Use yesterday's date for creating a new content file
yesterday=$(date -d "yesterday 13:00" '+%Y-%m-%d')
hugo new summary/Debate-$yesterday.md

# Add contents of the new file to Debate-$today.md
cat auto-hansard/summary/Debate-$yesterday.md > open-hansard-website/content/summary/Debate-$yesterday.md

# Set the draft to false
sed -i 's/draft: true/draft: false/g' content/summary/Debate-$yesterday.md

# Run a git command to add, commit and push the changes
git add .
git commit -m "Update content - $yesterday"
git push