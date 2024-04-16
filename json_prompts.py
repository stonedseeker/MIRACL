import json
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

with open("metadata.json", "r") as file:
    metadata = json.load(file)

def get_answer(question):
    prompt = ""
    for key, value in metadata.items():
        prompt += f"{key}: {value}\n"
    prompt += f"\nQuestion: {question}\n"
    
    # Print out the prompt for debugging
    print("Prompt:", prompt)
    
    # Get answer from LLM using the generated prompt
    answer = qa_pipeline(context=prompt, question=question)
    return answer["answer"]



# Example questions
questions = [
    # "What were the traditional methods used for epilepsy classification before the adoption of deep learning techniques?",
    # "What are some of the key feature extraction techniques mentioned in the paper for EEG signal analysis?",
    "On which page can I find information about the methodology references used in the study?"
    # Add more questions as needed
]

# Get answers to the questions
for question in questions:
    answer = get_answer(question)
    print(f"Answer: {answer}\n")
    

