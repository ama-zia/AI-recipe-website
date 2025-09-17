# test_app.py
import pytest
from python_backend.app import create_app, db
from python_backend.models import User, Recipe
from bcrypt import hashpw, gensalt

@pytest.fixture(scope='module')
def new_user():
    """A test user for the database."""
    hashed_password = hashpw('password123'.encode('utf-8'), gensalt())
    user = User(username='testuser', email='test@example.com', password_hash=hashed_password.decode('utf-8'))
    return user

@pytest.fixture(scope='module')
def test_client():
    """Create a test client for the Flask app."""
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"  # in-memory DB for tests
    })
    
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()


def test_home_page(test_client):
    """Test that the home page loads correctly."""
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Sweet Delights Blog" in response.data

def test_signup_page(test_client):
    """Test the signup route with new user."""
    response = test_client.post('/signup', data=dict(
        name='newuser',
        email='newuser@example.com',
        password='password123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"login" in response.data
    user = User.query.filter_by(email='newuser@example.com').first()
    assert user is not None

def test_signup_existing_email(test_client, new_user):
    """Test that a user with an existing email cannot sign up."""
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()
    response = test_client.post('/signup', data=dict(
        username='testuser2',
        email='test@example.com',
        password='anotherpassword'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"A user with this email already exists." in response.data

def test_login_successful(test_client, new_user):
    """Test a successful user login."""
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()
    response = test_client.post('/login', data=dict(
        email='test@example.com',
        password='password123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"Our Recipes" in response.data # Check if they are redirected to the recipes page

def test_login_invalid_password(test_client, new_user):
    """Test login with an incorrect password."""
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()
    response = test_client.post('/login', data=dict(
        email='test@example.com',
        password='wrongpassword'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid email or password." in response.data

def test_logout(test_client, new_user):
    """Test user logout."""
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()
    test_client.post('/login', data=dict(email='test@example.com', password='password123'))
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data # After logout, the user is redirected to the login page

def test_chat_api_successful(test_client, monkeypatch):
    """Test the chat API endpoint with a mock AI response."""
    def mock_semantic_search_hf(user_input):
        return "This is a mocked answer."
    monkeypatch.setattr('python_backend.api.api.semantic_search_hf', mock_semantic_search_hf)

    
    response = test_client.post('/api/chat', json={'message': 'how to bake?'})
    assert response.status_code == 200
    assert response.json['response'] == "This is a mocked answer."

def test_chat_api_no_match(test_client, monkeypatch):
    """Test the chat API with a query that gets no match."""
    def mock_semantic_search_hf(user_input):
        return None
    monkeypatch.setattr('python_backend.semantic_search_hf.semantic_search_hf', mock_semantic_search_hf)

    response = test_client.post('/api/chat', json={'message': 'some random query'})
    assert response.status_code == 200
    assert response.json['response'] == "I'm sorry, I don't have an answer for that. Please try asking about a specific recipe or baking technique."

def test_chat_api_empty_message(test_client):
    response = test_client.post('/api/chat', json={'message': ''})
    assert response.status_code == 200
    assert "Hello, I am your AI baking chatbot" in response.json['response']


def test_chat_api_non_recommendation(monkeypatch, test_client):
    def mock_semantic_search_hf(user_input):
        return "Fallback response."
    monkeypatch.setattr('python_backend.api.api.semantic_search_hf', mock_semantic_search_hf)
    
    response = test_client.post('/api/chat', json={'message': 'How do I bake chocolate cake?'})
    assert response.status_code == 200
    assert response.json['response'] == "Fallback response."

def test_chat_api_recommendation_no_match(monkeypatch, test_client):
    """Test chat API with a recommendation query that returns no recipes."""
    from python_backend.api import api  # import the module where the function is used

    def mock_recommend_recipes(query, top_n=3):
        return []  # simulate no matching recipes

    # Patch the function inside api module
    monkeypatch.setattr(api, 'recommend_recipes', mock_recommend_recipes)

    response = test_client.post(
        '/api/chat',
        json={'message': 'recommend a recipe with unicorn meat'}
    )
    assert response.status_code == 200
    assert "couldn't find any recipes" in response.json['response']

# ------------------ app.py coverage ------------------
def test_load_user_function(test_client):
    """Test the user_loader function in app.py with a real user in session."""
    with test_client.application.app_context():
        user = User(username="loaduser", email="load@example.com", password_hash="hashed")
        db.session.add(user)
        db.session.commit()

        from python_backend.app import create_app
        app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        with app.app_context():
            db.session.add(User(username="temp", email="temp@example.com", password_hash="hash"))
            db.session.commit()
            loaded = User.query.filter_by(id=1).first()
            assert loaded.username == "temp"

# ------------------ models.py coverage ------------------
def test_user_repr(test_client):
    """Test the __repr__ method of User with a bound user."""
    with test_client.application.app_context():
        user = User(username="repruser", email="repr@example.com", password_hash="hash")
        db.session.add(user)
        db.session.commit()
        assert "repruser" in repr(user)
        assert "repr@example.com" in repr(user)

def test_recipe_repr(test_client, new_user):
    """Test the __repr__ method of Recipe."""
    with test_client.application.app_context():
        db.session.add(new_user)
        db.session.commit()
        recipe = Recipe(name="Chocolate Cake", link="/choc", full_text="Delicious cake", user_id=new_user.id)
        db.session.add(recipe)
        db.session.commit()
        assert "Chocolate Cake" in repr(recipe)

# ------------------ recipe_recommender.py coverage ------------------
def test_recommend_recipes_success():
    """Test that recommender returns recipes for a valid query."""
    from python_backend.recipe_recommender import recommend_recipes
    results = recommend_recipes("flour sugar")
    assert isinstance(results, list)
    assert len(results) > 0
    assert "name" in results[0]

def test_recommend_recipes_no_match():
    """Test recommender returns empty list when no recipe matches."""
    from python_backend.recipe_recommender import recommend_recipes
    results = recommend_recipes("unicorn meat")
    assert results == []

def test_recommend_recipes_empty_query():
    """Test recommender with empty query."""
    from python_backend.recipe_recommender import recommend_recipes
    results = recommend_recipes("")
    assert isinstance(results, list)

# ------------------ semantic_search_hf.py coverage ------------------
def test_semantic_search_returns_answer():
    """Test semantic search returns a valid answer for a known question."""
    from python_backend.semantic_search_hf import semantic_search_hf, baking_data
    question = baking_data[0]["question"]
    answer = semantic_search_hf(question)
    assert answer == baking_data[0]["answer"]

def test_semantic_search_low_similarity(monkeypatch):
    """Force semantic search to return None for low similarity."""
    from python_backend import semantic_search_hf
    def mock_encode(*args, **kwargs):
        return semantic_search_hf.vectors[0:1] * 0.0  # simulate bad match
    monkeypatch.setattr(semantic_search_hf.model, "encode", mock_encode)

    result = semantic_search_hf.semantic_search_hf("random gibberish")
    assert result is None
