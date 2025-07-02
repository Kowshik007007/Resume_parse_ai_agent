from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

class JobItem(BaseModel):
    company: str
    designation: str
    duration_years: Optional[float] = Field(None, description="Duration in years")

class ResumeSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    city: Optional[str]
    country: Optional[str]
    skills: List[str]
    soft_skills: List[str] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    college_name: Optional[str]
    degree: Optional[str]
    total_experience: Optional[str]
    work_history: List[JobItem]
    summary: str
    languages: List[str] = Field(default_factory=list)
    social_links: List[str] = Field(default_factory=list)
