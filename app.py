
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! Welcome to my Python DevOps Project!."

@app.route("/about")
def about():
    return "This application is created using Python Flask."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
