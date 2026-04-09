from flask import Flask, request
from main import *

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Cloud Security System</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
            }
            h1 { color: #38bdf8; }
            .box {
                background: #1e293b;
                padding: 15px;
                margin: 10px auto;
                width: 300px;
                border-radius: 10px;
            }
            input, button {
                padding: 8px;
                margin: 5px;
                width: 90%;
            }
        </style>
    </head>
    <body>

    <h1>🔐 Cloud Security System</h1>

    <div class="box">
        <h3>Register</h3>
        <form action="/register" method="post">
            <input name="u" placeholder="Username"><br>
            <input name="p" placeholder="Password"><br>
            <button>Register</button>
        </form>
    </div>

    <div class="box">
        <h3>Login</h3>
        <form action="/login" method="post">
            <input name="u"><br>
            <input name="p"><br>
            <button>Login</button>
        </form>
    </div>

    <div class="box">
        <h3>Encrypt</h3>
        <form action="/encrypt" method="post">
            <input name="file"><br>
            <button>Encrypt</button>
        </form>
    </div>

    <div class="box">
        <h3>Decrypt</h3>
        <form action="/decrypt" method="post">
            <input name="file"><br>
            <button>Decrypt</button>
        </form>
    </div>

    <div class="box">
        <h3>Integrity</h3>
        <form action="/hash" method="post">
            <input name="file"><br>
            <button>Check</button>
        </form>
    </div>

    <div class="box">
        <h3>Firewall</h3>
        <form action="/block" method="post">
            <input name="ip"><br>
            <button>Block</button>
        </form>
        <form action="/allow" method="post">
            <input name="ip"><br>
            <button>Allow</button>
        </form>
        <form action="/check" method="post">
            <input name="ip"><br>
            <button>Check</button>
        </form>
    </div>

    </body>
    </html>
    '''


@app.route('/register', methods=['POST'])
def register():
    return register_user(request.form['u'], request.form['p'])

@app.route('/login', methods=['POST'])
def login():
    return login_user(request.form['u'], request.form['p'])

@app.route('/encrypt', methods=['POST'])
def encrypt():
    return encrypt_file(request.form['file'])

@app.route('/decrypt', methods=['POST'])
def decrypt():
    return decrypt_file(request.form['file'])

@app.route('/hash', methods=['POST'])
def hash_file():
    return check_integrity(request.form['file'])

@app.route('/block', methods=['POST'])
def block():
    return block_ip(request.form['ip'])

@app.route('/allow', methods=['POST'])
def allow():
    return allow_ip(request.form['ip'])

@app.route('/check', methods=['POST'])
def check():
    return check_ip(request.form['ip'])


if __name__ == "__main__":
    app.run(debug=True)
