import requests
import csv
import xml.etree.ElementTree as ET

queries = ["machine learning", "natural language processing", "deep learning", "computer vision", "recommendation systems"]
papers = []

for query in queries:
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=100"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title')
        abstract = entry.find('{http://www.w3.org/2005/Atom}summary')
        link = entry.find('{http://www.w3.org/2005/Atom}id')
        if title is not None and abstract is not None and link is not None:
            papers.append([title.text.strip(), abstract.text.strip(), link.text.strip()])

with open('dataset/papers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'abstract', 'link'])
    writer.writerows(papers)

print(f"Total papers saved: {len(papers)}")