from llama_index.core.prompts import Prompt

# Note that this allows is for writting multiline strings in Python
COVER_LETTER_PROMPT_STR = """\n 
Write a cover letter based on the provided applicant's information.\n
Make sure to include their name and relate their experiences directly to the job description.\n
Do not include information that is not provided.

Note that if you cannot find a resume, utilize the vector database resume, alongside the relevant additional information about the individual, such as their transcript, LinkedIn, or GitHub profile.\n

<Applicant personal information>
{applicant_personal_information}

<Applicant skills>
{applicant_skills}

<Applicant experiences>
{applicant_experiences}

<Job description>
{job_description}

<Cover letter>
"""

COVER_LETTER_PROMPT_TEMPLATE = Prompt(COVER_LETTER_PROMPT_STR)