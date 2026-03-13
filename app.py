import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page title
st.title("AI Hospital Assistant")

st.write("Ask questions about hospital admission, surgery preparation, discharge, or follow-ups.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_question = st.text_input("Ask your question")

if user_question:

    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    # Generate AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a healthcare assistant helping patients prepare for hospitalisation.

Give clear, short answers using bullet points.

You can answer questions about:
- hospital admission documents
- surgery preparation
- hospital discharge
- follow-up care
"""
            }
        ] + st.session_state.messages
    )

    ai_answer = response.choices[0].message.content

    # Add AI message
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_answer}
    )

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("**You:**", msg["content"])
    else:
        st.write("**Assistant:**", msg["content"])