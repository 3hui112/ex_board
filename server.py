from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("APIExamNaverLogin.html")

@app login('/login')
def login():
    return render_template("callback.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)