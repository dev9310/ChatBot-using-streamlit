import streamlit as st
import helper as he


st.markdown("""
<style> 
h1{
   text-align: center; 
}
</style>
""" , unsafe_allow_html=True)

    

model = he.genai.GenerativeModel('gemini-1.5-flash')

def main():
    
    st.markdown('<h1 >Chat Bot</h1>',unsafe_allow_html=True)
    # for m in he.genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.text(m.name)

    prompt = st.chat_input("Say something")
    if prompt:
        response = model.generate_content(prompt)
        he.to_markdown(response)



main()