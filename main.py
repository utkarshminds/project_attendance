import streamlit as st
#postgresql
#pgadmin, postgresql
import psycopg2
from datetime import datetime

from services.create_empty_tables import create_table
from services.display_attendance import display_attendance
from services.insert_dummy_data import insert_dummy_data
from services.add_attendance import add_attendance

import hmac



def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# Main Streamlit app starts here


#connect to the database

conn = st.connection("postgresql", type="sql")

cursor = conn.cursor()

st.title('Attendance management system')

if st.button('Create table and insert dummy data'):
    create_table(conn, cursor)
    insert_dummy_data(conn, cursor)

st.subheader('Add attendance manually')
name = st.text_input('Name')
rollno = st.text_input('Rollno')
date = st.date_input('Date', datetime.now())
subject = st.text_input('Subject')

if st.button('Add data'):
    add_attendance(name, rollno, date, subject, conn, cursor)

st.subheader('Display attendance')
date_filter = st.date_input('Select date', datetime.now())
subject_filter = st.text_input('Select Subject')

if st.button('Display attendance data'):
    display_attendance(date_filter, subject_filter, conn, cursor)