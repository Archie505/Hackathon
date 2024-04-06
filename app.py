from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/browse")
def browse():
    return render_template("browse.html")

@app.route("/browse/travel")
def browse_travel():
    return render_template("browse_travel.html")

@app.route("/browse/tutoring")
def browse_tutoring():
    return render_template("browse_tutoring.html")

@app.route("/browse/creatives")
def browse_creatives():
    return render_template("browse_creatives.html")

@app.route("/browse/other_services")
def browse_other_services():
    return render_template("browse_other_services.html")

@app.route("/makepost")
def makepost():
    return render_template("makepost.html")

@app.route("/submitted")
def submitted():
    return render_template("submitted.html")

if __name__ == "__main__":
    app.run(debug=True)
