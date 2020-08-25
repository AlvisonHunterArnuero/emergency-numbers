from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static', template_folder="templates")
app.run(debug=True)

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


