from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (for demo)
users = {}

# ---------------- HOME (REGISTER PAGE) ----------------
@app.route('/')
def home():
    return render_template("register.html")


# ---------------- REGISTER ----------------
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    users[username] = password
    return redirect(url_for('login_page'))


# ---------------- LOGIN PAGE ----------------
@app.route('/login')
def login_page():
    return render_template("login.html")


# ---------------- LOGIN FUNCTION ----------------
@app.route('/login_user', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']

    if users.get(username) == password:
        return redirect(url_for('dashboard'))
    else:
        return "❌ Invalid Login"


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


# ---------------- ENCRYPT ----------------
@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['text']
    result = text[::-1]   # simple demo encryption
    return f"Encrypted: {result}"


# ---------------- DECRYPT ----------------
@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form['text']
    result = text[::-1]
    return f"Decrypted: {result}"


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
