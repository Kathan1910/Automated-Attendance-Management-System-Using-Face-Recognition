# import streamlit as st
# import os
# import csv
# import json
# import cv2
# import face_recognition
# import pandas as pd
# import datetime
# import time
# import matplotlib.pyplot as plt
# import seaborn as sns
# from fpdf import FPDF
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# import schedule

# # Create necessary folders
# if not os.path.exists('emp_details'):
#     os.makedirs('emp_details')

# if not os.path.exists('emp_images'):
#     os.makedirs('emp_images')

# if not os.path.exists('attendance'):
#     os.makedirs('attendance')

# if not os.path.exists('reports'):
#     os.makedirs('reports')

# # Load employee details from JSON file
# json_path = os.path.join('emp_details', 'employee_details.json')
# if os.path.exists(json_path):
#     with open(json_path, 'r') as json_file:
#         employee_details_dict = json.load(json_file)
# else:
#     employee_details_dict = {}

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# # Initialize attendance data
# attendance_data = {}

# # Load existing attendance data from a CSV file
# attendance_directory = 'attendance'
# if not os.path.exists(attendance_directory):
#     os.makedirs(attendance_directory)

# current_date = datetime.datetime.now().strftime('%Y-%m-%d')
# csv_file_path = os.path.join(attendance_directory, f'attendance_{current_date}.csv')

# if os.path.exists(csv_file_path):
#     with open(csv_file_path, mode='r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             employee_name, department, role, timestamp = row
#             attendance_data[employee_name] = {
#                 'department': department,
#                 'role': role,
#                 'timestamp': timestamp,
#             }

# # Set the update interval in seconds
# update_interval = 60  # Update every minute

# last_update_time = time.time()

# def clear_form():
#     global emp_id, emp_name, emp_department, emp_role, emp_joining_date, uploaded_photo
#     emp_id = ''
#     emp_name = ''
#     emp_department = ''
#     emp_role = ''
#     emp_joining_date = ''
#     uploaded_photo = None

# st.title('Employee Registration and Attendance System')

# # Employee Registration Section
# st.sidebar.header('Employee Registration')
# emp_id = st.sidebar.text_input('Employee ID')
# emp_name = st.sidebar.text_input('Employee Name')
# emp_department = st.sidebar.text_input('Employee Department')
# emp_role = st.sidebar.text_input('Employee Role')
# emp_joining_date = st.sidebar.text_input('Joining Date (YYYY-MM-DD)')
# uploaded_photo = st.sidebar.file_uploader('Upload Photo', type=['jpg', 'png', 'jpeg'])

# if uploaded_photo is not None:
#     st.sidebar.image(uploaded_photo, caption='Uploaded Photo', use_column_width=True)

# # Check if emp_id is unique
# csv_path = os.path.join('emp_details', 'employee_details.csv')
# if emp_id and os.path.exists(csv_path):
#     with open(csv_path, mode='r', newline='') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         emp_ids = set()
#         for row in csv_reader:
#             if row:  # Check if the row is not empty
#                 emp_ids.add(row[0] if len(row) > 0 else "")  # Add the ID if available This change ensures that you only attempt to access the first element of each row if the row is not empty. If the row is empty or doesn't have any elements, it adds an empty string to the emp_ids set.


# # Register Button
# if st.sidebar.button('Register'):
#     if emp_id and emp_name and emp_department and emp_role and emp_joining_date and uploaded_photo:
#         # Convert employee name to lowercase
#         emp_name_lower = emp_name.lower()

#         # Update employee details in the dictionary
#         employee_details_dict[emp_name_lower] = {
#             'id': emp_id,
#             'department': emp_department,
#             'role': emp_role,
#             'joining_date': emp_joining_date
#         }

#         # Save employee details to JSON
#         with open(json_path, 'w') as json_file:
#             json.dump(employee_details_dict, json_file, indent=4)

#         # Save uploaded photo
#         image_path = os.path.join('emp_images', f'{emp_name_lower}.jpg')
#         image_path = image_path.lower()  # Convert to lowercase
#         with open(image_path, 'wb') as f:
#             f.write(uploaded_photo.read())

#         st.sidebar.success('Registration successful!')

#         # Clear form for the next registration
#         clear_form()

# # Display stored employee details
# if st.sidebar.button('Show Employee Details'):
#     st.write("Stored Employee Details:")
#     st.write(employee_details_dict)

# def generate_report(date, report_type):
#     try:
#         # Generate the attendance file path based on the selected date and directory
#         attendance_csv_path = os.path.join('attendance', f'attendance_{date}.csv')

#         # Check if the attendance file exists
#         if not os.path.exists(attendance_csv_path):
#             st.error(f"Attendance data file '{attendance_csv_path}' not found for the selected date. Please make sure it exists.")
#             return

#         # Load attendance data from the CSV file and convert the "Timestamp" column to datetime
#         df = pd.read_csv(attendance_csv_path, parse_dates=['Timestamp'])

#         # Create the "reports" directory if it doesn't exist
#         if not os.path.exists('reports'):
#             os.makedirs('reports')

#         # Generate and display the report
#         if report_type == "Daily":
#             st.subheader(f"Attendance Report for {date}")
#             st.write(df)
#             report_csv_path = os.path.join('reports', f'daily_report_{date}.csv')
#         elif report_type == "Weekly":
#             st.subheader(f"Weekly Attendance Report for {date}")
#             weekly_report = df.set_index('Timestamp').resample('W').count()
#             st.write(weekly_report)
#             report_csv_path = os.path.join('reports', f'weekly_report_{date}.csv')
#         elif report_type == "Monthly":
#             st.subheader(f"Monthly Attendance Report for {date}")
#             monthly_report = df.set_index('Timestamp').resample('M').count()
#             st.write(monthly_report)
#             report_csv_path = os.path.join('reports', f'monthly_report_{date}.csv')

#         # Export the report to a CSV file within the "reports" directory
#         df.to_csv(report_csv_path, index=False)
#         st.success(f"Report exported to {report_csv_path}")

#         # Generate and display a bar chart of daily attendance data
#         if report_type == "Daily":
#             st.subheader("Daily Attendance Bar Chart")
#             fig, ax = plt.subplots(figsize=(10, 6))
#             sns.countplot(data=df, x='Name', ax=ax)
#             plt.xticks(rotation=90)
#             st.pyplot(fig)

#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")

# def main():
#     st.title("Attendance System")

#     # List available dates based on files in the "attendance" directory
#     available_dates = [f.split('_')[1].split('.')[0] for f in os.listdir('attendance') if f.startswith('attendance_')]

#     # Add a date selection widget
#     selected_date = st.selectbox("Select a Date", available_dates)

#     # Add options for generating different types of reports
#     report_type = st.selectbox("Select Report Type", ["Daily", "Weekly", "Monthly"])

#     # Display attendance data or generate reports based on user selection
#     if st.button("Generate Report"):
#         generate_report(selected_date, report_type)

# if __name__ == "__main__":
#     main()



import streamlit as st
import os
import csv
import json
from datetime import datetime
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create necessary folders
if not os.path.exists('emp_details'):
    os.makedirs('emp_details')

if not os.path.exists('emp_images'):
    os.makedirs('emp_images')

# Load employee details from JSON file
json_path = os.path.join('emp_details', 'employee_details.json')
if os.path.exists(json_path):
    with open(json_path, 'r') as json_file:
        employee_details_dict = json.load(json_file)
else:
    employee_details_dict = {}

# Initialize global variables for employee registration
emp_id = ''
emp_name = ''
emp_department = ''
emp_role = ''
emp_joining_date = ''
uploaded_photo = None

# Function to clear the registration form
def clear_form():
    global emp_id, emp_name, emp_department, emp_role, emp_joining_date, uploaded_photo
    emp_id = ''
    emp_name = ''
    emp_department = ''
    emp_role = ''
    emp_joining_date = ''
    uploaded_photo = None

# Function to generate the daily, weekly, or monthly report
def generate_report(date, report_type):
    try:
        # Generate the attendance file path based on the selected date and directory
        attendance_csv_path = os.path.join('attendance', f'attendance_{date}.csv')

        # Check if the attendance file exists
        if not os.path.exists(attendance_csv_path):
            st.error(f"Attendance data file '{attendance_csv_path}' not found for the selected date. Please make sure it exists.")
            return

        # Load attendance data from the CSV file and convert the "Timestamp" column to datetime
        df = pd.read_csv(attendance_csv_path, parse_dates=['Timestamp'])

        # Create the "reports" directory if it doesn't exist
        if not os.path.exists('reports'):
            os.makedirs('reports')

        # Generate and display the report
        if report_type == "Daily":
            st.subheader(f"Attendance Report for {date}")
            st.write(df)
            report_csv_path = os.path.join('reports', f'daily_report_{date}.csv')
        elif report_type == "Weekly":
            st.subheader(f"Weekly Attendance Report for {date}")
            weekly_report = df.set_index('Timestamp').resample('W').count()
            st.write(weekly_report)
            report_csv_path = os.path.join('reports', f'weekly_report_{date}.csv')
        elif report_type == "Monthly":
            st.subheader(f"Monthly Attendance Report for {date}")
            monthly_report = df.set_index('Timestamp').resample('M').count()
            st.write(monthly_report)
            report_csv_path = os.path.join('reports', f'monthly_report_{date}.csv')

        # Export the report to a CSV file within the "reports" directory
        df.to_csv(report_csv_path, index=False)
        st.success(f"Report exported to {report_csv_path}")

        # Generate and display a bar chart of daily attendance data
        if report_type == "Daily":
            st.subheader("Daily Attendance Bar Chart")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(data=df, x='Name', ax=ax)
            plt.xticks(rotation=90)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("Integrated Employee Registration and Attendance System")

    # Add Streamlit app code for Employee Registration Form
    st.sidebar.header('Employee Details')
    global emp_id, emp_name, emp_department, emp_role, emp_joining_date, uploaded_photo

    emp_id = st.sidebar.text_input('Employee ID', emp_id)
    emp_name = st.sidebar.text_input('Employee Name', emp_name)
    emp_department = st.sidebar.text_input('Employee Department', emp_department)
    emp_role = st.sidebar.text_input('Employee Role', emp_role)
    emp_joining_date = st.sidebar.text_input('Joining Date (YYYY-MM-DD)', emp_joining_date)
    uploaded_photo = st.sidebar.file_uploader('Upload Photo', type=['jpg', 'png', 'jpeg'], key='emp_photo')

    if uploaded_photo is not None:
        st.sidebar.image(uploaded_photo, caption='Uploaded Photo', use_column_width=True)

    # Check if emp_id is unique
    csv_path = os.path.join('emp_details', 'employee_details.csv')
    if emp_id and os.path.exists(csv_path):
        with open(csv_path, mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            emp_ids = set(row[0] for row in csv_reader)
            if emp_id in emp_ids:
                st.sidebar.warning('Employee ID already exists. Please use a unique ID.')

    # Register Button
    if st.sidebar.button('Register'):
        if emp_id and emp_name and emp_department and emp_role and emp_joining_date and uploaded_photo:
            # Convert employee name to lowercase
            emp_name_lower = emp_name.lower()

            # Save employee details to CSV
            if not os.path.exists(csv_path):
                with open(csv_path, mode='w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['Employee ID', 'Employee Name', 'Department', 'Role', 'Joining Date'])

            with open(csv_path, mode='a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([emp_id, emp_name_lower, emp_department, emp_role, emp_joining_date])

            # Update employee details in the dictionary
            employee_details_dict[emp_name_lower] = {
                'id': emp_id,
                'department': emp_department,
                'role': emp_role,
                'joining_date': emp_joining_date
            }

            # Save uploaded photo
            image_path = os.path.join('emp_images', f'{emp_name_lower}.jpg')
            image_path = image_path.lower()  # Convert to lowercase
            with open(image_path, 'wb') as f:
                f.write(uploaded_photo.read())

            st.sidebar.success('Registration successful!')

            # Save employee details to JSON
            with open(json_path, 'w') as json_file:
                json.dump(employee_details_dict, json_file, indent=4)

            # Clear form for the next registration
            clear_form()

    # Display stored employee details
    if st.sidebar.button('Show Employee Details'):
        st.write("Stored Employee Details:")
        st.write(employee_details_dict)

    # Add Streamlit app code for Attendance System
    st.subheader("Attendance System")

    # List available dates based on files in the "attendance" directory
    available_dates = [f.split('_')[1].split('.')[0] for f in os.listdir('attendance') if f.startswith('attendance_')]
    selected_date = st.selectbox("Select a Date", available_dates)

    report_type = st.selectbox("Select Report Type", ["Daily", "Weekly", "Monthly"])

    if st.button("Generate Report"):
        generate_report(selected_date, report_type)

if __name__ == "__main__":
    main()
