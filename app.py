from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user storage
users = {}

# ---------------- HOME ----------------
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


# ---------------- LOGIN ----------------
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
@app.route('/encrypt', methods=['GET','POST'])
def encrypt():
    if request.method == 'POST':
        text = request.form['text']
        result = text[::-1]
        return render_template("encrypt.html", result=result)
    return render_template("encrypt.html")


# ---------------- DECRYPT ----------------
@app.route('/decrypt', methods=['GET','POST'])
def decrypt():
    if request.method == 'POST':
        text = request.form['text']
        result = text[::-1]
        return render_template("decrypt.html", result=result)
    return render_template("decrypt.html")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
