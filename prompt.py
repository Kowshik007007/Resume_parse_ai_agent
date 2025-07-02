from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from schema import ResumeSchema


parser = PydanticOutputParser(pydantic_object=ResumeSchema)

resume_prompt = PromptTemplate(
    template=(
        "You are an expert in resume parsing.\n"
        "Extract the following structured fields from the resume text.\n"
        "{format_instructions}\n\n"
        "🔹 Notes:\n"
        "- *languages*: ONLY spoken/written languages like English, Hindi, etc.\n"
        "- *work_history*: Extract company, designation, and duration_years in decimal format.\n"
        "- Use 0.2, 0.3 for short stints. Round to 2 or 3 for complete years.\n"
        "- Estimate for ongoing (present) jobs.\n"
        "- *social_links*: Include GitHub, LinkedIn, portfolio, or blog URLs.\n\n"
        "- *city* and *country*: Extract from the address, location, or context if present.\n\n"
        "- *soft_skills*: Include communication, leadership, teamwork, problem-solving, etc.\n\n"
        "- *certifications*: Extract professional certifications or course completions (e.g., AWS Certified, Google Data Analytics).\n\n"
        "Resume:\n\"\"\"\n{resume_text}\n\"\"\""
    ),
    input_variables=["resume_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

__all__ = ["parser", "resume_prompt"]
