#!/bin/bash

# Run main.py
python auto-hansard/main.py > debug.txt

# Use today's date for creating a new content file
today=$(date '+%Y-%m-%d')
hugo new summary/Debate-$today.md

# Add contents of the new file to Debate-$today.md
cat auto-hansard/summary/Debate-$today.md > open-hansard-website/content/summary/Debate-$today.md

# Set the draft to false
sed -i 's/draft: true/draft: false/g' content/summary/Debate-$today.md

# Run a git command to add, commit and push the changes
# git add auto-hansard/summary/*
# git add open-hansard-website/content/summary/*
# git commit -m "Update content"
# git push