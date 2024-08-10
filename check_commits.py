import requests
import os

# Constants
GITHUB_REPO_OWNER = "devopsaziz"
GITHUB_REPO_NAME = "htmlassignment"
GITHUB_TOKEN = "*****************"
LAST_COMMIT_FILE = "/home/ubuntu/assignment/last_commit.txt"

# Function to get the latest commit from the GitHub repository
def get_latest_commit():
    url = f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/commits"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()[0]['sha']
    else:
        print(f"Error: Unable to fetch commits. Status code: {response.status_code}")
        return None

# Function to get the last saved commit from the file
def get_last_saved_commit():
    try:
        with open(LAST_COMMIT_FILE, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Function to save the latest commit to the file
def save_last_commit(commit_sha):
    with open(LAST_COMMIT_FILE, 'w') as file:
        file.write(commit_sha)

# Main function to check for new commits and update the file
def main():
    latest_commit = get_latest_commit()
    last_saved_commit = get_last_saved_commit()

    if latest_commit and latest_commit != last_saved_commit:
        print("New commit found!")
        save_last_commit(latest_commit)
        return True

    print("No new commit.")
    return False

# Run the main function
if __name__ == "__main__":
    main()
