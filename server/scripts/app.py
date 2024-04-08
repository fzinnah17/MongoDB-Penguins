import streamlit as st
from gen_cover_letter import main 
# from example_data import example_cv, example_job_description

st.set_page_config(page_title="Home Page", page_icon=":lemon:", layout="centered")

hide_menu_style = "<style> footer {visibility: hidden;} textarea {width: -webkit-fill-available; height: 1200px;} </style>"
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("📝 CoverCraft: Tailored Applications")
    
st.info("Please enter the requested information in the text areas below. Then click the submit button to generate your cover letter.", icon='ℹ️')
    
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
           st.markdown(f'<textarea>{download_button_html}</textarea>', unsafe_allow_html=True)
   


            