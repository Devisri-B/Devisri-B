import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import squarify
import requests
from collections import Counter
import re
import os

USERNAME = "Devisri-B"

TARGET_LIBRARIES = [
    "pandas", "numpy", "scipy", "matplotlib", "seaborn",
    "sklearn", "xgboost", "lightgbm", "catboost",
    "tensorflow", "torch", "keras",
    "langchain", "langgraph", "openai", "gemini", "transformers", "llamaindex",
    "cv2", "mlflow", "fastapi",
    "faiss", "pinecone", "chromadb",
]

SEARCH_PATTERNS = {
    "pandas":       r'\b(import\s+pandas|from\s+pandas|pandas)',
    "numpy":        r'\b(import\s+numpy|from\s+numpy|numpy)',
    "matplotlib":   r'\b(import\s+matplotlib|from\s+matplotlib|matplotlib)',
    "seaborn":      r'\b(import\s+seaborn|from\s+seaborn|seaborn)',
    "scipy":        r'\b(import\s+scipy|from\s+scipy|scipy)',
    "sklearn":      r'\b(import\s+sklearn|from\s+sklearn|scikit-learn|sklearn)',
    "xgboost":      r'\b(import\s+xgboost|from\s+xgboost|xgboost)',
    "lightgbm":     r'\b(import\s+lightgbm|from\s+lightgbm|lightgbm)',
    "catboost":     r'\b(import\s+catboost|from\s+catboost|catboost)',
    "tensorflow":   r'\b(import\s+tensorflow|from\s+tensorflow|tensorflow)',
    "torch":        r'\b(import\s+torch|from\s+torch|torch)',
    "keras":        r'\b(import\s+keras|from\s+keras|keras)',
    "langchain":    r'\b(import\s+langchain|from\s+langchain|langchain)',
    "langgraph":    r'\b(import\s+langgraph|from\s+langgraph|langgraph)',
    "openai":       r'\b(import\s+openai|from\s+openai|openai)',
    "gemini":       r'\b(import\s+google\.generativeai|from\s+google\.generativeai|google-generativeai|gemini)',
    "transformers": r'\b(import\s+transformers|from\s+transformers|transformers)',
    "llamaindex":   r'\b(llama.?index|from\s+llama_index|import\s+llama_index)',
    "cv2":          r'\b(import\s+cv2|from\s+cv2|opencv)',
    "mlflow":       r'\b(import\s+mlflow|from\s+mlflow|mlflow)',
    "fastapi":      r'\b(import\s+fastapi|from\s+fastapi|fastapi)',
    "faiss":        r'\b(import\s+faiss|from\s+faiss|faiss)',
    "pinecone":     r'\b(import\s+pinecone|from\s+pinecone|pinecone)',
    "chromadb":     r'\b(import\s+chromadb|from\s+chromadb|chromadb)',
}

CATEGORIES = {
    "Core Data":     {"libs": ["pandas","numpy","scipy","matplotlib","seaborn"],                       "color": "#1f6feb"},
    "Classical ML":  {"libs": ["sklearn","xgboost","lightgbm","catboost"],                            "color": "#f78166"},
    "Deep Learning": {"libs": ["tensorflow","torch","keras"],                                          "color": "#db6d28"},
    "LLM / GenAI":   {"libs": ["langchain","langgraph","openai","gemini","transformers","llamaindex"], "color": "#8957e5"},
    "CV & MLOps":    {"libs": ["cv2","mlflow","fastapi"],                                              "color": "#3fb950"},
    "Vector DBs":    {"libs": ["faiss","pinecone","chromadb"],                                         "color": "#39c5cf"},
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


def add_scaled_labels(ax, rects, labels, sizes):
    """Add text labels that scale with box size and clip to box boundaries."""
    total = sum(sizes)
    norm_sizes = [s / total for s in sizes]
    for rect, label, norm_size in zip(rects, labels, norm_sizes):
        x = rect['x']
        y = rect['y']
        w = rect['dx']
        h = rect['dy']
        if w < 5 or h < 5:
            continue
        font_size = max(7, min(20, 20 * (norm_size ** 0.35)))
        cx = x + w / 2
        cy = y + h / 2
        parts = label.split('\n')
        name = parts[0]
        count_str = parts[1] if len(parts) > 1 else ''
        txt = ax.text(
            cx, cy, name,
            ha='center', va='center',
            fontsize=font_size, fontweight='bold', color='white',
            clip_on=True,
            wrap=False,
        )
        renderer = ax.get_figure().canvas.get_renderer()
        x0_disp, y0_disp = ax.transData.transform((x, y))
        x1_disp, y1_disp = ax.transData.transform((x + w, y + h))
        box_w_disp = abs(x1_disp - x0_disp)
        box_h_disp = abs(y1_disp - y0_disp)
        while font_size > 7:
            bbox = txt.get_window_extent(renderer=renderer)
            if bbox.width <= box_w_disp * 0.92 and bbox.height <= box_h_disp * 0.45:
                break
            font_size -= 1
            txt.set_fontsize(font_size)
        bbox = txt.get_window_extent(renderer=renderer)
        if count_str and box_h_disp > bbox.height * 2.2:
            txt.set_position((cx, cy + bbox.height * 0.3))
            ax.text(
                cx, cy - bbox.height * 0.3, count_str,
                ha='center', va='center',
                fontsize=max(6, font_size - 3), color='white',
                clip_on=True,
            )


def generate_chart():
    repos = get_repos(USERNAME)
    total_counts = Counter()
    for repo in repos:
        counts = scan_repo_for_libraries(USERNAME, repo, TARGET_LIBRARIES)
        total_counts.update(counts)

    if not total_counts:
        print("No library usage found, using fallback data")
        total_counts = Counter({lib: 1 for lib in TARGET_LIBRARIES})

    sorted_items = total_counts.most_common()
    labels = [item[0] for item in sorted_items]
    sizes  = [item[1] for item in sorted_items]
    colors = [get_color(lib) for lib in labels]

    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')

    normed = squarify.normalize_sizes(sizes, 100, 100)
    rects  = squarify.squarify(normed, 0, 0, 100, 100)

    squarify.plot(
        sizes=sizes,
        label=None,
        color=colors,
        alpha=0.88,
        edgecolor='#0d1117',
        linewidth=2,
        ax=ax
    )

    full_labels = [f"{l}\n{s} repos" for l, s in zip(labels, sizes)]
    add_scaled_labels(ax, rects, full_labels, sizes)

    legend_patches = [
        mpatches.Patch(color=info["color"], label=cat)
        for cat, info in CATEGORIES.items()
    ]
    ax.legend(handles=legend_patches, loc='upper left',
              framealpha=0.3, labelcolor='white',
              facecolor='#161b22', edgecolor='#30363d', fontsize=9)

    ax.set_title('Library Usage Across My Repositories',
                 fontsize=30, fontweight='bold', color='white', pad=15)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('library_usage.png', dpi=150, bbox_inches='tight',
                facecolor='#0d1117')
    print("Treemap generated successfully!")
    for lib, count in total_counts.most_common():
        print(f"  {lib}: {count} repos")


if __name__ == "__main__":
    generate_chart()
