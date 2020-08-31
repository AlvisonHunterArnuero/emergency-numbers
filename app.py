from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, static_url_path='/static', template_folder="templates")
DEVELOPMENT_ENV  = True

app_data = {
    "name":         "EMERGENCY PHONE NUMBERS",
    "description":  "A basic Flask app using bootstrap for layout",
    "author":       "Alvison Hunter Arnuero",
    "html_title":   "EMERGENCY PHONE NUMBERS",
    "project_name": "EMERGENCY PHONE NUMBERS",
    "keywords":     "flask, webapp, bootstrap, basic, python, static web"
}
# I will use this globally to use in any of the templates
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Defining the regular routes on this section
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("home.html", page="home")

@app.route("/login")
def login():
    return render_template("login.html", page="login")

@app.route("/about")
def about():
    return render_template("about.html", page="about")

@app.route("/github")
def github():
    return render_template("github.html", page="github")

@app.route("/contact")
def contact():
    return render_template("contact.html", page="contact")

# Let's try to capture the 404 error and handle it
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page="404"),404

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)
