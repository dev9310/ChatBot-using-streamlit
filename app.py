import streamlit as st
import helper 
import pathlib

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
genai.configure(api_key='AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg')


st.markdown("""
<style> 
h1{
   text-align: center; 
}
</style>
""" , unsafe_allow_html=True)

import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)



model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    
    st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)
    # for m in he.genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.text(m.name)

    prompt = st.chat_input("Say something")
    if prompt:
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))



main()