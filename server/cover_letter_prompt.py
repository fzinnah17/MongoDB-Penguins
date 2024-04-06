from llama_index.core.prompts import Prompt

COVER_LETTER_PROMPT_STR = """\
Write a cover letter based on the provided applicant's information.\
Make sure to include their name and relate their experiences directly to the job description.\
Do not include information that is not provided.

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
