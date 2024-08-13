import streamlit as st
import traceback

def create_table(conn, cursor):

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            rollno VARCHAR(20),
            date DATE,
            subject VARCHAR(20)
            )

            """)
        conn.commit()
        st.success('Table created named students with columns id, name, rollno, date, subject')

    except Exception as e:
        st.error('Error is', e)
        print(traceback.format_exc())
