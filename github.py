import requests
import subprocess
import os
# Create a new GitHub repository -------------------------------->

def create_github_repo(repo_name, repo_desc, github_username, github_token):
    user_url = f"https://api.github.com/user"
    response = requests.get(user_url, auth=(github_username, github_token))
    if response.status_code != 200:
        print("Error authenticating with GitHub")
        exit(1)

    # Get user's information from GitHub API
    user_data = response.json()
    print(user_data["repos_url"])

    # Set up repository creation parameters
    repo_params = {
        "name": repo_name,
        "description": repo_desc,
        "private": False
    }

    # Create new repository with GitHub API
    repo_url = "https://api.github.com/user/repos"
    response = requests.post(repo_url, json=repo_params, auth=(github_username, github_token))
    if response.status_code != 201:
        print("Error creating repository")
        print(response.json())
        exit(1)

    print(f"Repository '{repo_name}' created successfully!")

# Set up repository creation parameters
repo_name = input("Enter your repository name: ")
repo_desc = input("Enter a description for your repository: ")
github_username = input("Enter your GitHub username: ")
github_token = os.getenv("GITHUB_TOKEN")

if(github_token):
    github_token = github_token

else:
    print("Please set the GITHUB_TOKEN environment variable or provide a valid GitHub token")
    github_token=input("Enter your GitHub Token: ")


# Create new GitHub repository
create_github_repo(repo_name, repo_desc, github_username, github_token)


# Initialize the repository locally
#---------------------------------------------------------------->
def initialize_repo():
    # Check if the current directory is already a git repository
    if os.path.isdir('.git'):
        print("This directory is already a git repository.")
    else:
        # Create a new Git repository in the current directory
        subprocess.run(['git', 'init'])
        print("Initialized a new git repository.")

def add_files():
    # Add files to the repository
    with open('README.md', 'w') as f:
        f.write('This is a sample repository.')
    with open('LICENSE', 'w') as f:
        f.write('License information.')

def commit_changes(message):
    # Commit changes with a meaningful message
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', message])

def push_to_github():
    # Push changes to GitHub
    subprocess.run(['git', 'remote', 'add', 'origin', f'https://github.com/{github_username}/{repo_name}.git'])
    subprocess.run(['git', 'push' ,'--set-upstream', 'origin', 'master'])

def main():
    # Initialize the repository
    initialize_repo()

    # Add files
    add_files()

    # Commit changes
    message = input("Enter a commit message: ")
    commit_changes(message)

    # Push changes to GitHub
    push_to_github()

if __name__ == '__main__':
    main()