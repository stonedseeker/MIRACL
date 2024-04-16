import PyPDF2
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_answer_from_pdf(question, pdf_path):
    # Load text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Construct prompt using PDF text
    prompt = f"{pdf_text}\n\nQuestion: {question}\n"
    
    # Get answer from the BERT-based model
    answer = qa_pipeline(context=prompt, question=question)
    return answer["answer"]

# Example PDF file path
pdf_path = "Lekshmy.pdf"

# Example questions
questions = [
    "What is the primary focus of the proposed model discussed in the paper?"
    # Add more questions as needed
]

# Get answers to the questions
for question in questions:
    answer = get_answer_from_pdf(question, pdf_path)
    print(f"Question: {question}\nAnswer: {answer}\n")
