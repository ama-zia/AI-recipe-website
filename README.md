# Stone & Sugar – Full-Stack Baking Web Application

## Project Overview

"Stone & Sugar" is a sophisticated full-stack web application designed for baking enthusiasts. The platform allows users to browse recipes, ask baking-related questions, and receive personalized recipe recommendations. The project demonstrates expertise in **web development, machine learning, AI, software engineering, and cybersecurity**, offering a seamless and interactive experience.

---

## Purpose and Usefulness

* **Instant Baking Assistance**: Users can ask questions about baking and get accurate answers from an AI-powered Q\&A system.
* **Personalized Recipe Recommendations**: Users receive suggestions based on ingredients, preferences, and available pantry items.
* **Educational & Interactive**: Encourages users to explore new recipes and techniques.
* **Security-Oriented Design**: Includes robust user authentication and secure password management.

This platform combines practical utility with cutting-edge AI technology, enhancing user experience and engagement.

---

## Backend – Flask Application

The backend is built with **Python and Flask**, serving as the project's brain.

### Key Responsibilities

* Handling user data and authentication.
* Routing requests from frontend to appropriate services.
* Serving the AI chatbot and recommendation system.

### Components

1. **User Authentication System**

   * **Flask-Login**: Manages user sessions and protects restricted pages.
   * **Bcrypt**: Securely hashes passwords to prevent storage of plain-text passwords.

2. **Database & Data Models**

   * **Flask-SQLAlchemy** ORM for database management.
   * **User Model**: Stores username, email, and password hash.
   * **Recipe Model**: Stores recipe information and author details.

3. **AI Baking Assistant**

   * **Dual-Purpose AI System**: Routes user queries to one of two specialized models.

   #### a. Q\&A Engine (`semantic_search_hf.py`)

   * Uses **Hugging Face Sentence-Transformers** to create sentence embeddings.
   * Uses **FAISS** for fast vector similarity search.
   * Responds to user questions with relevant answers from `baking_data.json`.

   #### b. Recipe Recommendation Engine (`recipe_recommender.py`)

   * Uses **TF-IDF vectorization** to encode recipe data from `recipe_data.json`.
   * Computes **cosine similarity** to match user queries with recipes.
   * Suggests recipes based on keywords like ingredients or preferences.

### How AI and ML are Used

* **Natural Language Processing**: Understands user questions semantically, not just by keywords.
* **Recommendation System**: Uses vectorization and similarity calculations to recommend recipes.
* Demonstrates integration of AI into web applications, bridging frontend interactions with intelligent backend processing.

---

## Frontend – User Interface

The frontend is composed of HTML, CSS, and JavaScript.

* **HTML**: Provides page structure (e.g., `index.html`, `signup.html`, `chatbot.html`).
* **CSS**: Styles the website for a professional and appealing look (`style.css`, `styles.css`).
* **JavaScript**: Handles dynamic interaction, sending user input to `/chat` endpoint and updating chat interface in real-time.

---

## Project File Structure

* `app.py` – Main Flask application and routing.
* `models.py` – Database schema for users and recipes.
* `semantic_search_hf.py` – Q\&A chatbot engine.
* `recipe_recommender.py` – Recipe recommendation engine.
* `baking_data.json` – Knowledge base for Q\&A chatbot.
* `recipe_data.json` – Recipe database for recommendation engine.
* `requirements.txt` – Python dependencies.
* HTML/CSS/JS files – Frontend user interface.

---

## Languages and Tools Used

* **Python**: Backend logic, AI/ML models.
* **HTML/CSS/JavaScript**: Frontend structure, styling, and interactivity.
* **Flask**: Web framework.
* **Flask-SQLAlchemy**: Database ORM.
* **Flask-Login**: User session management.
* **Bcrypt**: Password hashing for security.
* **Scikit-learn**: TF-IDF vectorization and cosine similarity.
* **Hugging Face Sentence-Transformers**: Sentence embeddings for semantic search.
* **FAISS**: Fast similarity search.
* **NumPy**: Numerical operations for AI models.

---

## Security and Software Engineering Principles

* Secure password storage using Bcrypt.
* Protected routes with Flask-Login.
* Modular and well-structured code for maintainability.
* Separation of concerns: Backend, frontend, and AI components clearly defined.
* Emphasis on robust, scalable design demonstrating professional software engineering practices.

---

## Running the Project

1. Navigate to the project directory:

   ```bash
   cd AI-recipe-website
   ```
2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Start the backend server:

   ```bash
   python -m python_backend.app
   ```
4. Open your browser and access the website at `http://localhost:5000`.

---

## Test Coverage

The backend and AI systems are thoroughly tested with **92% coverage**, ensuring reliability and robustness.

---

## Summary

"Stone & Sugar" is a cutting-edge, AI-powered baking platform that combines full-stack web development, machine learning, software engineering best practices, and cybersecurity principles. It provides an interactive, educational, and secure environment for baking enthusiasts, making it both practical and technically impressive.
