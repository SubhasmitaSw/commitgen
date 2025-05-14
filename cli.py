import os
import subprocess
import sys
import argparse

# Add vendor directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vendor'))

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

RELAXAI_API_KEY = os.getenv('RELAXAI_API_KEY')
RELAXAI_API_ENDPOINT = os.getenv('RELAXAI_API_ENDPOINT')
RELAXAI_MODEL_NAME = os.getenv('RELAXAI_MODEL_NAME')

def get_git_diff():
    """
    Retrieves the staged changes using `git diff --cached`.
    
    Returns:
        str: The staged changes as a string.
    
    Exits:
        int: 1 if no staged changes are found or if there's a Git error.
    """
    try:
        diff = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True
        ).stdout.strip()
        if not diff:
            print("⚠️ No staged changes found. Use `git add` first.")
            exit(1)
        return diff
    except Exception as e:
        print(f"❌ Git error: {e}")
        exit(1)

def generate_commit_message(diff, bonkers=False):
    """
    Generates a commit message using the Relax AI API based on the provided diff.
    
    Args:
        diff (str): The staged changes to generate a commit message for.
        bonkers (bool, optional): Whether to generate a humorous commit message. Defaults to False.
    
    Returns:
        str: The generated commit message.
    
    Exits:
        int: 1 if there's an error with the Relax AI API call.
    """
    headers = {
        "Authorization": f"Bearer {RELAXAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": RELAXAI_MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that writes clear, concise one-line Git commit messages based on code changes. Label the change as bug fix 🐛, new feature ✨, improvement 🚀, documentation 📚, or other 🤔, with relevant emojis. Use a professional tone unless directed otherwise."
            },
            {
                "role": "user",
                "content": f"Generate a {'hilarious' if bonkers else 'professional'} commit message for these changes (max 1 line, imperative mood, include label):\n{diff}"
            }
        ]
    }
    try:
        response = requests.post(
            RELAXAI_API_ENDPOINT,
            headers=headers,
            json=payload
        )
        response.raise_for_status()  # Raise error if API call fails
        return response.json()["choices"][0]["message"]["content"].strip('"')
    except Exception as e:
        print(f"❌ Relax AI API error: {e}")
        exit(1)

def confirm_and_commit(message):
    """
    Prompts the user to confirm, edit, or abort the commit with the given message.
    
    Args:
        message (str): The commit message to be used for the commit.
    """
    print(f"\n📝 Suggested commit message: \n{message}")
    choice = input("\n✅ Commit with this message? (Y/edit/abort): ").strip().lower()
    
    if choice == "y":
        subprocess.run(["git", "commit", "-m", message], check=True)
        print("🎉 Commit created!")
    elif choice == "edit":
        new_message = input("✏️ Enter new commit message: ")
        subprocess.run(["git", "commit", "-m", new_message], check=True)
        print("🎉 Commit created with custom message!")
    else:
        print("🚫 Commit aborted.")

def main():
    """
    The main entry point for the CLI tool.
    
    Parses command-line arguments and orchestrates the commit message generation and commit process.
    """
    parser = argparse.ArgumentParser(description='AI Git Commit Message Generator (Powered by Relax AI)')
    parser.add_argument('--bonkers', action='store_true', help='Generate a humorous commit message')
    args = parser.parse_args()

    print("🤖 AI Git Commit Message Generator (Powered by Relax AI)")
    diff = get_git_diff()
    commit_msg = generate_commit_message(diff, args.bonkers)
    confirm_and_commit(commit_msg)

if __name__ == "__main__":
    main()