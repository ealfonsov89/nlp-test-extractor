import PyPDF2
import spacy

nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Función para procesar texto con spaCy y extraer entidades relevantes
def process_text_and_extract_questions_answers(text):
    doc = nlp(text)

    questions_and_answers = []
    current_question: str = ''
    current_answers = []

    for token in doc:
        if token.is_ and token.text.endswith('.') in token.whitespace_:
            current_question += "{}{}\n".format(token.text, token.whitespace_)
        if current_question != '':
            questions_and_answers.append((current_question, []))
            current_question = ''
    return questions_and_answers

# Path to the PDF file
pdf_path = './test.pdf'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Process text and extract questions and answers
extracted_questions_answers = process_text_and_extract_questions_answers(pdf_text)

# Print the result
for question, answers in extracted_questions_answers:
    print("Question:", question)
    print("Answers:", answers)
    print("---")