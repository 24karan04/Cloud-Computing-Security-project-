from flask import Flask, render_template, request, redirect, session
import sqlite3, base64

app = Flask(__name__)
app.secret_key = "secret123"

DB = "users.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    conn.commit()
    conn.close()

init_db()

def encrypt_text(text):
    return base64.b64encode(text.encode()).decode()

def decrypt_text(text):
    return base64.b64decode(text.encode()).decode()

# ---------- HOME ----------
@app.route("/")
def home():
    return redirect("/register")

# ---------- REGISTER ----------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?,?)",(u,p))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
        user = c.fetchone()
        conn.close()

        if user:
            session["user"] = u
            return redirect("/dashboard")
        else:
            return "Invalid Login"

    return render_template("login.html")

# ---------- FORGOT ----------
@app.route("/forgot_password", methods=["GET","POST"])
def forgot():
    msg = ""
    if request.method == "POST":
        u = request.form["username"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username=?",(u,))
        res = c.fetchone()
        conn.close()

        msg = f"Password: {res[0]}" if res else "User not found"

    return render_template("forgot_password.html", message=msg)

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

# ---------- ENCRYPT ----------
@app.route("/encrypt", methods=["GET","POST"])
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
    return render_template("encrypt_result.html",
                           result=encrypt_text(text))

# ---------- DECRYPT ----------
@app.route("/decrypt", methods=["GET","POST"])
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
    return render_template("decrypt_result.html",
                           result=decrypt_text(text))

if __name__ == "__main__":
    app.run()
