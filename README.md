# AI Research Paper Recommender

##  Project Overview
The **AI Research Paper Recommender** is a web application that recommends relevant research papers based on a user's search query.
It uses Natural Language Processing techniques to compare the user query with paper abstracts and returns the most relevant results.
This project demonstrates how **AI-based recommendation systems** can help researchers quickly find useful academic papers.
##  Features
* Search research papers by topic
* AI-based recommendation using NLP
* Displays paper titles with links
* Clean and simple web interface
* Backend API built using Flask
##  Technologies Used
* Python
* Flask
* Scikit-learn
* Pandas
* HTML
* CSS
* JavaScript
##  Project Structure
ai-research-paper-recommender
│
├── backend
│   ├── app.py
│   └── recommender.py
│
├── dataset
│   └── papers.csv
│
├── frontend
│   └── index.html
│
└── README.md
## How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/bejjenkisrinithya-dot/ai-research-paper-recommender.git
### 2️⃣ Navigate to the project folder

cd ai-research-paper-recommender
### 3️⃣ Install required libraries
pip install flask pandas scikit-learn flask-cors
### 4️⃣ Run the backend server
cd backend
python app.py
The backend server will start at:
http://127.0.0.1:5000
### 5️⃣ Run the frontend
Open the `frontend/index.html` file in a browser or run:
python -m http.server 5500
Then open:
http://localhost:5500

##  Example
User Input:
machine learning
Recommended Papers:

* Deep Learning for Healthcare
* AI in Medical Imaging
* Natural Language Processing Survey

## Future Improvements

* Integrate real-time research papers from arXiv
* Add paper summaries using AI
* Improve UI with modern frameworks
* Deploy the project online

##  Author
Srinithya
Computer Science Student interested in AI, Machine Learning, and Software Development.

---
