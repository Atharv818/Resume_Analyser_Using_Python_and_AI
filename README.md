# AI Resume Analyzer

A Flask web app that uses Google Gemini AI to analyze PDF resumes against a target job description — providing a match score, missing skills, and improvement suggestions.

## How It Works
1. User uploads a resume (PDF) and pastes a job description
2. The app extracts resume text using PyMuPDF
3. The extracted text + job description are sent to Gemini with a structured prompt
4. Gemini returns a match score, missing skills, and actionable suggestions, rendered as formatted Markdown

## Tech Stack
- **Flask** — web framework
- **PyMuPDF (fitz)** — PDF text extraction
- **Google Gemini (gemini-2.5-flash)** — resume analysis
- **Bootstrap 5** — frontend styling
- **Marked.js** — Markdown rendering in the browser

## Setup

1. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. Copy \`.env.example\` to \`.env\` and add your Gemini API key:
   \`\`\`bash
   cp .env.example .env
   \`\`\`

3. Run:
   \`\`\`bash
   python src/main.py
   \`\`\`

4. Open \`http://localhost:5000\` in your browser

## Output Example
\`\`\`
Match Score: 78/100
Missing Skills:
- Docker
- CI/CD pipelines
Suggestions:
- Add specific metrics to project descriptions
- Highlight cloud deployment experience
\`\`\`

## Note
Uploaded resumes are stored temporarily in \`uploads/\` for processing and are not tracked in version control.
