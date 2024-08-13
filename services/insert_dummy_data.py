import streamlit as st
import traceback
def insert_dummy_data(conn, cursor):
    try:
        cursor.execute("""
                INSERT INTO students (name, rollno, date, subject)
                VALUES
                       ('John', '123', '2024-03-08', 'Math'),
                       ('Peter', '456', '2024-03-08', 'English'), 
                       ('Jane', '789', '2024-03-08', 'Science')        
         """)
        conn.commit()
        st.success('Dummy Data was inserted into the tables')
    except Exception as e:
        st.error('Error is', e)
        print(traceback.format_exc())
    