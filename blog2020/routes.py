from blog2020 import app
from flask import render_template

# Home Route
@app.route("/")
def home():
    languages = {
        "primary": "python",
        "secondary": "JavaScript",
        "legendary": "C++",
        "future":"Go",
        "near_future": "Dart"
    }

    for order,lang in languages.items():
        if lang == 'Python':
            print(lang)
    return render_template('home.html',languages = languages)

# Create User Route
@app.route('/create')
def create_user():
    return render_template('create_user.html')