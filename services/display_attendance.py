import traceback
import streamlit as st

def display_attendance(date_filter, subject_filter, conn, cursor):
    try:
        cursor.execute(
            """SELECT name, rollno FROM students WHERE date = %s AND subject 
              = %s""",(date_filter, subject_filter)
        )
        rows = cursor.fetchall()
        if rows:
            st.write('Students on', date_filter, 'for subject', subject_filter)
            for row_data in rows:
                st.write(row_data[0], " - ", row_data[1])
            
            st.success('Data was retrieved from the tables')
        else:
            st.write('No data found')
        conn.commit()
        
    except Exception as e:
        st.error('Error is', e)
        print(traceback.format_exc())