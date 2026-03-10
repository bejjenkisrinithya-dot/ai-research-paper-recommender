# 🔍 AI Research Paper Recommender

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey?logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-NLP-orange?logo=scikit-learn)
![Dataset](https://img.shields.io/badge/Dataset-500%20arXiv%20Papers-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A web-based intelligent research paper recommendation system that uses **Natural Language Processing (NLP)** to suggest the most relevant academic papers based on a user's search query. Built using TF-IDF vectorization and Cosine Similarity on a dataset of **500 real arXiv research papers**.

> Developed by **Bejjenki Srinithya**, B.Tech CSE, Anurag University, Hyderabad
> 📧 bejjenkisrinithya@gmail.com | [LinkedIn](https://linkedin.com) | [GitHub](https://github.com/bejjenkisrinithya-dot)

---

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Example Output](#example-output)
- [Future Improvements](#future-improvements)

---

## 📖 Overview

Finding relevant research papers is time-consuming for students and researchers. This project solves that by building an **AI-powered recommendation engine** that:
- Takes a user's topic/query as input
- Compares it against 500 real arXiv paper abstracts using NLP
- Returns the most semantically similar papers ranked by relevance score

This project demonstrates how content-based filtering and NLP techniques can be applied to build intelligent academic search tools.

---

## ✨ Features

- 🔎 Search research papers by any topic or keyword
- 🤖 AI-based recommendation using TF-IDF + Cosine Similarity
- 📄 Displays paper titles with direct arXiv links
- 📊 500 real arXiv papers across CS, ML, NLP, CV, and AI domains
- 🌐 Clean and responsive web interface
- ⚡ Fast Flask REST API backend

---

## ⚙️ How It Works

```
User Query
    │
    ▼
TF-IDF Vectorization
    │
    ▼
Cosine Similarity Calculation
(Query vs all 500 paper abstracts)
    │
    ▼
Top-N Most Relevant Papers Returned
```

1. All 500 paper abstracts are vectorized using **TF-IDF** (Term Frequency-Inverse Document Frequency)
2. The user query is transformed into the same vector space
3. **Cosine Similarity** is computed between the query vector and all paper vectors
4. Papers are ranked by similarity score and top results are returned

---

## 📂 Dataset

| Property | Details |
|---|---|
| Source | arXiv Open Access API |
| Total Papers | 500 |
| Domains | Machine Learning, NLP, Deep Learning, Computer Vision, Recommendation Systems |
| Columns | `title`, `abstract`, `link` |
| Format | CSV |

Dataset was collected using the arXiv API and covers major CS/AI research areas published on arXiv.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| Backend | Flask, Flask-CORS |
| NLP / ML | Scikit-learn, Pandas |
| Frontend | HTML, CSS, JavaScript |
| Dataset | arXiv API (500 papers) |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```
ai-research-paper-recommender/
│
├── backend/
│   ├── app.py              # Flask API endpoints
│   └── recommender.py      # TF-IDF + Cosine Similarity logic
│
├── dataset/
│   └── papers.csv          # 500 arXiv research papers
│
├── frontend/
│   └── index.html          # Web interface
│
├── fetch_papers.py         # Script to fetch papers from arXiv API
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/bejjenkisrinithya-dot/ai-research-paper-recommender.git
cd ai-research-paper-recommender
```

### 2. Install dependencies
```bash
pip install flask pandas scikit-learn flask-cors requests
```

### 3. Run the backend
```bash
cd backend
python app.py
```
Backend starts at: `http://127.0.0.1:5000`

### 4. Open the frontend
Open `frontend/index.html` in your browser or run:
```bash
python -m http.server 5500
```
Then visit: `http://localhost:5500`

---

## 💡 Example Output

**Input Query:** `natural language processing`

**Recommended Papers:**
| # | Title | Link |
|---|---|---|
| 1 | A Survey on Natural Language Processing Techniques | arXiv |
| 2 | BERT: Pre-training of Deep Bidirectional Transformers | arXiv |
| 3 | Attention Is All You Need | arXiv |
| 4 | Text Classification using Neural Networks | arXiv |
| 5 | Word Embeddings for NLP Tasks | arXiv |

---

## 🔮 Future Improvements

- [ ] Add paper summaries using generative AI (GPT/Gemini)
- [ ] Implement user feedback loop to improve recommendations
- [ ] Add filters by year, author, and citation count
- [ ] Deploy on cloud (Render / Vercel / AWS)
- [ ] Improve UI with React.js
- [ ] Add semantic search using Sentence Transformers (SBERT)

---

## 👩‍💻 Author

**Bejjenki Srinithya**
B.Tech Computer Science & Engineering | Anurag University, Hyderabad
- 📧 bejjenkisrinithya@gmail.com
- 🔗 [LinkedIn](https://linkedin.com)
- 💻 [GitHub](https://github.com/bejjenkisrinithya-dot)
