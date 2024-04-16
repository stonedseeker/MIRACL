import json
from transformers import pipeline
import PyPDF2

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")


with open("metadata2.json", "r") as file:
    metadata = json.load(file)

def extract_text_from_pdf(pdf_file_path):
    pdf_text = ""
    try:
        with open(pdf_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)  # Get number of pages using len()
            for page_num in range(num_pages):
                page = reader.pages[page_num]  # Access page using reader.pages[index]
                pdf_text += page.extract_text()
    except Exception as e:
        print("Error occurred while extracting text from PDF:", e)
    return pdf_text

def answer_question(question, pdf_text, metadata):
    prompt = ""
    for key, value in metadata.items():
        prompt += f"{key}: {value}\n"
    prompt += f"\nPDF Text: {pdf_text}\n\nQuestion: {question}\n"
    
    try:
        answer = qa_pipeline(context=prompt, question=question)
        return answer["answer"]
    except Exception as e:
        print("Error occurred while answering question:", e)
        return None

pdf_file_path = "/home/vybhv/Downloads/NCT.pdf"

pdf_text = extract_text_from_pdf(pdf_file_path)

if pdf_text:
    questions = [
       "Which city is mentioned?"
    ]

    for question in questions:
        answer = answer_question(question, pdf_text, metadata)
        if answer:
            print(f"Question: {question}\nAnswer: {answer}\n")
else:
    print("No text extracted from the PDF.")









