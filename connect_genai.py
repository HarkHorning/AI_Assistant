import asyncio
from google import genai
from dotenv import find_dotenv, load_dotenv
import os

envirenment = find_dotenv()
load_env = load_dotenv(envirenment)
API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)

question = input("What would you like to ask Gemini? ")

async def response():
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=question
    )
    print(response.text)

asyncio.run(response())