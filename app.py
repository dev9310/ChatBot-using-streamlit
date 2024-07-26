import streamlit as st
import helper 
# import pathlib
import google.generativeai as genai
# from IPython.display import display
# from IPython.display import Markdown
import streamlit.components.v1 as components


st.markdown(helper.get_css() , unsafe_allow_html=True)

genai.configure(api_key='AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg')
model = genai.GenerativeModel('gemini-1.5-flash')



with st.sidebar:
    st.markdown("<h1>Welcome</h1>",unsafe_allow_html=True)
    st.divider()

    # messages =st.container(height=500)
    # if prompt1 := st.chat_input("Say something"):
    #     messages.chat_message("user").write(prompt1)
    #     messages.chat_message("assistant").write(f"Echo: {prompt1}")


def stream_data(txt ,sleep_time=0.05):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(sleep_time)


def create_recent_topic(topic):
    with st.sidebar:

        st.markdown("<h2>Recents</h2>",unsafe_allow_html=True)
        container = st.container(height=300)
        container.chat_message("user").write_stream(stream_data(topic,0.6))

def intro():
    st.markdown(helper.get_intro())

def main():
    
    st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)
    # for m in he.genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.text(m.name)

    messages = st.container()
    prompt = st.chat_input("Say something")

    if prompt:
        
        messages.chat_message("human").write(prompt)
        response = model.generate_content(prompt)
        res = helper.to_markdown(response.text)
        # while response :
        #     st.spinner('Wait for a sec...!')
        st.chat_message("ai").write_stream(stream_data(res))
        create_recent_topic(prompt)

import time



main()