import traceback
import streamlit as st
def add_attendance(name, rollno, date, subject, conn, cursor):
    try:

        cursor.execute("""
            INSERT INTO students (name, rollno, date, subject)
                       VALUES (%s, %s, %s, %s)

""", (name, rollno, date, subject))

        conn.commit()
        st.success('Attendance Data was inserted into the tables')
    
    except Exception as e:
        st.error('Error is', e)
        print(traceback.format_exc())
