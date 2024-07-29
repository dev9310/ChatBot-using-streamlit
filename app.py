import streamlit as st
import helper 
import google.generativeai as genai
import time

if "key" not in st.session_state:
    st.session_state.key = 'AIzaSyCi2c-H5RHN-OO4XOa3lCCcqsL_lxT6fNg'

genai.configure(api_key=st.session_state.key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Title
st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)

# Element Css
st.markdown(helper.get_css() , unsafe_allow_html=True)

# SideBar
with st.sidebar:
    st.markdown("<h1>Welcome</h1>",unsafe_allow_html=True)
    st.divider()
    container = st.container(height=300)



# Stream Data
def stream_data(txt ,sleep_time=0.05):
    for word in txt.split(" "):
        yield word + " "
        time.sleep(sleep_time)


# # Topic session state
# if "topic" not in st.session_state:
#     st.session_state.topic =[]


# # Save history data
# for topic in st.session_state.topic:
#     with container.chat_message(topic["role"]):
#         st.markdown(topic["message"])

if "message" not in st.session_state:
    st.session_state.message =[]

# Save history data
for msg in st.session_state.message:
    with st.chat_message(msg["role"]):
        st.markdown(msg["message"])






def intro():
    st.markdown(helper.get_intro())


def main():
    
    
    messages = st.container()
    prompt = st.chat_input("Say something")

    if prompt:      
        messages.chat_message("human").write(prompt)
        response = model.generate_content(prompt)
        res = helper.to_markdown(response.text)
        
        st.chat_message("ai").write_stream(stream_data(res))

        # Added messages to history
        st.session_state.message.append({"role":"user" ,"message":prompt})
        st.session_state.message.append({"role":"ai" ,"message":res})

        # with st.sidebar :
        #     container.chat_message("User").write_stream(stream_data(prompt,0.6))
        # st.session_state.topic.append({"role":"human" ,"message":prompt })  



main()

