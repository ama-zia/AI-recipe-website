from flask import Blueprint, request, jsonify
from python_backend.semantic_search_hf import semantic_search_hf
from python_backend.recipe_recommender import recommend_recipes  # 🆕 Import the new function

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

@api_bp.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get('message', '').lower()  # Convert to lowercase for easier keyword matching
    
    # 🆕 Check if the user is asking for a recipe recommendation
    if any(keyword in user_message for keyword in ['what can i make with', 'recommend a recipe', 'show me recipes']):
        # If keywords are found, use the new recommendation engine
        recommendations = recommend_recipes(user_message, top_n=3)
        if recommendations:
            # Format the list of recommended recipes into a single string for the chatbot
            response_text = "Here are some recipes you might like:\n"
            for recipe in recommendations:
                response_text += f"- {recipe['name']}\n"
            return jsonify({"response": response_text})
        else:
            return jsonify({"response": "I'm sorry, I couldn't find any recipes that match your request. Please try a different query."})

    # If it's not a recommendation request, fall back to the old Q&A logic
    response = semantic_search_hf(user_message)

    if response is None:
        return jsonify({"response": "I'm sorry, I don't have an answer for that. Please try asking about a specific recipe or baking technique."})
    
    return jsonify({"response": response})

