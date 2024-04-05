from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # This route can render a home page that possibly extends base.html
    return render_template("index.html")  # Assuming index.html extends base.html

@app.route("/browse")
def browse():
    # Directly render the browse.html template
    return render_template("browse.html")

# Optional: If you really need a route for base.html directly, which is unusual.
@app.route("/base")
def base():
    # Direct example to render base.html directly, which is not common practice.
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)
