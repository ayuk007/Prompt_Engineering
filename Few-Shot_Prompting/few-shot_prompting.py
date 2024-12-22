from dotenv import find_dotenv, load_dotenv
from groq import Groq

load_dotenv(find_dotenv())

groq_client = Groq()

system_prompt = """
You are great at sarcasm. So whenever you see a situation or ask you something, give them answer in sarcastic manner.
For example:
User: Internet is down.
Bot: Great! Now I can finally focus on staring at the wall.
User: I burned the toast.
Bot: Fantastic! Just the way I love it—extra crunchy and black.
User: It's raining on my picnic day.
Bot: Perfect weather for an outdoor swim!
"""

groq_client.chat.completions.create(
    model = "llama3-8b-8192",
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
    ]
)

def chat_completion(user_prompt):

    response = groq_client.chat.completions.create(
                    model = "llama3-8b-8192",
                    messages = [
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ]
                )
    return response.choices[0].message.content
 
if __name__ == "__main__":

    user_prompt = input("Ask a question: ")
    print("Answer: ", chat_completion(user_prompt))    
