import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import requests
from collections import Counter
import re
import os
import numpy as np

USERNAME = "Devisri-B"

TARGET_LIBRARIES = [
    # Core Data
    "pandas", "numpy", "scipy", "matplotlib", "seaborn",
    # Classical ML
    "sklearn", "xgboost", "lightgbm", "catboost",
    # Deep Learning
    "tensorflow", "torch", "keras",
    # LLM / GenAI
    "langchain", "openai", "gemini", "transformers", "llamaindex",
    # CV & MLOps
    "cv2", "mlflow", "fastapi",
    # Vector DBs
    "faiss", "pinecone", "chromadb",
]

SEARCH_PATTERNS = {
    "pandas":      r'\b(import\s+pandas|from\s+pandas|pandas)',
    "numpy":       r'\b(import\s+numpy|from\s+numpy|numpy)',
    "matplotlib":  r'\b(import\s+matplotlib|from\s+matplotlib|matplotlib)',
    "seaborn":     r'\b(import\s+seaborn|from\s+seaborn|seaborn)',
    "scipy":       r'\b(import\s+scipy|from\s+scipy|scipy)',
    "sklearn":     r'\b(import\s+sklearn|from\s+sklearn|scikit-learn|sklearn)',
    "xgboost":     r'\b(import\s+xgboost|from\s+xgboost|xgboost)',
    "lightgbm":    r'\b(import\s+lightgbm|from\s+lightgbm|lightgbm)',
    "catboost":    r'\b(import\s+catboost|from\s+catboost|catboost)',
    "tensorflow":  r'\b(import\s+tensorflow|from\s+tensorflow|tensorflow)',
    "torch":       r'\b(import\s+torch|from\s+torch|torch)',
    "keras":       r'\b(import\s+keras|from\s+keras|keras)',
    "langchain":   r'\b(import\s+langchain|from\s+langchain|langchain)',
    "openai":      r'\b(import\s+openai|from\s+openai|openai)',
    "gemini":      r'\b(import\s+google\.generativeai|from\s+google\.generativeai|google-generativeai|gemini)',
    "transformers":r'\b(import\s+transformers|from\s+transformers|transformers)',
    "llamaindex":  r'\b(llama.?index|from\s+llama_index|import\s+llama_index)',
    "cv2":         r'\b(import\s+cv2|from\s+cv2|opencv)',
    "mlflow":      r'\b(import\s+mlflow|from\s+mlflow|mlflow)',
    "fastapi":     r'\b(import\s+fastapi|from\s+fastapi|fastapi)',
    "faiss":       r'\b(import\s+faiss|from\s+faiss|faiss)',
    "pinecone":    r'\b(import\s+pinecone|from\s+pinecone|pinecone)',
    "chromadb":    r'\b(import\s+chromadb|from\s+chromadb|chromadb)',
}

# Category grouping for colors
CATEGORIES = {
    "Core Data":     {"libs": ["pandas","numpy","scipy","matplotlib","seaborn"],     "color": "#1f77b4"},
    "Classical ML":  {"libs": ["sklearn","xgboost","lightgbm","catboost"],           "color": "#ff7f0e"},
    "Deep Learning": {"libs": ["tensorflow","torch","keras"],                        "color": "#d62728"},
    "LLM / GenAI":   {"libs": ["langchain","openai","gemini","transformers","llamaindex"], "color": "#9467bd"},
    "CV & MLOps":    {"libs": ["cv2","mlflow","fastapi"],                            "color": "#2ca02c"},
    "Vector DBs":    {"libs": ["faiss","pinecone","chromadb"],                       "color": "#17becf"},
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

def get_color(lib):
    for cat, info in CATEGORIES.items():
        if lib in info["libs"]:
            return info["color"]
    return "#aaaaaa"

def generate_chart():
    repos = get_repos(USERNAME)
    total_counts = Counter()
    for repo in repos:
        counts = scan_repo_for_libraries(USERNAME, repo, TARGET_LIBRARIES)
        total_counts.update(counts)

    if not total_counts:
        print("No library usage found, using fallback data")
        total_counts = Counter({lib: 1 for lib in TARGET_LIBRARIES})

    labels = [item[0] for item in total_counts.most_common()]
    sizes  = [item[1] for item in total_counts.most_common()]
    n = len(labels)

    # Layout: spiral/grid placement so bubbles don't overlap
    np.random.seed(42)
    cols = int(np.ceil(np.sqrt(n * 1.6)))
    rows = int(np.ceil(n / cols))
    x_pos, y_pos = [], []
    for i in range(n):
        x_pos.append((i % cols) + np.random.uniform(-0.2, 0.2))
        y_pos.append((i // cols) + np.random.uniform(-0.2, 0.2))

    max_size = max(sizes)
    bubble_sizes = [((s / max_size) * 3000) + 400 for s in sizes]
    colors = [get_color(lib) for lib in labels]

    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#0d1117')   # GitHub dark background
    ax.set_facecolor('#0d1117')

    scatter = ax.scatter(x_pos, y_pos, s=bubble_sizes, c=colors,
                         alpha=0.85, edgecolors='white', linewidths=0.8)

    for i, (label, size, x, y) in enumerate(zip(labels, sizes, x_pos, y_pos)):
        ax.text(x, y + 0.01, label, ha='center', va='center',
                fontsize=max(7, min(11, 150 // n)),
                fontweight='bold', color='white')
        ax.text(x, y - 0.22, f'{size}', ha='center', va='center',
                fontsize=7, color='#cccccc')

    # Legend
    legend_patches = [
        mpatches.Patch(color=info["color"], label=cat)
        for cat, info in CATEGORIES.items()
    ]
    ax.legend(handles=legend_patches, loc='lower right',
              framealpha=0.2, labelcolor='white',
              facecolor='#161b22', edgecolor='#30363d', fontsize=9)

    ax.set_title('Library Usage Across My Repositories',
                 fontsize=15, fontweight='bold', color='white', pad=15)
    ax.set_xlim(-0.8, cols - 0.2)
    ax.set_ylim(-0.8, rows - 0.2)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('library_usage.png', dpi=150, bbox_inches='tight',
                facecolor='#0d1117')
    print("Bubble chart generated successfully!")
    for lib, count in total_counts.most_common():
        print(f"  {lib}: {count} repos")

if __name__ == "__main__":
    generate_chart()
