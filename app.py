import openai
import streamlit as st


openai.api_key = "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" 

st.title("AI Personal Assistant 🤖")  
st.write("Ask me anything!")


user_input = st.text_input("You:")


if st.button("Send"):
    if user_input:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("🤖 AI:", response["choices"][0]["message"]["content"])
        
