<h1 align="center">Hi 👋, I'm Devi Sri Bandaru</h1>

<h3 align="center">
  I don't just train models; I engineer resilient, deterministic AI systems.
  <br/>
  My passion lies in taking fragile LLM prototypes and hardening them into scalable, agentic microservices. Whether it's architecting graph-based Self-RAG pipelines with zero-cost NLI guardrails, publishing open-source data tooling, or optimizing low-latency vector databases, I operate at the intersection of high-performance engineering and applied cognitive intelligence.
</h3>

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-Live_Website-2563EB?style=for-the-badge&logo=google-chrome&logoColor=white)](https://devisri-b.github.io/Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devisri-bandaru)
[![Medium](https://img.shields.io/badge/Medium-Articles-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@bandarudevisri.ds)
[![Email](https://img.shields.io/badge/Email-Get_in_Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bandarudevisri.ds@gmail.com)

</div>

<br/>

## 🔬 About Me

- 🎓 **MS in Computer Science** from **Kent State University** (GPA: **3.97 / 4.0**) | BS in CS (GPA: 3.7 / 4.0).
- 📜 **Researcher** with peer-reviewed publications across **IEEE CAI 2026**, **MDPI AI (2025)**, and **SKASE (2024)**.
- 📦 **Open-Source Tooling:** Creator & Maintainer of [`wranglefy`](https://pypi.org/project/wranglefy/) and [`tprdbreader`](https://pypi.org/project/tprdbreader/) on PyPI (**80% dataset parsing speedup**).
- 🛡️ **Certifications:** Anthropic Model Context Protocol (MCP) Specialized Engineer, AWS Machine Learning - Specialty, Microsoft Certified: Power BI Data Analyst Associate, Tableau Desktop Specialist, HackerRank Advanced SQL, and Databricks Generative AI Fundamentals.
- 💡 **Core Focus:** Autonomous Agent Workflows (LangGraph, Anthropic SDK), Low-Latency Vector Databases (pgvector <120ms), Serverless Inference Optimization (ONNX Lambda <100ms), and Quantitative BI Analytics.

---

## 📦 Open Source on PyPI

<div align="center">

| Package | Description | Badges |
|---|---|---|
| **[`wranglefy`](https://pypi.org/project/wranglefy/)** | Automated tabular data preprocessing, schema validation, and missing data auditing across CSV, JSON, Excel, and Parquet. | [![PyPI Version](https://img.shields.io/pypi/v/wranglefy?style=flat-square&color=blue)](https://pypi.org/project/wranglefy/) [![Downloads](https://img.shields.io/pypi/dm/wranglefy?style=flat-square&color=green)](https://pypi.org/project/wranglefy/) |
| **[`tprdbreader`](https://pypi.org/project/tprdbreader/)** | High-performance custom byte-stream parser delivering an **80% speedup** in dataset loading for research pipelines. | [![PyPI Version](https://img.shields.io/pypi/v/tprdbreader?style=flat-square&color=blue)](https://pypi.org/project/tprdbreader/) [![Downloads](https://img.shields.io/pypi/dm/tprdbreader?style=flat-square&color=green)](https://pypi.org/project/tprdbreader/) |

</div>

---

## 📚 Research Publications

| Venue | Paper Title | Core Contribution |
| :--- | :--- | :--- |
| **IEEE CAI 2026** | *Retrieval-Augmented AI Feedback in STEM Education* | RAG evaluation pipelines, metacognitive prompting, and factual grounding |
| **MDPI AI 2026** | *Mapping the LLM Landscape: Cross-Family Survey* | Cross-family survey across 100+ LLMs, RLHF, DPO, and benchmark evals |
| **SKASE 2025** | *The Behavioural Translation Style Space* | Temporal cognitive dynamics & RL agent behavioral trajectory simulation |
| **TT8 2026 conference** | *Assessing Pause Thresholds in Process Research* | Parametric & non-parametric latency distribution modeling on HCI data |
| **Preprint 2026** | *Large Language Models: Architectures & Alignment* | Attention formulations, state-space models, PEFT/LoRA, and alignment |
| **arXiv 2025** | *From Representation to Enactment: ABC Framework* | Cognitive state transitions and mental representation modeling in NLP |


---


## 🚀 Featured Systems & Projects

### 🧠 [Multi-Tenant Knowledge Platform Backend with Adaptive LangGraph Self-RAG](https://github.com/Devisri-B/Multi-Tenant-SaaS-Platform-with-an-AI-Product-Assistant)
- **Live Platform:** [multi-tenant-saas-platform-with-an-ai.onrender.com](https://multi-tenant-saas-platform-with-an-ai.onrender.com)
- Engineered an adaptive **LangGraph Self-RAG state graph** combining hybrid retrieval (**pgvector** + Postgres FTS via RRF) with local **DeBERTa-v3 NLI cross-encoders** (~20–40ms CPU latency) for zero-cost hallucination verification and dynamic online search fallback.
- Built a production **Model Context Protocol (FastMCP)** server and autonomous ReAct agent over `stdio`, exposing tenant-isolated vector search and Self-RAG tools directly to **Claude Desktop and Cursor IDE** with zero unauthorized cross-boundary leakage.

### 🔬 [Reasoning & Alignment Post-Training Engine with Critic-Free GRPO & DPO](https://github.com/Devisri-B/DeepAlign-RL)
- **Live Demo:** [deepalign-rl.streamlit.app](https://deepalign.streamlit.app)
- Implemented **DeepSeek-style Group Relative Policy Optimization (GRPO)** and **DPO** from scratch in PyTorch, standardizing group-wise advantages to eliminate the critic model and **cut peak training VRAM by ~50%**.
- Engineered a zero-noise **SymPy symbolic reward verifier** and AST sandbox for mathematical equivalence and Chain-of-Thought format compliance, achieving **74.8% GSM8K / 49.3% MATH accuracy** across automated ablation suites.

### ⚡ [Flow Matching DiT Acceleration Engine with Trajectory Distillation & PTQ](https://github.com/Devisri-B/FlowMatch-Compress)
- **Live Demo:** [flowmatch-compress.streamlit.app](https://flowmatch-compress.streamlit.app)
- Implemented **Optimal Transport Flow Matching (OT-CFM)** and **DiT with AdaLN-Zero** from scratch in PyTorch, developing **two-stage distillation (CFG + progressive trajectory consistency)** to eliminate dual-pass evaluations and compress 50 ODE steps into 4 (**22.05× inference speedup**).
- Engineered a modular **Post-Training Quantization (PTQ) suite** supporting IEEE FP8 (E4M3), per-channel INT8, and grouped INT4 with activation calibration, slashing model footprint by **up to 56.3%** with minimal discretization drift.
- Integrated an **AutoencoderKL VAE latent pipeline** ($4 \times 32 \times 32$ latent space) for high-resolution $256 \times 256$ generation, validated against photographic benchmarks and visual ODE trajectory profilers.

### 📈 [Financial Market Risk Forecasting Pipeline with Serverless ONNX Deployment](https://github.com/Devisri-B/Financial-forecasting-pipeline)
- Built a hybrid deep learning ensemble (**Attention-LSTM + Ridge Regression**) achieving **75% directional accuracy**.
- Exported the PyTorch computational graph to **ONNX Runtime** and deployed on serverless **AWS Lambda (<100ms cold-start latency)**.

### 📊 [Olist E-Commerce Intelligence -- Causal Econometrics & Behavioral Segmentation](https://github.com/Devisri-B/Olist-Ecommerce-Intelligence)
- **Live Streamlit App:** [olist-ecommerce-intelligence.streamlit.app](https://olist-ecommerce-intelligence.streamlit.app)
- Executed causal econometric analysis on **96,000+ customer records ($15.4M GMV)** and built RFM behavioral segmentation in PostgreSQL & Streamlit.

### 💳 [Asset Default & Operational Risk Analytics Platform](https://github.com/Devisri-B/Credit-Risk-Scoring-Model)
- **Live Tableau Dashboard:** [Public Tableau Visualization](https://public.tableau.com/app/profile/devi.sri.b/viz/CreditRiskAnalysis_17822342909330/Dashboard4)
- Engineered quantitative data models across **50,000+ records**, evaluating diagnostics via **AUC-ROC, KS statistic, and Gini coefficient**.

---

## 🛠️ Tech Stack & Tooling

<h3 align="center">Languages & Core</h3>
<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/SQL-Advanced_Certified-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++"/>
</div>

<h3 align="center">Generative AI, Agents & Vector Systems</h3>
<div align="center">
  <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/Anthropic_MCP-Certified-D97706?style=for-the-badge&logo=anthropic&logoColor=white" alt="Anthropic MCP"/>
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"/>
  <img src="https://img.shields.io/badge/PostgreSQL_pgvector-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="pgvector"/>
  <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white" alt="FAISS"/>
  <img src="https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pinecone&logoColor=white" alt="Pinecone"/>
</div>

<h3 align="center">Machine Learning, Optimization & Serving</h3>
<div align="center">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/ONNX_Runtime-005CED?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/XGBoost-150458?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/PyArrow-E04E39?style=for-the-badge&logo=apache&logoColor=white" alt="PyArrow"/>
</div>

<h3 align="center">Cloud, Backend & DevOps</h3>
<div align="center">
  <img src="https://img.shields.io/badge/AWS-Lambda_S3_SageMaker-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS"/>
  <img src="https://img.shields.io/badge/GCP-BigQuery_CloudStorage-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="GCP"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/pytest-135_Tests_Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
</div>

<h3 align="center">Business Intelligence & Observability</h3>
<div align="center">
  <img src="https://img.shields.io/badge/Tableau-Certified_Specialist-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Tableau"/>
  <img src="https://img.shields.io/badge/Power_BI-Certified_Associate-F2C811?style=for-the-badge&logo=power-bi&logoColor=black" alt="Power BI"/>
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLflow"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
</div>

<br/>

<div align="center">
  <img src="https://github.com/Devisri-B/Devisri-B/blob/main/library_usage.png?raw=true" alt="Library Usage" width="1000">
</div>

---

## ✍️ Latest Technical Articles & Publications

<!-- BLOG-POST-LIST:START -->
- 📖 [A Practical Guide to T-SQL](https://medium.com/@bandarudevisri.ds/a-practical-guide-to-t-sql-5a2f589c5dde)
- 📖 [Every Microsoft PL-300: Power BI Data Analyst Associate Certification Trap in One Article](https://ai.plainenglish.io/every-microsoft-pl-300-power-bi-data-analyst-associate-certification-trap-in-one-article-plus-the-4ea33451fa68)
- 📖 [Stop Paying for Tokens: Run Private LLMs on Your Laptop with Docker](https://medium.com/@bandarudevisri.ds/stop-paying-for-tokens-run-private-llms-on-your-laptop-with-docker-0b5e7ac55743)
- 📖 [Beyond the Curve: A Holistic Guide to Activation Functions (From Sigmoid to SwiGLU)](https://ai.plainenglish.io/beyond-the-curve-a-holistic-guide-to-activation-functions-from-sigmoid-to-swiglu-3e96faaa7a84)
- 📖 [The Student’s Guide to SAP Certification: How to Get It for Free and Pass with AI](https://medium.com/@bandarudevisri.ds/the-students-guide-to-sap-certification-how-to-get-it-for-free-and-pass-with-ai-d0bbdf78e26a)
<!-- BLOG-POST-LIST:END -->
---

## 📊 GitHub Analytics

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Devisri-B&theme=default" alt="Profile Details" />

<br/>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Devisri-B&theme=default" height="170" alt="Stats" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Devisri-B&theme=default" height="170" alt="Top Languages"/>

<br/>

<a href="https://git.io/streak-stats"><img src="https://streak-stats.demolab.com?user=Devisri-B&hide_border=true&border_radius=5.6&date_format=M%20j%5B%2C%20Y%5D&exclude_days=Sun" alt="GitHub Streak" /></a>

</div>
