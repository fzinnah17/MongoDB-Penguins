# MongoDB-Penguins 🐧 🍃
## Overview
Cover letters can be quite tedious, especially because filling out a job application in itself can take upwards of 2+ hours if there's a lot of questions involved. This can be mentally exhausting, especially because nowadays it's imperative that we apply for multiple jobs, at least 10-20 on a daily basis, and having a cover letter shows your passionate about the company's culture, the position and the company's mission. To reduce the fatigue job applicaiton has on our mental health, we decided to build a personalized cover letter. You may be wondering, "How does this differ from simply asking public models like ChatGPT or Gemini (formerly Bard), to generate a cover letter for you? The problem with using such tools, although can quickly generate a response, the tradeoff is that all we end up having is a generic cover letter. The problem with generic cover letter is that it doesn't convey your actual interest/passion you may have toward the role your applying for, nor does it sound anything like us, not to mention it is easy to distinguish between AI generaeted cover letters and personally written cover letters. So to fix the issue of generic/poorly written cover letter, we developed this software, which will take into consideration resume, transcript, personal portfolio, github portfolio and any additional documents written by you to take into conisderation your tonality, method of writting etc. (factors that the model should take into consideration) alongside prestored information of around 20 companies. Additionally, through the upload feature on the GUI, we are able to dynamically pass in additional information (such as another person's resume, specific job description, github portfolio/respositories the person wants to highlight, linkedin profile etc. from which the html is extracted and then converted to mongoDB nodes and added onto the existing vector database. After which, Huggingface LLMS model utilizes RAG to retrieve relevant contexual information to generate a cover letter that discusses the strong points you have listed in your resume, relevant experience and how you would be a good fit for the company based on your skillset, interest in tackling certain specific aspects of a company and what components of the comapny culture someone of your personality would value.

## How We Built it
We used Huggingface/Nomic to embed pdf based data that we parsed through. The embedded data was then stored into MongoDB vector database. Additionally, the links that were supplied during the prompt, alongside the preliminary base links that were provided, we used HTMLNodeParser() to extract the HTML code from the links and then converted the extracted content into nodes using llama index. The nodes were also added to the existing vector database. Lastly, the huggingface LLMS used the query provided alongside the information, retrieved the neccessary contextual information from the vector database to generate a cover letter based on the provided information it accessed (RAG Technique).

## Stretch Features
- [ ] Improving UI, due to the 8 hour time constraint, we quickly developed the UI using Streamlit
- [ ] Implement user authentication to ensure that the users can only access their own content and not the content of other users, providing security
- [ ] Improved options for dynamically passing in parameters, having more fields to have information relevant to the user will allow the model to make more accurate judgements and minimize model hallucinations.
- [ ] Improving the frontend and backend functionlaity
- [ ] Fixing and merging changes from other branches, the main branch still requires complete integration with multiple other branches.

### Video Walkthrough
Below Contains a Demo Video:

[Video 1: (Frontend View)](https://youtu.be/2INy342w2jE)

[Video 2: (Backend View)](https://youtu.be/yG3zQq3CrJM)




