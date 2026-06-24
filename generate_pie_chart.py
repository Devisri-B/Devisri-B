import matplotlib.pyplot as plt
import requests
from collections import Counter
import re
import os

USERNAME = "Devisri-B"
TARGET_LIBRARIES = [
    # Core ML
    "pandas", "numpy", "sklearn", "scipy",
    "matplotlib", "seaborn",
    # Deep Learning
    "tensorflow", "torch", "keras",
    # Boosting
    "xgboost", "lightgbm", "catboost",
    # LLM / GenAI
    "langchain", "openai", "transformers", "llamaindex",
    # CV
    "cv2",
    # MLOps
    "mlflow", "fastapi",
    # Vector DBs
    "faiss", "pinecone", "chromadb",
]

SEARCH_PATTERNS = {
    "pandas":      r'\b(import\s+pandas|from\s+pandas|pandas)',
    "numpy":       r'\b(import\s+numpy|from\s+numpy|numpy)',
    "matplotlib":  r'\b(import\s+matplotlib|from\s+matplotlib|matplotlib)',
    "seaborn":     r'\b(import\s+seaborn|from\s+seaborn|seaborn)',
    "sklearn":     r'\b(import\s+sklearn|from\s+sklearn|scikit-learn|sklearn)',
    "tensorflow":  r'\b(import\s+tensorflow|from\s+tensorflow|tensorflow)',
    "torch":       r'\b(import\s+torch|from\s+torch|torch(?!vision|audio))',
    "keras":       r'\b(import\s+keras|from\s+keras|keras)',
    "xgboost":     r'\b(import\s+xgboost|from\s+xgboost|xgboost)',
    "lightgbm":    r'\b(import\s+lightgbm|from\s+lightgbm|lightgbm)',
    "catboost":    r'\b(import\s+catboost|from\s+catboost|catboost)',
    "langchain":   r'\b(import\s+langchain|from\s+langchain|langchain)',
    "openai":      r'\b(import\s+openai|from\s+openai|openai)',
    "transformers":r'\b(import\s+transformers|from\s+transformers|transformers)',
    "llamaindex":  r'\b(llama.?index|from\s+llama_index|import\s+llama_index)',
    "cv2":         r'\b(import\s+cv2|from\s+cv2|opencv)',
    "mlflow":      r'\b(import\s+mlflow|from\s+mlflow|mlflow)',
    "fastapi":     r'\b(import\s+fastapi|from\s+fastapi|fastapi)',
    "faiss":       r'\b(import\s+faiss|from\s+faiss|faiss)',
    "pinecone":    r'\b(import\s+pinecone|from\s+pinecone|pinecone)',
    "chromadb":    r'\b(import\s+chromadb|from\s+chromadb|chromadb)',
    "scipy":       r'\b(import\s+scipy|from\s+scipy|scipy)',
}

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

    url = f"https://api.github.com/repos/{username}/{repo_name}/git/trees/HEAD?recursive=1"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return found

    # Scan .py files AND any requirements*.txt anywhere in the repo
    relevant_files = [
        f['path'] for f in r.json().get('tree', [])
        if f['path'].endswith('.py')
        or re.search(r'requirements.*\.txt$', f['path'])
        or f['path'].endswith('.ipynb')
    ]

    for filepath in relevant_files[:30]:
        content = get_file_content(username, repo_name, filepath, headers)
        for lib in libraries:
            pattern = SEARCH_PATTERNS.get(lib, rf'\b{lib}\b')
            if re.search(pattern, content, re.IGNORECASE):
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
    for lib, count in total_counts.most_common():
        print(f"  {lib}: {count} repos")

if __name__ == "__main__":
    generate_chart()
