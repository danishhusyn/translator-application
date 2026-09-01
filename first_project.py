import streamlit as st
from groq import Groq

client=Groq(api_key=api_key)

st.title("English to urdu translator application")

text=st.text_area("Enter your Text")

if st.button("Translate"):
    completion=client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role":"user",
                    "content" : f"act as a translator and your job is only to traslate this text into urdu : \n{text}" 
                }
            ]

    )

    result=completion.choices[0].message.content

    st.subheader("Translated text")
    st.success(result)





