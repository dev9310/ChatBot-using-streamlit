import streamlit as st
import helper 
import google.generativeai as genai
import time

if "key" not in st.session_state:
    st.session_state.key = 'AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg'


genai.configure(api_key=st.session_state.key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown(helper.get_css() , unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1>Welcome</h1>",unsafe_allow_html=True)
    st.divider()
topic_list = []

def stream_data(txt ,sleep_time=0.05):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(sleep_time)


def create_recent_topic(topic):
    with st.sidebar:
        
        topic_list.append(topic)

        st.markdown("<h2>Recents</h2>",unsafe_allow_html=True)
        container = st.container(height=300)
        for i in topic_list:
            
            st.sidebar.text(i)
            container.chat_message("user").write_stream(stream_data(i,0.6))

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
        
        st.chat_message("ai").write_stream(stream_data(res))
        create_recent_topic(prompt)


main()