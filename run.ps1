# Run main.py
python auto-hansard/main.py > debug.txt

# # Use today's date for creating a new content file
$today = Get-Date -Format "yyyy-MM-dd"
hugo new "summary\Debate-$today.md"

# Add contents of the new file to Debate-$today.md
Get-Content "auto-hansard\summary\Debate-$today.md" | Add-Content "content\summary\Debate-$today.md"

# Set the draft to false
(Get-Content "content\summary\Debate-$today.md") -replace "draft = true", "draft = false" | Set-Content "content\summary\Debate-$today.md"

# Run a git command to add, commit and push the changes
git add .
git commit -m "Update content - $today"
git push
