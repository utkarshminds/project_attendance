import streamlit as st
#postgresql
#pgadmin, postgresql
import psycopg2
from datetime import datetime

from services.create_empty_tables import create_table
from services.display_attendance import display_attendance
from services.insert_dummy_data import insert_dummy_data
from services.add_attendance import add_attendance

#connect to the database

conn = psycopg2.connect(
    dbname = 'attendance',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)

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