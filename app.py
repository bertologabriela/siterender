from flask import Flask

app = flask(__name__)

@app.route("/")
def index():
  return"Olá, <b>tudo bem?</b>"
