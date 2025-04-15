from flask import Flask, render_template, url_for, request, jsonify
import asyncio
from connect_genai import response
from formatting import format_gemini_response
from db.context import add_user_response


app = Flask(__name__)



# Routes

@app.route("/")
def index():
    answer = ""
    return render_template("index.html", answer=answer)


@app.route("/ask", methods=['POST'])
def post():
    ask = request.form.get('ask')
    askList = add_user_response(ask)
    gemini_response = asyncio.run(response(ask))
    answer = format_gemini_response(gemini_response)
    return render_template('index.html', ask=askList[0], answer=answer)


@app.route("/exp", methods=['POST']) # Route for testing things.
def experiment():
    answer = "Here is info<br><br>Here is some more"
    return render_template("index.html", answer=answer)


app.run(host="127.0.0.1", port=3000)
