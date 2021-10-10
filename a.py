from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world</h1>"

@app.route("/testing")
def testing():
    return "<h1>this is testing page</h1>"

@app.route("/greet/<name>")
def greet(name):
    return f"<h1>good morning {name}</h1>"

@app.route("/api/test")
def apitest():
    return jsonify({"hello": "world"})

@app.route("/html")
def html():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()