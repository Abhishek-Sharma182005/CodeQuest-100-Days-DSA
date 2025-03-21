import json
import requests
import os

# GitHub API Token (use environment variable)
GITHUB_TOKEN = os.getenv("CODEQUEST_ACCESS_TOKEN")
REPO_OWNER = "Abhishek-Sharma182005"
REPO_NAME = "CodeQuest-100-Days-DSA"
LEADERBOARD_FILE = "leaderboard.json"

# Fetch participant data from the GitHub repository
def get_participants():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contributors"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    
    print(f"Error fetching contributors: {response.status_code} - {response.text}")
    return []

# Load the existing leaderboard and ensure it contains the required structure
def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r") as file:
                leaderboard = json.load(file)
                if "participants" not in leaderboard:
                    raise ValueError("Missing 'participants' key in leaderboard.json")
                return leaderboard
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error: leaderboard.json is corrupted ({e}). Resetting leaderboard.")
    
    return {"participants": []}  # Ensure the file has the correct format

# Update scores based on contributions
def update_leaderboard():
    leaderboard = load_leaderboard()
    participants = get_participants()
    
    for participant in participants:
        username = participant["login"]
        commits = participant["contributions"]

        # Calculate scores
        daily_submissions = commits
        social_media_posts = 0.5 * commits  # Assume every commit corresponds to a social post
        total_score = daily_submissions + social_media_posts

        updated_entry = {
            "username": username,
            "total_score": total_score,
            "daily_submissions": daily_submissions,
            "social_media_posts": social_media_posts
        }

        # Add/update participant in leaderboard
        found = False
        for entry in leaderboard["participants"]:
            if entry["username"] == username:
                entry.update(updated_entry)
                found = True
                break

        if not found:
            leaderboard["participants"].append(updated_entry)

    # Save updated leaderboard
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

    print("Leaderboard updated successfully!")

# Run update
if __name__ == "__main__":
    update_leaderboard()
