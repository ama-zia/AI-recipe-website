import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔹 Option 1: Make path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # directory of this script
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "recipe_data.json")  # navigate to ../data/recipe_data.json

# 1️⃣ Load your recipe data
with open(DATA_FILE, "r") as f:
    recipe_data = json.load(f)

# 2️⃣ Prepare the data for the model
corpus = []
for recipe in recipe_data:
    combined_text = " ".join(recipe.get("keywords", []))
    combined_text += " " + recipe.get("season", "")
    combined_text += " " + " ".join(recipe.get("pantry", []))
    corpus.append(combined_text)

# 3️⃣ Create a TfidfVectorizer
vectorizer = TfidfVectorizer()
recipe_vectors = vectorizer.fit_transform(corpus)

# 4️⃣ Recommendation function
def recommend_recipes(user_query, top_n=3):
    """
    Recommends recipes based on a user's query using cosine similarity.
    """
    user_query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(user_query_vector, recipe_vectors).flatten()
    top_indices = np.argsort(similarities)[-top_n:][::-1]

    recommendations = []
    for i in top_indices:
        if similarities[i] > 0.1:
            recommendations.append(recipe_data[i])

    return recommendations
