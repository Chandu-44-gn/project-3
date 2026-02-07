import streamlit as st
st.title("Hello World")
num1=st.number_input("Enter a Number 1")
num2=st.number_input("Enter a Number 2")

st.camera_input("buddies")
st.file_uploader("upload")

if st.button("Add"):
    st.title(num1+num2)
    
st.color_picker("red")

import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

words=st.text_area("enter the words")
if st.button("check"):
    result=words.split()
    st.title(len(result))

import streamlit as st
import re

st.title("Strong Password Creator")

def is_strong_password(password):
    # Minimum 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    # At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    # At least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    # At least one digit
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    # At least one special character
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]|:;\"'<>,.?/~`]", password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is strong."

# Password input (hidden)
password = st.text_input("Create a password:", type="password")
confirm_password = st.text_input("Confirm password:", type="password")

if st.button("Submit"):
    if password != confirm_password:
        st.error("Passwords do not match.")
    else:
        valid, message = is_strong_password(password)
        if valid:
            st.success("Password set successfully!")
        else:
            st.error(message)