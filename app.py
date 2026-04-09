from flask import Flask, render_template, request, redirect, url_for, session
from main import *
import os

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    u = request.form['u']
    p = request.form['p']
    return register_user(u, p)


@app.route('/login', methods=['POST'])
def login():
    u = request.form['u']
    p = request.form['p']

    if login_user(u, p):
        session['user'] = u
        return redirect("/dashboard")

    return "Invalid Login"


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template("dashboard.html", user=session['user'])


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return encrypt_file(path)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return decrypt_file(path)


if __name__ == "__main__":
    app.run(debug=True)
