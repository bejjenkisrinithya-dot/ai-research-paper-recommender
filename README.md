A web-based intelligent research paper recommendation system that uses Natural Language Processing (NLP) to suggest the most relevant academic papers based on a user's search query. Built using TF-IDF vectorization and Cosine Similarity on a dataset of 500 real arXiv research papers.

Developed by Bejjenki Srinithya, B.Tech CSE, Anurag University, Hyderabad
bejjenkisrinithya@gmail.com 

Table of Contents

Overview
Features
How It Works
Dataset
Tech Stack
Project Structure
How to Run
Example Output
Future Improvements


 Overview
Finding relevant research papers is time-consuming for students and researchers. This project solves that by building an AI-powered recommendation engine that:

Takes a user's topic/query as input
Compares it against 500 real arXiv paper abstracts using NLP
Returns the most semantically similar papers ranked by relevance score

This project demonstrates how content-based filtering and NLP techniques can be applied to build intelligent academic search tools.

 Features

 Search research papers by any topic or keyword
 AI-based recommendation using TF-IDF + Cosine Similarity
 Displays paper titles with direct arXiv links
 500 real arXiv papers across CS, ML, NLP, CV, and AI domains
 Clean and responsive web interface
 Fast Flask REST API backend


  How It Works
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

All 500 paper abstracts are vectorized using TF-IDF (Term Frequency-Inverse Document Frequency)
The user query is transformed into the same vector space
Cosine Similarity is computed between the query vector and all paper vectors
Papers are ranked by similarity score and top results are returned


 Dataset
PropertyDetailsSourcearXiv Open Access APITotal Papers500DomainsMachine Learning, NLP, Deep Learning, Computer Vision, Recommendation SystemsColumnstitle, abstract, linkFormatCSV
Dataset was collected using the arXiv API and covers major CS/AI research areas published on arXiv.

🛠️ Tech Stack
LayerTechnologyLanguagePython 3.10BackendFlask, Flask-CORSNLP / MLScikit-learn, PandasFrontendHTML, CSS, JavaScriptDatasetarXiv API (500 papers)Version ControlGit, GitHub

 Project Structure
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

 How to Run
1. Clone the repository
bashgit clone https://github.com/bejjenkisrinithya-dot/ai-research-paper-recommender.git
cd ai-research-paper-recommender
2. Install dependencies
bashpip install flask pandas scikit-learn flask-cors requests
3. Run the backend
bashcd backend
python app.py
Backend starts at: http://127.0.0.1:5000
4. Open the frontend
Open frontend/index.html in your browser or run:
bashpython -m http.server 5500
Then visit: http://localhost:5500

 Example Output
Input Query: natural language processing
Recommended Papers:
#TitleLink1A Survey on Natural Language Processing TechniquesarXiv2BERT: Pre-training of Deep Bidirectional TransformersarXiv3Attention Is All You NeedarXiv4Text Classification using Neural NetworksarXiv5Word Embeddings for NLP TasksarXiv

 Future Improvements

 Add paper summaries using generative AI (GPT/Gemini)
 Implement user feedback loop to improve recommendations
 Add filters by year, author, and citation count
 Deploy on cloud (Render / Vercel / AWS)
 Improve UI with React.js
 Add semantic search using Sentence Transformers (SBERT)


  Author
Bejjenki Srinithya
B.Tech Computer Science & Engineering | Anurag University, Hyderabad

📧 bejjenkisrinithya@gmail.com
🔗 LinkedIn
💻 GitHub
