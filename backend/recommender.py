import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load dataset
data = pd.read_csv("../dataset/papers.csv")

# create tf-idf model
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(data["abstract"])


def recommend_papers(query):

    query_vec = tfidf.transform([query])

    similarity = cosine_similarity(query_vec, tfidf_matrix)

    scores = list(enumerate(similarity[0]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top_results = scores[0:4]

    results = []

    for i in top_results:

        paper = {
            "title": data.iloc[i[0]]["title"],
            "link": data.iloc[i[0]]["link"]
        }

        results.append(paper)

    return results