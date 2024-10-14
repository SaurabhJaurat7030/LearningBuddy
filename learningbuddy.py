import streamlit as st
import numpy as np
import random
import time


st.title("🌨️ LearnBuddy")
st.markdown("<p style='color:gray; font-style:italic;'>Ask questions and get instant answers on functional testing, business cases, and more!</p>", unsafe_allow_html=True)



with st.spinner("Thinking"):
    time.sleep(0.5)  # Simulate a process



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    if message["role"] == "assistant":
        col1, col2 = st.columns([5, 1])  # Assistant on left (wider column on right)
        with col1:
            st.chat_message(message["role"]).markdown(message["content"])

    else:
        col1, col2 = st.columns([1, 5])  # User on right (wider column on left)
        with col2:
            st.chat_message(message["role"]).markdown(message["content"])

# Input prompt for the user
prompt = st.chat_input("How can I help you today")

if prompt:
    # Display user message in the right column
    col1, col2 = st.columns([1, 5])
    with col2:
        st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate assistant response with simulated delay
    def response_generator():
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    # Display assistant response in the left column
    col1, col2 = st.columns([5,1])
    with col1:
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
