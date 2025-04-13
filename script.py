
import asyncio
from openai import OpenAI
your_api_key = ""
client = OpenAI(api_key=your_api_key)

async def response():
    response = client.responses.create(
        model="gpt-4o",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response.output_text)



asyncio.run(response())