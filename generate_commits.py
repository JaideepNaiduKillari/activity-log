import os
import subprocess
from datetime import datetime, timedelta

# Configuration
repo_path = os.getcwd()  # Use current directory
start_date = datetime.now() - timedelta(days=730)  # Start 2 years ago
end_date = datetime.now()  # Up to today
max_commits_per_day = 5  # Max commits per day

# Generate commits
current_date = start_date
while current_date <= end_date:
    # Randomize the number of commits for the day (0 to max_commits_per_day)
    num_commits = (hash(current_date.day) % (max_commits_per_day + 1))
    for commit in range(num_commits):
        # Create or modify a file
        with open("activity_log.txt", "a") as file:
            file.write(f"Commit on {current_date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Add changes
        subprocess.run(["git", "add", "."])
        
        # Commit with a specific date
        commit_message = f"Commit on {current_date.strftime('%Y-%m-%d')}"
        commit_date = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        subprocess.run(["git", "commit", "-m", commit_message, "--date", commit_date])
    
    # Move to the next day
    current_date += timedelta(days=1)

# Push changes to GitHub
subprocess.run(["git", "push", "origin", "main"])
