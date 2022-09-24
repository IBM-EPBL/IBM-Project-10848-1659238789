from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    return  render_template('main.html')

@app.route("/about",methods=["POST","GET"])
def about():
    return render_template('about.html')

@app.route("/signin",methods=["POST","GET"])
def signin():
    return render_template('signin.html')

@app.route("/form",methods=["POST","GET"])
def form():
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
    
