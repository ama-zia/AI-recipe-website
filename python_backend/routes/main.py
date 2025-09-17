from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__, template_folder='../templates')


recipe_files = {
    "dark-chocolate-cake": "dark-chocolate-cake.html",
    "vanilla-blueberry-cake": "vanilla-blueberry-cake.html",
    "banana-cake": "banana-cake.html",
    "carrot-cake": "carrot-cake.html",
    "lychee-basque": "lychee-basque.html",
    "japanese-pancakes": "japanese-pancakes.html",
    "apple-cake": "apple-cake.html",
    "orange-olive-oil-cake": "orange-olive-oil-cake.html",
    "date-cake": "date-cake.html",
    "matcha-cookies": "matcha-cookies.html",
    "red-velvet-cookies": "red-velvet-cookies.html",
    "blueberry-macarons": "blueberry-macarons.html",
    "lemon-bars": "lemon-bars.html",
    "pumpkin-chai-cookies": "pumpkin-chai-cookies.html",
    "gingerbread-cookies": "gingerbread-cookies.html",
    "apple-pie": "apple-pie.html",
    "hazelnut-chocolate-cupcakes": "hazelnut-chocolate-cupcakes.html",
    "pecan-pie": "pecan-pie.html",
    "pear-oat-pie": "pear-oat-pie.html",
    "brioche": "brioche.html",
    "cinnamon-rolls": "cinnamon-rolls.html",
    "blueberry-lemon-sourdough": "blueberry-lemon-sourdough.html",
    "olive-oil-focaccia": "olive-oil-focaccia.html",
    "chocolate-croissants": "chocolate-croissants.html",
    "raspberry-ice-cream-sandwich": "raspberry-ice-cream-sandwich.html"
}

@main_bp.route("/")
def home():
    return render_template('index.html')

@main_bp.route("/recipes")
def recipes_page():
    return render_template('recipes.html')

# NEW: Dynamic route for individual recipes
@main_bp.route("/recipes/<recipe_name>")
def recipe_page(recipe_name):
    file_name = recipe_files.get(recipe_name)
    if file_name:
        return render_template(file_name)
    return "Recipe not found", 404


@main_bp.route("/chat")
def chat_page():
    return render_template('chatbot.html')