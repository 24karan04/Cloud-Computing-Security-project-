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
            h1 {
                color: #38bdf8;
            }
            .box {
                background: #1e293b;
                padding: 15px;
                margin: 10px auto;
                width: 300px;
                border-radius: 10px;
                box-shadow: 0 0 10px #000;
            }
            input {
                padding: 8px;
                margin: 5px;
                width: 90%;
                border-radius: 5px;
                border: none;
            }
            button {
                padding: 8px 15px;
                background: #38bdf8;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background: #0ea5e9;
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
            <button type="submit">Register</button>
        </form>
    </div>

    <div class="box">
        <h3>Login</h3>
        <form action="/login" method="post">
            <input name="u" placeholder="Username"><br>
            <input name="p" placeholder="Password"><br>
            <button type="submit">Login</button>
        </form>
    </div>

    <div class="box">
        <h3>Encrypt File</h3>
        <form action="/encrypt" method="post">
            <input name="file" placeholder="File name"><br>
            <button type="submit">Encrypt</button>
        </form>
    </div>

    <div class="box">
        <h3>Decrypt File</h3>
        <form action="/decrypt" method="post">
            <input name="file" placeholder="File name"><br>
            <button type="submit">Decrypt</button>
        </form>
    </div>

    <div class="box">
        <h3>Check Integrity</h3>
        <form action="/hash" method="post">
            <input name="file" placeholder="File name"><br>
            <button type="submit">Check</button>
        </form>
    </div>

    <div class="box">
        <h3>Firewall</h3>
        <form action="/block" method="post">
            <input name="ip" placeholder="IP to block"><br>
            <button type="submit">Block</button>
        </form>
        <form action="/allow" method="post">
            <input name="ip" placeholder="IP to allow"><br>
            <button type="submit">Allow</button>
        </form>
        <form action="/check" method="post">
            <input name="ip" placeholder="Check IP"><br>
            <button type="submit">Check</button>
        </form>
    </div>

    </body>
    </html>
    '''
