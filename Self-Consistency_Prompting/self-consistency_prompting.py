import re
import json
from dotenv import find_dotenv, load_dotenv
from groq import Groq

load_dotenv(find_dotenv())

groq_client = Groq()

# Defining the prompt for the system and user, its different from other prompts because it's in more defined way that how the output should be.
# I wanted the output in the json format so that I can easily parse it and get the answer.

system_prompt = """
You are a great mathematician. Always understand the problem and break it down into smaller parts. This will help you solve the problem step by step. 
Always start with ```Let's think step by step.``` and then provide the solution. Always return a json in the format. 
Always include answer both in method and answer. If there are some unit in the question use them effectively.
Use proper json format.
```
{
    "method": Steps you used to solve the problem,
    "answer": Final Answer
}
```. 
For example:
Q: What is the sum of 15 and 25?
A: {
    "method": "Let's think step by step. Start with the numbers 15 and 25. Add them together: 15 + 25 = 40.",
    "answer": "40"
}
"""

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

def get_most_common_response(user_prompt):
    responses = []
    for i in range(5):
        response = chat_completion(user_prompt)
        responses.append(response)
    
    response_dict = {}
    max_count = 0    # To keep track of the most common response
    max_resp = dict()   # To store the most common response

    # Parsing the responses and getting the most common response.
    for response in responses:
        json_string = re.sub(r"\s+", " ", response).strip()
        dictionary = json.loads(json_string)
        if dictionary["answer"] in list(response_dict.keys()):
            response_dict[dictionary["answer"]]["count"] += 1
        else:
            response_dict[dictionary["answer"]] = {"count": 1, "method": dictionary["method"]}
        
        if response_dict[dictionary["answer"]]["count"] > max_count:
            max_count = response_dict[dictionary["answer"]]["count"]
            max_resp = dictionary

    return max_resp

if __name__ == "__main__":

    user_prompt = input("Ask a question: ")
    print("Answer: ", get_most_common_response(user_prompt))