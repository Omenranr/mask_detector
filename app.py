from flask import Flask, request

app = Flask('stock_pricer')


@app.route('/')
def showHello():
    return "hello world"


app.run("localhost", "9999", debug=True)
