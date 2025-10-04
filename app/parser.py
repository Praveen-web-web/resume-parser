import docx2txt
from pdfminer.high_level import extract_text
import spacy
from .nlp import (
    extract_name, extract_email, extract_phone, extract_location,
    extract_skills, extract_education, extract_experience,
    extract_certifications, extract_achievements, extract_links,
    extract_summary, extract_projects, extract_languages,
    extract_hobbies, extract_interests, extract_references,
    extract_internships, extract_resume_path
)

nlp_model = spacy.load("en_core_web_sm")

def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format")

def parse_resume(text, file_path):
    links = extract_links(text, file_path)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "location": extract_location(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "certifications": extract_certifications(text),
        "achievements": extract_achievements(text),
        "summary": extract_summary(text),
        "projects": extract_projects(text),
        "internships": extract_internships(text),
        "hobbies": extract_hobbies(text),
        "interests": extract_interests(text),
        "references": extract_references(text),
        "languages": extract_languages(text),
        "linkedin_link": links["linkedin"],
        "github_link": links["github"],
        "portfolio_link": links["portfolio"],
        "resume_path": extract_resume_path(file_path)
    }