import PyPDF2

def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    
    elif file.type == "text/plain":
        return file.read().decode("utf-8").strip()

    else:
        return "❌ Unsupported file type."
