# 🍰 AI-Powered Baking Website

Welcome to my AI-powered baking assistant website! This is a full-stack project built using **Sinatra** for user authentication, **HTML/CSS** for recipe pages, and a smart **AI baking chatbot** built with **Python, JavaScript, and Hugging Face models**.

---

## ✨ Features

- 👤 **User Authentication**: Signup and login using Sinatra.
- 📄 **Static Recipe Pages**: Beautifully designed HTML & CSS recipe pages.
- 🤖 **AI Baking Assistant Chatbot**:
  - Rule-based fallback logic (in JavaScript).
  - Hugging Face integration for baking-related questions using Python.
- 🎨 Mobile-responsive and accessible design.

---

## 🗂️ Project Structure

```
my-baking-website/
│
├── app.rb                  # Main Sinatra app
├── config.ru               # Rack configuration
├── Gemfile                 # Ruby dependencies
├── Gemfile.lock
│
├── controllers/            # Sinatra route handlers (signup/login)
├── db/                     # SQLite or ORM data (if applicable)
├── models/                 # User model
├── views/                  # ERB pages (signup/login forms)
│
├── public/                 # Static HTML/CSS/JS for recipes & chatbot UI
│   ├── recipes/            # Individual recipe HTML pages
│   └── chatbot.html        # Baking assistant page
│
├── python-backend/         # Python Flask server using Hugging Face API
│   ├── app.py              # Flask API that handles AI requests
│   └── requirements.txt    # Python dependencies
```

---

## 🔧 Installation & Setup

### Prerequisites

- Ruby & Bundler
- Python 3
- Node.js (optional, for JS tweaks)
- Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/ama-zia/my-portfolio-project.git
cd my-baking-website
```

---

### 2. Install Ruby Gems

```bash
bundle install
```

---

### 3. Run the Sinatra Server

```bash
ruby app.rb
```

---

### 4. Set Up Python AI Backend

```bash
cd python-backend
python -m venv venv
source venv/bin/activate  # (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
python app.py
```

---

### 5. Access the Website

- Open your browser and visit: `http://localhost:4567`
- Navigate to the chatbot page from the homepage or directly open `chatbot.html`

---

## 🤖 How the AI Chatbot Works

- The `chatbot.html` page sends user input to a Python Flask server using `fetch()`.
- A **JavaScript rule-based system** first tries to answer basic baking questions (like ingredient substitutions or conversions).
- If no rule-based response is found, the input is forwarded to the **Python Flask backend**, which uses **Hugging Face transformers** to generate an intelligent AI reply.

---

## 📚 Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Ruby (Sinatra), Python (Flask)  
- **AI**: Hugging Face Transformers  
- **Database**: SQLite3 (via ActiveRecord or similar)  
- **Version Control**: Git & GitHub
