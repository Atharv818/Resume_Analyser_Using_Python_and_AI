from flask import Flask, request, render_template     # Flas web framework to handle HTTP requests
import fitz  # PyMuPDF     used to extract text from pdf
from analyse_pdf import analyse_resume_gemini
import os                   # handling file paths and creating directories

app = Flask(__name__)           # create flask instance
app.config['UPLOAD_FOLDER'] = 'uploads'               # config a folder to store uploaded resumes
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)             # ensure thye folder exist


def extract_text_from_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


@app.route("/", methods=["GET", "POST"])       # @ defines the home page URL
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        job_description = request.form["job_description"]

        if resume_file.filename.endswith(".pdf"):
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(pdf_path)

            resume_content = extract_text_from_resume(pdf_path)
            result = analyse_resume_gemini(resume_content, job_description)

            return render_template("index.html", result=result)

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
