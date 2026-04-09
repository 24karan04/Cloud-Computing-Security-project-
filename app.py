from flask import Flask, request

from authentication import register_user, login_user
from encryption import encrypt_file, decrypt_file
from firewall import block_ip, allow_ip, check_ip
from integrity import file_hash
from logger import log_event

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return '''
    <h1>Advanced Cloud Security System</h1>

    <h3>1. Register</h3>
    <form action="/register" method="post">
        Username: <input name="u"><br>
        Password: <input name="p"><br>
        <input type="submit">
    </form>

    <h3>2. Login</h3>
    <form action="/login" method="post">
        Username: <input name="u"><br>
        Password: <input name="p"><br>
        <input type="submit">
    </form>

    <h3>3. Encrypt File</h3>
    <form action="/encrypt" method="post">
        File name: <input name="file"><br>
        <input type="submit">
    </form>

    <h3>4. Decrypt File</h3>
    <form action="/decrypt" method="post">
        File name: <input name="file"><br>
        <input type="submit">
    </form>

    <h3>5. File Integrity</h3>
    <form action="/hash" method="post">
        File name: <input name="file"><br>
        <input type="submit">
    </form>

    <h3>6. Block IP</h3>
    <form action="/block" method="post">
        IP: <input name="ip"><br>
        <input type="submit">
    </form>

    <h3>7. Allow IP</h3>
    <form action="/allow" method="post">
        IP: <input name="ip"><br>
        <input type="submit">
    </form>

    <h3>8. Check IP</h3>
    <form action="/check" method="post">
        IP: <input name="ip"><br>
        <input type="submit">
    </form>
    '''

# Register
@app.route('/register', methods=['POST'])
def register():
    u = request.form['u']
    p = request.form['p']
    result = register_user(u, p)
    log_event("User registered")
    return f"<h2>{result}</h2><a href='/'>Back</a>"

# Login
@app.route('/login', methods=['POST'])
def login():
    u = request.form['u']
    p = request.form['p']
    result = login_user(u, p)
    log_event("User login attempt")
    return f"<h2>{result}</h2><a href='/'>Back</a>"

# Encrypt
@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.form['file']
    result = encrypt_file(file)
    log_event("File encrypted")
    return f"<h2>{result}</h2><a href='/'>Back</a>"

# Decrypt
@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.form['file']
    result = decrypt_file(file)
    log_event("File decrypted")
    return f"<h2>{result}</h2><a href='/'>Back</a>"

# Hash
@app.route('/hash', methods=['POST'])
def hash_file():
    file = request.form['file']
    result = file_hash(file)
    return f"<h2>SHA256: {result}</h2><a href='/'>Back</a>"

# Block IP
@app.route('/block', methods=['POST'])
def block():
    ip = request.form['ip']
    return f"<h2>{block_ip(ip)}</h2><a href='/'>Back</a>"

# Allow IP
@app.route('/allow', methods=['POST'])
def allow():
    ip = request.form['ip']
    return f"<h2>{allow_ip(ip)}</h2><a href='/'>Back</a>"

# Check IP
@app.route('/check', methods=['POST'])
def check():
    ip = request.form['ip']
    return f"<h2>{check_ip(ip)}</h2><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(port=5000)