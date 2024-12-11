import streamlit as st
from send_email import send_email
import pandas as pd
df = pd.read_csv("topics.csv")


st.set_page_config(layout="wide", )

with st.form(key="form"):

    user_email = st.text_input(label="Your Email Address")

    options = st.selectbox(label="What topic do you want to discuss?",
                 options=df["topic"])

    raw_message =st.text_area(label="text")
    message = f"""\
Subject: new email from {user_email}

From: {user_email}

Topic {options}
{raw_message}    
    """


    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")