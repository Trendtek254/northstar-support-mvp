"""
Streamlit chat UI for NS-07: connects UI input state to backend handlers.
"""

import streamlit as st
from handlers import route_message

st.set_page_config(page_title="Northstar Support Chat", page_icon="💬")
st.title("💬 Northstar Support Chat")
st.caption("Ask about order status, returns/refunds, or stock availability.")

# Initialize chat history in session state (this IS the "UI input state")
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message to state and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Route to the correct backend handler and get a response
    response = route_message(user_input)

    # Add assistant response to state and display it
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)