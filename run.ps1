# Run main.py
python auto-hansard/main.py > debug.txt

# Use yesterday's date for creating a new content file
$yesterday = (Get-Date).AddDays(-1).ToString("yyyy-MM-dd")
# Get yesterdays month in words
$month = (Get-Date).AddDays(-1).ToString("MMMM")
# Get yesterdays day
$day = (Get-Date).AddDays(-1).ToString("dd")
# Get yesterdays year
$year = (Get-Date).AddDays(-1).ToString("yyyy")

hugo new "posts\Hansard Summary for $month $day, $year.md"

# Add contents of the new file to Debate-$today.md
Get-Content "auto-hansard\summary\Debate-$yesterday.md" | Add-Content "content\posts\Hansard Summary for $month $day, $year.md"

# Set the draft to false
(Get-Content "content\posts\Hansard Summary for $month $day, $year.md") -replace "draft = true", "draft = false" | Set-Content "content\posts\Hansard Summary for $month $day, $year.md"

# Run git to publish website
# cd public
# git add .
# git commit -m "Update website content - $yesterday"
# git push

# cd ..

# # Run a git command to add, commit and push the changes
# git add .
# git commit -m "Update content - $yesterday"
# git push
