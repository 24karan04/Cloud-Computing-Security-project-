from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import base64

app = Flask(__name__)
app.secret_key = "secret123"

DB = "users.db"

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- ENCRYPT FUNCTION ----------
def encrypt_text(text):
    return base64.b64encode(text.encode()).decode()

# ---------- DECRYPT FUNCTION ----------
def decrypt_text(text):
    return base64.b64decode(text.encode()).decode()

# ---------- HOME ----------
@app.route("/")
def home():
    return redirect("/register")

# ---------- REGISTER ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?,?)", (username, password))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Login"

    return render_template("login.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# ---------- FORGOT PASSWORD ----------
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    message = ""

    if request.method == "POST":
        username = request.form["username"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        result = c.fetchone()
        conn.close()

        if result:
            message = f"Your password is: {result[0]}"
        else:
            message = "User not found"

    return render_template("forgot_password.html", message=message)

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

# ---------- ENCRYPT ----------
@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        text = request.form["text"]
        return redirect(url_for("encrypt_process", text=text))

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

# ---------- DECRYPT ----------
@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        text = request.form["text"]
        return redirect(url_for("decrypt_process", text=text))

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

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
