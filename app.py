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
                font-weight: bold;
                color: #38bdf8;
                box-shadow: 0 2px 10px black;
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
                box-shadow: 0 0 15px rgba(0,0,0,0.5);
                transition: 0.3s;
            }

            .card:hover {
                transform: scale(1.05);
            }

            h2 {
                color: #38bdf8;
                text-align: center;
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
                font-weight: bold;
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
                    <button type="submit">Register</button>
                </form>
            </div>

            <div class="card">
                <h2>Login</h2>
                <form action="/login" method="post">
                    <input name="u" placeholder="Username">
                    <input name="p" placeholder="Password">
                    <button type="submit">Login</button>
                </form>
            </div>

            <div class="card">
                <h2>Encrypt File</h2>
                <form action="/encrypt" method="post">
                    <input name="file" placeholder="File name">
                    <button type="submit">Encrypt</button>
                </form>
            </div>

            <div class="card">
                <h2>Decrypt File</h2>
                <form action="/decrypt" method="post">
                    <input name="file" placeholder="File name">
                    <button type="submit">Decrypt</button>
                </form>
            </div>

            <div class="card">
                <h2>Integrity Check</h2>
                <form action="/hash" method="post">
                    <input name="file" placeholder="File name">
                    <button type="submit">Check</button>
                </form>
            </div>

            <div class="card">
                <h2>Firewall</h2>
                <form action="/block" method="post">
                    <input name="ip" placeholder="IP to block">
                    <button>Block</button>
                </form>

                <form action="/allow" method="post">
                    <input name="ip" placeholder="IP to allow">
                    <button>Allow</button>
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
