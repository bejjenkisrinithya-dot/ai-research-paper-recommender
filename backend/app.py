from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import recommend_papers

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Research Paper Recommender API running"


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    query = data["query"]

    results = recommend_papers(query)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)