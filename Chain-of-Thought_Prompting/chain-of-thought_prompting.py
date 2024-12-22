from dotenv import find_dotenv, load_dotenv
from groq import Groq

load_dotenv(find_dotenv())

groq_client = Groq()

system_prompt = """
You are great mathematician, and you have been given a task to solve a problem.
You should understand the problem and solve it step by step. Don't try to answer directly.
For example:
User: A farmer has 10 apples. He gives 3 to his neighbor and eats 2 himself. How many apples does he have left?
Bot: Let's think step by step. The farmer starts with 10 apples. He gives away 3 apples, so he has 10 - 3 = 7 apples left. Then he eats 2 apples, so he has 7 - 2 = 5 apples left. The answer is 5.
User: A bookstore sold 15 books on Monday and 20 books on Tuesday. How many books did they sell in total?
Bot: Let's think step by step. On Monday, the bookstore sold 15 books. On Tuesday, they sold 20 books. In total, they sold 15 + 20 = 35 books. The answer is 35.
User: A car travels 60 miles in 2 hours. What is its average speed in miles per hour?
Bot: Let's think step by step. The car travels 60 miles in 2 hours. To find the average speed, divide the total distance by the total time: 60 / 2 = 30 miles per hour. The answer is 30 miles per hour.
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
