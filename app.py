from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

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
    return login_user(u, p)


@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.form['file']
    return encrypt_file(file)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.form['file']
    return decrypt_file(file)


@app.route('/hash', methods=['POST'])
def hash_file():
    file = request.form['file']
    return check_integrity(file)


@app.route('/block', methods=['POST'])
def block():
    ip = request.form['ip']
    return block_ip(ip)


@app.route('/allow', methods=['POST'])
def allow():
    ip = request.form['ip']
    return allow_ip(ip)


@app.route('/check', methods=['POST'])
def check():
    ip = request.form['ip']
    return check_ip(ip)


if __name__ == "__main__":
    app.run(debug=True)
