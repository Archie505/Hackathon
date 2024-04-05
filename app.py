from flask import Flask, redirect, url_for, render_template
app=Flask(__name__) 

@app.route("/")#this initiates the home page
def home():
    return render_template("index.html")



@app.route("/<name>") #the <> passes that variable into the function 
def user(name):
    return f"Hello {name}" 

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Admin"))



if __name__ == "__main__":
    app.run()