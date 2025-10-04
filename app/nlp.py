import re
import pdfplumber
from docx import Document
import os


def extract_skills(text):
    keywords = ["Java", "Python", "SQL", "Spring Boot", "React", "Docker"]
    found = [kw for kw in keywords if kw.lower() in text.lower()]
    return ", ".join(found)

def extract_education(text):
    lines = text.split("\n")
    education_keywords = ["B.Tech", "M.Tech", "Intermediate", "High School", "B.Sc", "MCA"]
    education = []

    for i, line in enumerate(lines):
        if any(kw.lower() in line.lower() for kw in education_keywords):
            institution = lines[i + 1].strip() if i + 1 < len(lines) else ""
            entry = f"{line.strip()} - {institution}" if institution else line.strip()
            education.append(entry)

    return "\n".join(education[:5]) if education else "Not found"

def extract_experience(text):
    exp_keywords = ["Experience","Company","Role","Position","Duration","Intern", "Developer", "Engineer", "Project", "Worked at"]
    lines = text.split("\n")
    relevant = [line for line in lines if any(kw in line for kw in exp_keywords)]
    return "\n".join(relevant[:5])  # top 5 lines


def extract_certifications(text):
    cert_keywords = ["certified", "certification", "AWS", "Azure", "Google Cloud", "Oracle", "Cisco"]
    lines = text.split("\n")
    certs = [line for line in lines if any(kw.lower() in line.lower() for kw in cert_keywords)]
    return "\n".join(certs[:5])  # top 5 matches

def extract_achievements(text):
    achievement_keywords = ["won", "ranked", "awarded", "selected", "finalist", "top"]
    lines = text.split("\n")
    achievements = [line for line in lines if any(kw.lower() in line.lower() for kw in achievement_keywords)]
    return "\n".join(achievements[:5])


def extract_links(text, file_path=None):
    # Extract from visible text
    linkedin = re.search(r"(https?://)?(www\.)?linkedin\.com/in/[^\s]+", text)
    github = re.search(r"(https?://)?(www\.)?github\.com/[^\s]+", text)
    portfolio = re.search(r"(https?://)?(www\.)?[a-zA-Z0-9\-]+\.(dev|me|tech|com|io)", text)

    # Auto-detect file type
    embedded_links = []
    if file_path:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".pdf":
            embedded_links = extract_pdf_links(file_path)
        elif ext == ".docx":
            embedded_links = extract_all_links(file_path)

    # Match embedded links to known platforms
    for link in embedded_links:
        if "linkedin.com" in link:
            linkedin = re.match(r".*", link)
        elif "github.com" in link:
            github = re.match(r".*", link)
        elif any(ext in link for ext in [".dev", ".me", ".tech", ".com", ".io"]):
            portfolio = re.match(r".*", link)

    return {
        "linkedin": linkedin.group() if linkedin else "Mentioned but no URL",
        "github": github.group() if github else "Mentioned but no URL",
        "portfolio": portfolio.group() if portfolio else "Mentioned but no URL"
    }

def extract_all_links(docx_path):
    doc = Document(docx_path)
    rels = doc.part.rels
    urls = [rel.target_ref for rel in rels.values() if "hyperlink" in rel.reltype]
    return urls


def extract_pdf_links(pdf_path):
    links = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for annot in page.annots or []:
                if annot.get("uri"):
                    links.append(annot["uri"])
    return links

def extract_summary(text):
    match = re.search(r"# Summary\n([\s\S]+?)(?:\n#|\n##|\Z)", text)
    if match:
        return match.group(1).strip()
    # Fallback: look for keywords
    summary_keywords = ["summary", "objective", "profile", "about me"]
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if any(kw in line.lower() for kw in summary_keywords):
            return "\n".join(lines[i+1:i+4]).strip()
    return "Not found"

def extract_projects(text):
    project_keywords = ["project", "developed", "created", "built", "designed","Implemented"]
    lines = text.split("\n")
    projects = [line for line in lines if any(kw.lower() in line.lower() for kw in project_keywords)]
    return "\n".join(projects[:5])  # top 5 projects

def extract_languages(text):
    language_keywords = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Hindi"]
    found = [kw for kw in language_keywords if kw.lower() in text.lower()]
    return ", ".join(found)

def extract_hobbies(text):
    hobby_keywords = ["reading", "traveling", "gaming", "music", "sports", "cooking", "photography"]
    found = [kw for kw in hobby_keywords if kw.lower() in text.lower()]
    return ", ".join(found)

def extract_interests(text):
    interest_keywords = ["AI", "Machine Learning", "Web Development", "Mobile Apps", "Cloud Computing", "Cybersecurity"]
    found = [kw for kw in interest_keywords if kw.lower() in text.lower()]
    return ", ".join(found)

def extract_references(text):
    reference_keywords = ["reference", "referee", "contact","References","Recommendation"]
    lines = text.split("\n")
    references = [line for line in lines if any(kw.lower() in line.lower() for kw in reference_keywords)]
    return "\n".join(references[:5])  # top 5 references

def extract_phone(text):
    phone = re.search(r"\+?\d[\d -]{8,}\d", text)
    return phone.group() if phone else "Unknown"

def extract_email(text):
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return emails[0] if emails else "Unknown"

def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        if len(line.split()) <= 4 and all(c.isalpha() or c.isspace() for c in line):
            return line.strip()
    return "Unknown"


def extract_location(text):
    location_keywords = ["Address", "Location", "City", "State", "Pincode"]
    lines = text.split("\n")
    for line in lines:
        if any(kw.lower() in line.lower() for kw in location_keywords):
            return line.strip()
    
    cities = ["Agra", "Delhi", "Mumbai", "Bangalore", "Hyderabad"]
    for city in cities:
        if city.lower() in text.lower():
            return city
    return "Unknown"

def extract_internships(text):
    internship_keywords = ["internship", "intern", "worked at", "project", "summer training" , "Summer Internship","Winter Internship"]
    lines = text.split("\n")
    internships = [line for line in lines if any(kw.lower() in line.lower() for kw in internship_keywords)]
    return "\n".join(internships[:5])  # top 5 internships

def extract_resume_path(file_path):
    return file_path