

---

## 📄 `README.md`

```markdown
# 🧠 Resume Parser

A modular, full-stack resume parsing engine built with **FastAPI**, **React**, and **spaCy**. It extracts structured candidate data from `.pdf` and `.docx` resumes, stores it in a MySQL database, and displays it via a responsive frontend.

---

## 🚀 Features

- 🔍 NLP-powered resume parsing (skills, education, experience, links, etc.)
- 📄 Supports `.pdf` and `.docx` formats
- 🧠 Embedded link extraction from Word/PDF metadata
- 🧑‍💻 FastAPI backend with Swagger UI
- 🌐 React + Tailwind frontend with file upload and parsed data view
- 🗃️ MySQL integration for persistent storage
- 📦 Modular architecture for easy extension

---

## 🛠️ Tech Stack

| Layer      | Tech                          |
|------------|-------------------------------|
| Backend    | FastAPI, spaCy, pdfplumber, python-docx |
| Frontend   | React, Tailwind CSS, Vite     |
| Database   | MySQL                         |
| NLP        | spaCy `en_core_web_sm`        |

---

## 📁 Project Structure

```
resume_parser/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── api.py           # API routes
│   ├── parser.py        # File/text handling
│   ├── nlp.py           # NLP extraction logic
│   ├── models.py        # SQLAlchemy models
│   ├── database.py      # DB connection
│   ├── resumes/         # Uploaded files
│   └── static/          # React frontend build
```

---

## ⚙️ Setup Instructions

### 🔧 Backend

```bash
cd resume_parser
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn app.main:app --reload
```

### 🌐 Frontend

```bash
cd app/static
npm install
npm run dev
```

---

## 📬 API Endpoint

- `POST /upload-resume`  
  Accepts: `name`, `email`, `location`, `file`  
  Returns: Parsed JSON  
  Swagger: `http://localhost:8000/docs`

---

## 🧪 Sample Output

```json
{
  "name": "Praveen Baghel",
  "email": "xyz.com",
  "skills": "Java, Python, SQL, Spring Boot, React",
  "education": "B.Tech 2026 - HCST Mathura\nIntermediate 2018 - SVM Agra\nHigh School 2016 - NSSPS Agra",
  "linkedin_link": "https://linkedin.com/in/praveen",
  "github_link": "https://github.com/praveenbaghel",
  ...
}
```

---

## 📌 To-Do

- [ ] Add resume completeness scoring
- [ ] Build recruiter dashboard
- [ ] Add multi-language support
- [ ] Integrate resume preview and download

---

## 🧑‍💻 Author

**Praveen Baghel**  
Backend Engineer | Full-Stack Developer | ML Systems Architect  
📍 Agra, Uttar Pradesh  
📫 [praveenbaghel5573@gmail.com](mailto:praveenbaghel5573@gmail.com)

---

## 📄 License

Copyright © 2025 Praveen Baghel

Permission is granted to any individual or organization to use this software for personal, educational, or non-commercial purposes.

You may:
- View, run, and learn from the codebase
- Use it as a reference for your own projects

You may not:
- Modify or redistribute this codebase without explicit written permission from the author
- Use this software for commercial purposes without prior consent
- Remove or alter author attribution

This software is provided "as is", without warranty of any kind, express or implied.

All rights reserved.

```

---


