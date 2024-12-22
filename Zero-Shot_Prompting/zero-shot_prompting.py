from dotenv import find_dotenv, load_dotenv
from groq import Groq

load_dotenv(find_dotenv())

groq_client = Groq()

system_prompt = "You are a good translator. Whenever user asks a question in English, translate it to French."

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
