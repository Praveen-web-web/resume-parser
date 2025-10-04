from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    location = Column(String(100))
    skills = Column(Text)
    education = Column(Text)
    experience = Column(Text)
    certifications = Column(Text)
    achievements = Column(Text)
    summary = Column(Text)
    projects = Column(Text)
    internships = Column(Text)
    hobbies = Column(Text)
    interests = Column(Text)
    references = Column(Text)
    languages = Column(Text)
    linkedin_link = Column(String(255))
    github_link = Column(String(255))
    portfolio_link = Column(String(255))
    resume_path = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)