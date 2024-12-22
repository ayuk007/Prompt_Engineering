# Few-Shot Prompting

## What is Few-Shot Prompting?

**Few-Shot Prompting** is a method of using language models to perform tasks by providing multiple examples in the input prompt. These examples guide the model to understand the task better, enabling it to produce accurate and contextually relevant outputs.

### Key Features:
- **Multiple Example Guidance:** Provides several examples to demonstrate the task.
- **Enhanced Task Understanding:** Improves performance compared to zero-shot and one-shot prompting.
- **Applicable Across Domains:** Works well for diverse tasks like summarization, classification, creative writing, etc.

---

## How Does It Work?

Few-shot prompting involves writing a prompt that includes multiple examples of the task, followed by the task the model is expected to perform. This technique reduces ambiguity and leverages the model’s ability to generalize from examples.

### Example Prompt for Sarcastic Jokes:
```plaintext
Create a sarcastic joke based on the given situation:

Example 1:
Situation: "The internet is down."
Joke: "Great! Now I can finally focus on staring at the wall."

Example 2:
Situation: "I burned the toast."
Joke: "Fantastic! Just the way I love it—extra crunchy and black."

Example 3:
Situation: "It's raining on my picnic day."
Joke: "Perfect weather for an outdoor swim!"

Now, create a sarcastic joke for this situation: "I'm stuck in traffic."
```

### Expected Output:
```plaintext
"Oh, wonderful! Just the perfect moment to enjoy the beautiful sights of bumper-to-bumper cars."
```

---

## Examples of Few-Shot Prompting

1. **Sarcastic Jokes:**
   - Situation: "My alarm didn’t go off this morning."
     - Joke: "Ah, just what I needed—an extra hour of panic to start the day!"

2. **Creative Writing:**
   - Task: Write a creative caption for a photo of a cat sleeping on a pile of books.
     - Examples:
       - "Example 1: 'Clearly, the cat is preparing for a nap degree.'"
       - "Example 2: 'When you study so hard, you dream about it.'"
     - Caption: "This is what they mean by 'cat-aloging knowledge.'"

3. **Summarization:**
   - Task: Summarize a paragraph.
     - Examples:
       - "Example 1: 'Artificial intelligence is transforming industries.' -> 'AI is changing industries.'"
       - "Example 2: 'Machine learning improves efficiency and automation.' -> 'ML boosts efficiency.'"
     - Input: "Data science combines statistics, programming, and domain knowledge."
     - Output: "Data science integrates various fields."

---

## Advantages of Few-Shot Prompting

1. **Improved Context Understanding:** Multiple examples enhance the model’s comprehension.
2. **Flexibility:** Effective across creative, analytical, and technical domains.
3. **Higher Accuracy:** Outperforms zero-shot and one-shot prompting in complex tasks.

---

## Limitations

1. **Input Length Constraints:** Limited examples can be included due to token restrictions.
2. **Time Consumption:** Writing multiple examples takes more effort.
3. **Domain Dependency:** Examples may need to be tailored for specific use cases.

---