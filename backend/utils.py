import PyPDF2

def extract_text(file):
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        return ""
