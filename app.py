from flask import Flask, render_template, request, redirect, url_for, session
import base64
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret123"

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

init_db()

def encrypt_text(text):
    return base64.b64encode(text.encode()).decode()

def decrypt_text(text):
    return base64.b64decode(text.encode()).decode()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = u
            return redirect("/dashboard")
        else:
            return "Invalid Login"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?,?)", (u, p))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")


@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if request.method == "POST":
        text = request.form["text"]
        return redirect(f"/encrypt_process?text={text}")
    return render_template("encrypt.html")


@app.route("/encrypt_process")
def encrypt_process():
    text = request.args.get("text")
    return render_template("encrypt_process.html", text=text)


@app.route("/encrypt_result")
def encrypt_result():
    text = request.args.get("text")
    result = encrypt_text(text)
    return render_template("encrypt_result.html", result=result)


@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if request.method == "POST":
        text = request.form["text"]
        return redirect(f"/decrypt_process?text={text}")
    return render_template("decrypt.html")


@app.route("/decrypt_process")
def decrypt_process():
    text = request.args.get("text")
    return render_template("decrypt_process.html", text=text)


@app.route("/decrypt_result")
def decrypt_result():
    text = request.args.get("text")
    result = decrypt_text(text)
    return render_template("decrypt_result.html", result=result)


if __name__ == "__main__":
    app.run()
