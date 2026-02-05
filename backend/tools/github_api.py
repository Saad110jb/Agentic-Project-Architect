import os
import requests
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("github_scraper")
def get_github_user_data(username: str):
    """
    Fetches public repository data for a specific GitHub user to identify 
    their core tech stack, languages used, and skill level.
    """
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Error: Could not fetch data for {username} (Status: {response.status_code})"
    
    repos = response.json()
    repo_summary = [
        {
            "name": r["name"], 
            "description": r.get("description"), 
            "language": r.get("language")
        } for r in repos
    ]
    return str(repo_summary)