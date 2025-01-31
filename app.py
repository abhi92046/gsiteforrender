from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def proxy():
    return redirect("google.com", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
