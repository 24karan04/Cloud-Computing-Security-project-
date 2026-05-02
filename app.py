from flask import Flask, render_template, request, redirect, url_for
import base64

app = Flask(__name__)

def encrypt_text(text):
    return base64.b64encode(text.encode()).decode()

def decrypt_text(text):
    return base64.b64decode(text.encode()).decode()

@app.route("/")
def home():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------------- ENCRYPT ----------------

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    if request.method == "POST":
        text = request.form["text"]
        return redirect(url_for("encrypt_process", text=text))
    return render_template("encrypt.html")

@app.route("/encrypt/process")
def encrypt_process():
    text = request.args.get("text")
    return render_template("encrypt_process.html", text=text)

@app.route("/encrypt/result")
def encrypt_result():
    text = request.args.get("text")
    result = encrypt_text(text)
    return render_template("encrypt_result.html", result=result)

# ---------------- DECRYPT ----------------

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    if request.method == "POST":
        text = request.form["text"]
        return redirect(url_for("decrypt_process", text=text))
    return render_template("decrypt.html")

@app.route("/decrypt/process")
def decrypt_process():
    text = request.args.get("text")
    return render_template("decrypt_process.html", text=text)

@app.route("/decrypt/result")
def decrypt_result():
    text = request.args.get("text")
    result = decrypt_text(text)
    return render_template("decrypt_result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
