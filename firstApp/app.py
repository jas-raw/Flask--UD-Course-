from flask import Flask

app = Flask(__name__)

@app.route("/")
def get():
    return "Hello world"

#RUN: flask --app app run