# PhysioConnect - Streamlit App with Enhanced UI and Features

import streamlit as st
from PIL import Image
import datetime

# Load logo
logo = Image.open("/mnt/data/Salinan dari Orange White Modern Geometric Business Company Profile Booklet_20250618_131842_0000.png")

# Initialize session states
if 'user_type' not in st.session_state:
    st.session_state.user_type = None
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Header with logo
col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, width=80)
with col2:
    st.markdown("""
    <h1 style='color:#D62828; font-size: 32px;'>PhysioConnect</h1>
    <p style='font-size:16px;'>Your Physiotherapy Telemedicine Hub</p>
    """, unsafe_allow_html=True)

# Sidebar login selection
st.sidebar.title("Login")
user_choice = st.sidebar.radio("Login as:", ["Patient", "Admin"])
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

# Dummy login validation
if login_button:
    if user_choice == "Admin" and username == "admin" and password == "admin123":
        st.session_state.user_type = "admin"
        st.sidebar.success("Logged in as Admin")
    elif user_choice == "Patient" and username:
        st.session_state.user_type = "patient"
        st.sidebar.success(f"Logged in as {username}")
    else:
        st.sidebar.error("Invalid credentials")

# Admin Features
if st.session_state.user_type == "admin":
    st.subheader("Admin Panel")
    admin_menu = st.selectbox("Choose Admin Task:", ["Reply to Patient Chats", "Add Physiotherapist", "Settings"])

    if admin_menu == "Reply to Patient Chats":
        st.info("Recent Patient Messages:")
        for msg in st.session_state.messages:
            st.write(f"**{msg['user']}**: {msg['text']}")
            reply = st.text_input(f"Reply to {msg['user']}", key=f"reply_{msg['user']}")
            if st.button(f"Send to {msg['user']}", key=f"send_{msg['user']}"):
                st.success(f"Message sent to {msg['user']}")

    elif admin_menu == "Add Physiotherapist":
        with st.form("Add Physio"):
            name = st.text_input("Physiotherapist Name")
            phone = st.text_input("Phone Number")
            location = st.text_input("Location")
            submitted = st.form_submit_button("Add")
            if submitted:
                st.success(f"Added physiotherapist: {name}")

    elif admin_menu == "Settings":
        st.write("Change settings below:")
        st.text_input("Change Password")
        st.selectbox("Language", ["English", "Bahasa Indonesia"])

# Patient Features
elif st.session_state.user_type == "patient":
    st.subheader("Welcome to PhysioConnect")
    menu = st.selectbox("Choose Service:", ["PhysioMU Journal Bank", "Physio Nearby", "Chat with Physio", "Exercise Recommendation"])

    if menu == "PhysioMU Journal Bank":
        st.write("Accessing Journal Bank...")
        st.markdown("[Open Jurnal Fisiomu UMS](https://journals.ums.ac.id/)")

    elif menu == "Physio Nearby":
        st.write("Google Maps Placeholder (integration needed)")
        st.image("https://developers.google.com/static/maps/images/maps-icon-64.png", width=60)
        st.info("Feature under development")

    elif menu == "Chat with Physio":
        st.write("Ask your question below:")
        chat_input = st.text_input("Type your message")
        if st.button("Send"):
            st.session_state.messages.append({"user": username, "text": chat_input})
            st.success("Message sent. A physiotherapist will reply shortly.")

    elif menu == "Exercise Recommendation":
        query = st.text_input("Enter your condition (e.g., low back pain)")
        if st.button("Get Recommendation"):
            st.info(f"Searching recommendations for: {query}")
            st.video("https://www.youtube.com/watch?v=4BOTvaRaDjI")
            st.markdown("**Instructions:**\n\n- Perform 3 sets of 10 reps each.\n- Rest 30 seconds between sets.")

# Guest users
else:
    st.warning("Please log in to access PhysioConnect features.")
