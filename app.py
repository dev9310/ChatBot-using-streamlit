import streamlit as st
import helper 
# import pathlib

import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown
genai.configure(api_key='AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg')


st.markdown(helper.get_css() , unsafe_allow_html=True)




model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    
    st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)
    # for m in he.genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.text(m.name)

    prompt = st.chat_input("Say something")
    if prompt:
        response = model.generate_content(prompt)
        st.markdown(helper.to_markdown(response.text))



main()