import matplotlib.pyplot as plt
import requests
import base64
from collections import Counter
import re

# CONFIGURATION
USERNAME = "Devisri-B"
# libraries to track
TARGET_LIBRARIES = ["pandas", "numpy", "matplotlib", "seaborn", "sklearn", "tensorflow", "torch", "scipy", ]

def get_repos(username):
    # Fetch all public repos for the user
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return [repo['name'] for repo in response.json()]

def scan_repo_for_libraries(username, repo_name, libraries):
    pass 

def generate_chart():
    # Simulated data based on your image
    labels = ['sklearn', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'torch', 'tensorflow', 'scipy']
    sizes = [30.2, 18.6, 18.6, 14.0, 7.0, 4.7, 4.7, 2.3]
    
    # Colors 
    colors = ['#2ca02c', '#aec7e8', '#1f77b4', '#ffbb78', '#ff9896', '#d62728', '#98df8a', '#ff7f0e']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Library Usage Percentage Across All Repositories')
    
    # Save the chart
    plt.savefig('library_usage.png')
    print("Chart generated successfully: library_usage.png")

if __name__ == "__main__":
    generate_chart()
