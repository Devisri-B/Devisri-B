import matplotlib.pyplot as plt
import requests
from collections import Counter
import re
import os

USERNAME = "Devisri-B"
TARGET_LIBRARIES = ["pandas", "numpy", "matplotlib", "seaborn", 
                    "sklearn", "tensorflow", "torch", "scipy"]

def get_repos(username):
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Authorization": f"token {token}"} if token else {}
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    response = requests.get(url, headers=headers)
    return [repo['name'] for repo in response.json()]

def get_file_content(username, repo, path, headers):
    url = f"https://api.github.com/repos/{username}/{repo}/contents/{path}"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        import base64
        return base64.b64decode(r.json()['content']).decode('utf-8', errors='ignore')
    return ""

def scan_repo_for_libraries(username, repo_name, libraries):
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Authorization": f"token {token}"} if token else {}
    found = Counter()
    
    # Get repo tree
    url = f"https://api.github.com/repos/{username}/{repo_name}/git/trees/HEAD?recursive=1"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return found
    
    py_files = [f['path'] for f in r.json().get('tree', []) 
                if f['path'].endswith('.py') or f['path'] in ('requirements.txt',)]
    
    for filepath in py_files[:20]:  # limit to avoid rate limits
        content = get_file_content(username, repo_name, filepath, headers)
        for lib in libraries:
            if re.search(rf'\b(import\s+{lib}|from\s+{lib})', content):
                found[lib] += 1
    return found

def generate_chart():
    repos = get_repos(USERNAME)
    total_counts = Counter()
    for repo in repos:
        counts = scan_repo_for_libraries(USERNAME, repo, TARGET_LIBRARIES)
        total_counts.update(counts)
    
    if not total_counts:
        print("No library usage found, using fallback data")
        total_counts = Counter({lib: 1 for lib in TARGET_LIBRARIES})
    
    labels = list(total_counts.keys())
    sizes = list(total_counts.values())
    colors = ['#2ca02c','#aec7e8','#1f77b4','#ffbb78','#ff9896','#d62728','#98df8a','#ff7f0e']
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)])
    plt.title('Library Usage Percentage Across All Repositories')
    plt.savefig('library_usage.png')
    print("Chart generated successfully!")

if __name__ == "__main__":
    generate_chart()
