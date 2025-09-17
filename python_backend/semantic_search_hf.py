# semantic_search_hf.py
import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# 1️⃣ Load baking Q&A dataset
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
with open(os.path.join(BASE_DIR, 'baking_data.json'), 'r') as f:
    baking_data = json.load(f)

# 2️⃣ Load HuggingFace embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3️⃣ Precompute embeddings for all questions
questions = [qa["question"] for qa in baking_data]
vectors = model.encode(questions, convert_to_numpy=True, normalize_embeddings=True)

# 4️⃣ Build FAISS index
dim = vectors.shape[1]
index = faiss.IndexFlatIP(dim)
index.add(vectors)

# 5️⃣ Function to find most similar question
def semantic_search_hf(user_input, top_k=1):
    user_vector = model.encode([user_input], convert_to_numpy=True, normalize_embeddings=True)
    distances, indices = index.search(user_vector, top_k)
    best_idx = indices[0][0]

    if distances[0][0] < 0.5:
        return None

    return baking_data[best_idx]["answer"]
