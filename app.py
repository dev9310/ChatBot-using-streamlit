import streamlit as st
import helper 
# import pathlib
import google.generativeai as genai
# from IPython.display import display
# from IPython.display import Markdown

st.markdown(helper.get_css() , unsafe_allow_html=True)

genai.configure(api_key='AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg')
model = genai.GenerativeModel('gemini-1.5-flash')

with st.sidebar:
    st.title("Welcome :sunglasses:")
    # messages =st.container(height=500)
    # if prompt1 := st.chat_input("Say something"):
    #     messages.chat_message("user").write(prompt1)
    #     messages.chat_message("assistant").write(f"Echo: {prompt1}")


def main():
    
    st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)
    # for m in he.genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.text(m.name)

    messages = st.container()
    prompt = st.chat_input("Say something")

    def stream_data(txt):
        for word in txt.split(" "):
            yield word + " "
            time.sleep(0.05)
        


    if prompt:
        messages.chat_message("user").write(prompt)
        response = model.generate_content(prompt)
        res = helper.to_markdown(response.text)
        # while response :
        #     st.spinner('Wait for a sec...!')
        st.chat_message("assistant").write_stream(stream_data(res))


import time

main()