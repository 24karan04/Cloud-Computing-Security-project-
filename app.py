from flask import Flask, request
from main import *

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Security Dashboard</title>

        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
            }

            header {
                background: #020617;
                padding: 20px;
                text-align: center;
                font-size: 28px;
                color: #38bdf8;
            }

            .container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                padding: 20px;
            }

            .card {
                background: #1e293b;
                width: 280px;
                margin: 15px;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 0 15px black;
            }

            h2 {
                text-align: center;
                color: #38bdf8;
            }

            input {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border-radius: 6px;
                border: none;
            }

            button {
                width: 100%;
                padding: 10px;
                background: #38bdf8;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }

            button:hover {
                background: #0ea5e9;
            }
        </style>
    </head>

    <body>

        <header>🔐 Cloud Security Dashboard</header>

        <div class="container">

            <div class="card">
                <h2>Register</h2>
                <form action="/register" method="post">
                    <input name="u" placeholder="Username">
                    <input name="p" placeholder="Password">
                    <button>Register</button>
                </form>
            </div>

            <div class="card">
                <h2>Login</h2>
                <form action="/login" method="post">
                    <input name="u" placeholder="Username">
                    <input name="p" placeholder="Password">
                    <button>Login</button>
                </form>
            </div>

            <div class="card">
                <h2>Encrypt File</h2>
                <form action="/encrypt" method="post">
                    <input name="file" placeholder="File name">
                    <button>Encrypt</button>
                </form>
            </div>

            <div class="card">
                <h2>Decrypt File</h2>
                <form action="/decrypt" method="post">
                    <input name="file" placeholder="File name">
                    <button>Decrypt</button>
                </form>
            </div>

            <div class="card">
                <h2>Firewall</h2>
                <form action="/block" method="post">
                    <input name="ip" placeholder="IP to block">
                    <button>Block</button>
                </form>

                <form action="/check" method="post">
                    <input name="ip" placeholder="Check IP">
                    <button>Check</button>
                </form>
            </div>

        </div>

    </body>
    </html>
    '''

# ---------------- ROUTES ----------------
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

@app.route('/block', methods=['POST'])
def block():
    return block_ip(request.form['ip'])

@app.route('/check', methods=['POST'])
def check():
    return check_ip(request.form['ip'])


if __name__ == "__main__":
    app.run()
