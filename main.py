from flask import Flask, render_template, url_for, request, jsonify
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
    gemini_response = asyncio.run(response(ask))
    answer = jsonify(**gemini_response)
    return render_template('index.html', answer=answer)


app.run(host="127.0.0.1", port=3000)