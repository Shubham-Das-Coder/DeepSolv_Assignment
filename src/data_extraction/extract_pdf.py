import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "E:/DeepSolv_Assignment/data/pdfs/Apple_Vision_Pro_Privacy_Overview.pdf"
    pdf_text = extract_text_from_pdf(pdf_path)
    with open("E:/DeepSolv_Assignment/data/extracted_pdf_text.txt", "w") as f:
        f.write(pdf_text)
