from flask import Flask, render_template, request, redirect, session, flash, send_file
import sqlite3
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = "secret123"

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

init_db()

# ---------- ENCRYPTION ----------
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

with open("key.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

# ---------- ROUTES ----------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    u = request.form['u']
    p = request.form['p']

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (u, p))
    conn.commit()
    conn.close()

    flash("✅ Registered Successfully")
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    u = request.form['u']
    p = request.form['p']

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    user = c.fetchone()
    conn.close()

    if user:
        session['user'] = u
        return redirect('/dashboard')
    else:
        flash("❌ Invalid Login")
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template("dashboard.html", user=session['user'])

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['file']
    data = file.read()

    encrypted = cipher.encrypt(data)

    with open("encrypted.bin", "wb") as f:
        f.write(encrypted)

    flash("🔐 File Encrypted (Download below)")
    return redirect('/dashboard')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['file']
    data = file.read()

    decrypted = cipher.decrypt(data)

    with open("decrypted.txt", "wb") as f:
        f.write(decrypted)

    flash("🔓 File Decrypted (Download below)")
    return redirect('/dashboard')

@app.route('/download_encrypted')
def download_encrypted():
    return send_file("encrypted.bin", as_attachment=True)

@app.route('/download_decrypted')
def download_decrypted():
    return send_file("decrypted.txt", as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run()
