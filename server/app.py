import streamlit as st
from gen_cover_letter import main 
# from example_data import example_cv, example_job_description

st.set_page_config(page_title="Home Page", page_icon=":lemon:", layout="centered")

hide_menu_style = "<style> footer {visibility: hidden;} </style>"
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("👩🏼‍💻 Cover Letter Generator")
    
st.info("Please enter your CV and the job description in the text areas below. Then click the submit button to generate your cover letter. (Reponse has a limit of 250 words)", icon='ℹ️')
    
with st.form("my_form"):
   st.write("Inside the form")
   jobDescription = st.text_input('Pasted Job Description', '')
   companywebsite = st.text_input('Company website', '')
   resume = st.text_input('resume', '')
   github = st.text_input('github', '')
   
   submit = st.form_submit_button('Submit')
   
   if submit:
       with st.spinner('Generating cover letter...'):
           download_button_html = main(jobDescription)
           st.markdown(download_button_html, unsafe_allow_html=True)
        #    text_output = main()
        #    st.text_area(label='Cover Letter:',value=text_output)
   


            