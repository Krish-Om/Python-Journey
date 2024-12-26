import fitz  # PyMuPDF
import pandas as pd
import re
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_mcq_from_pdf(pdf_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        mcq_data = []

        # Function to check if the color is blue
        def is_blue(color):
            # Convert negative color value to RGB
            if isinstance(color, int):
                color = color & 0xFFFFFF
                r = (color >> 16) & 0xFF
                g = (color >> 8) & 0xFF
                b = color & 0xFF
                return r == 0 and g == 0 and b == 255
            return False

        # Iterate through each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")
            blocks = page.get_text("dict")["blocks"]

            # Extract highlighted text
            highlighted_text = []
            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            color = span.get("color", 0)
                            logger.debug(f"Span color: {color}")
                            if is_blue(color):  # Check if the color is blue
                                highlighted_text.append(span["text"])

            logger.debug(f"Page {page_num + 1} highlighted text: {highlighted_text}")

            # Split text into lines
            lines = text.split('\n')
            question = None
            options = []
            answer = None

            for line in lines:
                line = line.strip()
                if re.match(r'^\d+\.', line):  # Question line
                    if question and options and answer:
                        mcq_data.append({
                            'Question': question,
                            'Option_A': options[0] if len(options) > 0 else '',
                            'Option_B': options[1] if len(options) > 1 else '',
                            'Option_C': options[2] if len(options) > 2 else '',
                            'Option_D': options[3] if len(options) > 3 else '',
                            'Answer': answer
                        })
                        logger.debug(f"Added question: {question}")
                    question = line
                    options = []
                    answer = None
                elif re.match(r'^[A-D]\)', line):  # Option line
                    options.append(line)
                elif line in highlighted_text:  # Answer line
                    answer = line

            # Add the last question
            if question and options and answer:
                mcq_data.append({
                    'Question': question,
                    'Option_A': options[0] if len(options) > 0 else '',
                    'Option_B': options[1] if len(options) > 1 else '',
                    'Option_C': options[2] if len(options) > 2 else '',
                    'Option_D': options[3] if len(options) > 3 else '',
                    'Answer': answer
                })
                logger.debug(f"Added question: {question}")

        # Create DataFrame and save to CSV with UTF-8 encoding
        df = pd.DataFrame(mcq_data)
        df.to_csv("mcq_data.csv", index=False, encoding='utf-8')
        logger.info("MCQ data extracted and saved to mcq_data.csv")
        print("MCQ data extracted and saved to mcq_data.csv")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_path = "DSA.pdf"
    extract_mcq_from_pdf(pdf_path)