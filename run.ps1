# Run main.py
python auto-hansard/main.py > debug.txt

# Use yesterday's date for creating a new content file
$yesterday = (Get-Date).AddDays(-1).ToString("yyyy-MM-dd")
hugo new "summary\Debate-$yesterday.md"

# Add contents of the new file to Debate-$today.md
Get-Content "auto-hansard\summary\Debate-$yesterday.md" | Add-Content "content\summary\Debate-$yesterday.md"

# Set the draft to false
(Get-Content "content\summary\Debate-$yesterday.md") -replace "draft = true", "draft = false" | Set-Content "content\summary\Debate-$yesterday.md"

# Run git to publish website
cd public
git add .
git commit -m "Update website content - $yesterday"
git push

cd ..

# Run a git command to add, commit and push the changes
git add .
git commit -m "Update content - $yesterday"
git push
