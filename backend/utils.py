import PyPDF2
import io

def extract_text(file):
    """
    Extract text from uploaded file (.pdf or .txt).
    Returns cleaned string or error message.
    """

    try:
        if file.type == "application/pdf":
            reader = PyPDF2.PdfReader(file)
            text = "\n".join(
                page.extract_text() or "" for page in reader.pages
            )
            return text.strip() if text.strip() else "❌ No text found in the PDF."

        elif file.type == "text/plain":
            # Handle bytes or text object
            raw = file.read()
            text = raw.decode("utf-8", errors="ignore")
            return text.strip()

        else:
            return "❌ Unsupported file type. Please upload a .pdf or .txt file."

    except Exception as e:
        return f"❌ Error during extraction: {str(e)}"
