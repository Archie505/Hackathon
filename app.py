from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/browse")
def browse():
    return render_template("browse.html")

if __name__ == "__main__":
    app.run(debug=True)
