from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html", title="home")

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template('about.html', title="about")

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    return render_template('sign_in.html', title="sign_in")

@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    return render_template('sign_up.html', title="sign_up")

if __name__ == "__main__":
    app.run(debug = True)