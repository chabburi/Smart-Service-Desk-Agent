

import streamlit as st
from agents import clean_strands_response


if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if "placeholder" not in st.session_state:
    st.session_state.placeholder = "Enter query here"

st.title("Welcome to Smart Service Desk Agent")
st.markdown(
    '''
    We are here to help you with your queries. 

    We Provide:
    1. Helping you in resolving query.
    2. Get status of your issue using user id.
    '''
)
text_input = st.text_input(
        "Please enter your query below 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
if text_input:
    response = clean_strands_response(text_input)
    
if st.button("Submit"):
    if text_input:
        response
    else:
        "Please provide a valid question to answer"
        