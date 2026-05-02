from flask import Flask, render_template, request, redirect, url_for, session
import base64
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"   # change later

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

init_db()

# ---------- ENCRYPT/DECRYPT ----------
def encrypt_text(text):
    return base64.b64encode(text.encode()).decode()

def decrypt_text(text):
    return base64.b64decode(text.encode()).decode()

# ---------- AUTH ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Credentials"

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# ---------- ENCRYPT ----------
@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        text = request.form["text"]
        return redirect(url_for("encrypt_process", text=text))

    return render_template("encrypt.html")


@app.route("/encrypt/process")
def encrypt_process():
    text = request.args.get("text")
    return render_template("encrypt_process.html", text=text)


@app.route("/encrypt/result")
def encrypt_result():
    text = request.args.get("text")
    result = encrypt_text(text)
    return render_template("encrypt_result.html", result=result)

# ---------- DECRYPT ----------
@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        text = request.form["text"]
        return redirect(url_for("decrypt_process", text=text))

    return render_template("decrypt.html")


@app.route("/decrypt/process")
def decrypt_process():
    text = request.args.get("text")
    return render_template("decrypt_process.html", text=text)


@app.route("/decrypt/result")
def decrypt_result():
    text = request.args.get("text")
    result = decrypt_text(text)
    return render_template("decrypt_result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
