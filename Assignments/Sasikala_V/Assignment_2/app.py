from flask import Flask,render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, world</p>"

@app.route("/")
def main():
    return  render_template("main.html")

@app.route("/about",methods=["POST","GET"])
def about():
    return render_template('about.html')

@app.route("/signin",methods=["POST","GET"])
def signin():
    return render_template('signin.html')

@app.route("/signup",methods=["POST","GET"])
def form():
    return render_template('form.html')

# @app.route("/profiles/<username>")
# def profile(username):
#     return "<p>Hello,"+username+" </p>"
if __name__ == '__main__':
    app.run(debug=True)