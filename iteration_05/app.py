from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    contact_info = {
         "email": "amarakaeva26@nmhschool.org",
         "github": "github.com/angmar-a",
         "phone": 1234567890
    }
    return render_template("contact.html",contact=contact_info)

@app.route("/about")
def about():
    return render_template("about.html", name ="Angelina", is_student=True)

app.run(debug=True)