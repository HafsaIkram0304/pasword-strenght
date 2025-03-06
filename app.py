import re
import streamlit as st

# Page styling.
st.set_page_config(page_title="Strength Password", page_icon="🔑", layout="centered")

# Custom CSS.
st.markdown(
    """
    <style>
     .main {text-align: center;}
     .stTextInput {width: 60% !important;}
     .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
     .stButton button:hover {background-color: #45a049;}
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title and Description.
st.title("🔐 Password Strength Checker")
st.write("🔍 This app checks the strength of your password and suggests improvements.")

# Function to check password strength.
def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 6:
        score += 1
    else:
        feedback.append("❌ Password must be at least **6 characters long**.")

    if re.search('[A-Z]', password) and re.search('[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password must contain both **uppercase (A-Z) and lowercase (a-z) characters**.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least **one number (0-9)**.")

    if re.search(r'[!@#$%^&*()_+]', password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least **one special character (!@#$%^&*)**.")

    # Display password strength
    if score == 4:
        st.success("✔️ **Strong Password** - Your Password is secure.")
    elif score == 3:
        st.warning("⚠️ **Medium Password** - Your Password is fairly secure but could be improved.")
    else:
        st.error("❌ **Weak Password** - Your Password is not secure.")

    # Display feedback if improvements are needed
    if feedback:
        with st.expander("📌 **Improve your password by following these suggestions:**"):
            for item in feedback:
                st.write(item)

# Get user input
password = st.text_input("Enter your password", type="password", help="Ensure your password is at least 6 characters long.")

# Button to check password strength
if st.button("Check"):
    if password:
        check_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")
