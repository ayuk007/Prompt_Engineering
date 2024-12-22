from dotenv import find_dotenv, load_dotenv
from groq import Groq

load_dotenv(find_dotenv())

groq_client = Groq()

prompt = "Translate this sentence into Spanish: 'I love programming.'"

response = groq_client.chat.completions.create(
    model = "llama3-8b-8192",
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
)

response.choices[0].message.content