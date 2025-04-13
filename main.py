from flask import Flask, render_template, url_for, request
import asyncio
from connect_genai import response

app = Flask(__name__)

@app.route("/")
def index():
    answer = ""
    return render_template("index.html", answer=answer)

@app.route("/ask", methods=['POST'])
def post():
    ask = request.form.get('ask')
    answer = asyncio.run(response(ask))
    return render_template('index.html', answer=answer)


app.run(host="127.0.0.1", port=3000)