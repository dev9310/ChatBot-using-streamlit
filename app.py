import streamlit as st
import helper 
import google.generativeai as genai
import time


genai.configure(api_key='AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg')
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown(helper.get_css() , unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1>Welcome</h1>",unsafe_allow_html=True)
    st.divider()



def create_recent_topic(topic):
    with st.sidebar:

        st.markdown("<h2>Recents</h2>",unsafe_allow_html=True)
        container = st.container(height=300)
        container.chat_message("user").write_stream(helper.stream_data(topic,0.6))

def intro():
    st.markdown(helper.get_intro())

def main():

    
    st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)
    
    messages = st.container()
    prompt = st.chat_input("Say something")

    if prompt:        
        messages.chat_message("human").write(prompt)
        response = model.generate_content(prompt)
        res = helper.to_markdown(response.text)
        
        st.chat_message("ai").write_stream(helper.stream_data(res))
        create_recent_topic(prompt)


main()