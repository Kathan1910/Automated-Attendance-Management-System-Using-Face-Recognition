# import streamlit as st
# import os
# import csv
# from datetime import datetime
# import cv2

# # Create necessary folders
# if not os.path.exists('emp_details'):
#     os.makedirs('emp_details')

# if not os.path.exists('emp_images'):
#     os.makedirs('emp_images')

# st.title('Employee Attendance System')

# def clear_form():
#     global emp_id, emp_name, emp_department, emp_role, emp_joining_date, uploaded_photo
#     emp_id = ''
#     emp_name = ''
#     emp_department = ''
#     emp_role = ''
#     emp_joining_date = ''
#     uploaded_photo = None

# # Employee Details
# st.sidebar.header('Employee Details')
# emp_id = st.sidebar.text_input('Employee ID')
# emp_name = st.sidebar.text_input('Employee Name')  # No lowercase conversion for emp_name
# emp_department = st.sidebar.text_input('Employee Department')  # No lowercase conversion for emp_department
# emp_role = st.sidebar.text_input('Employee Role')  # No lowercase conversion for emp_role
# emp_joining_date = st.sidebar.text_input('Joining Date (YYYY-MM-DD)')

# # Photo Upload
# st.sidebar.header('Photo Upload')
# uploaded_photo = st.sidebar.file_uploader('Upload Photo', type=['jpg', 'png', 'jpeg'])

# if uploaded_photo is not None:
#     st.sidebar.image(uploaded_photo, caption='Uploaded Photo', use_column_width=True)

# # Check if emp_id is unique
# csv_path = os.path.join('emp_details', 'employee_details.csv')
# if emp_id and os.path.exists(csv_path):
#     with open(csv_path, mode='r', newline='') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         emp_ids = set(row[0] for row in csv_reader)
#         if emp_id in emp_ids:
#             st.sidebar.warning('Employee ID already exists. Please use a unique ID.')

# # Register Button
# if st.sidebar.button('Register'):
#     if emp_id and emp_name and emp_department and emp_role and emp_joining_date and uploaded_photo:
#         # Save employee details to CSV
#         if not os.path.exists(csv_path):
#             with open(csv_path, mode='w', newline='') as csv_file:
#                 csv_writer = csv.writer(csv_file)
#                 csv_writer.writerow(['Employee ID', 'Employee Name', 'Department', 'Role', 'Joining Date'])

#         with open(csv_path, mode='a', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerow([emp_id, emp_name, emp_department, emp_role, emp_joining_date])

#         # Save uploaded photo
#         image_path = os.path.join('emp_images', emp_name, f'{emp_name}.jpg')
#         image_path = image_path.lower()  # Convert to lowercase
#         if not os.path.exists(os.path.dirname(image_path)):
#             os.makedirs(os.path.dirname(image_path))
#         with open(image_path, 'wb') as f:
#             f.write(uploaded_photo.read())

#         st.sidebar.success('Registration successful!')

#         # Clear form for next registration
#         clear_form()

#         # Provide a refresh button
#         if st.sidebar.button('Refresh'):
#             clear_form()

#################################################################################################

# import streamlit as st
# import os
# import csv
# import json
# from datetime import datetime
# import cv2

# # Create necessary folders
# if not os.path.exists('emp_details'):
#     os.makedirs('emp_details')

# if not os.path.exists('emp_images'):
#     os.makedirs('emp_images')

# st.title('Employee Attendance System')

# # Load employee details from JSON file
# json_path = os.path.join('emp_details', 'employee_details.json')
# if os.path.exists(json_path):
#     with open(json_path, 'r') as json_file:
#         employee_details_dict = json.load(json_file)
# else:
#     employee_details_dict = {}

# def clear_form():
#     global emp_id, emp_name, emp_department, emp_role, emp_joining_date, uploaded_photo
#     emp_id = ''
#     emp_name = ''
#     emp_department = ''
#     emp_role = ''
#     emp_joining_date = ''
#     uploaded_photo = None

# # Employee Details
# st.sidebar.header('Employee Details')
# emp_id = st.sidebar.text_input('Employee ID')
# emp_name = st.sidebar.text_input('Employee Name')
# emp_department = st.sidebar.text_input('Employee Department')
# emp_role = st.sidebar.text_input('Employee Role')
# emp_joining_date = st.sidebar.text_input('Joining Date (YYYY-MM-DD)')

# # Photo Upload
# st.sidebar.header('Photo Upload')
# uploaded_photo = st.sidebar.file_uploader('Upload Photo', type=['jpg', 'png', 'jpeg'])

# if uploaded_photo is not None:
#     st.sidebar.image(uploaded_photo, caption='Uploaded Photo', use_column_width=True)

# # Check if emp_id is unique
# csv_path = os.path.join('emp_details', 'employee_details.csv')
# if emp_id and os.path.exists(csv_path):
#     with open(csv_path, mode='r', newline='') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         emp_ids = set(row[0] for row in csv_reader)
#         if emp_id in emp_ids:
#             st.sidebar.warning('Employee ID already exists. Please use a unique ID.')

# # Register Button
# if st.sidebar.button('Register'):
#     if emp_id and emp_name and emp_department and emp_role and emp_joining_date and uploaded_photo:
#         # Save employee details to CSV
#         if not os.path.exists(csv_path):
#             with open(csv_path, mode='w', newline='') as csv_file:
#                 csv_writer = csv.writer(csv_file)
#                 csv_writer.writerow(['Employee ID', 'Employee Name', 'Department', 'Role', 'Joining Date'])

#         with open(csv_path, mode='a', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerow([emp_id, emp_name, emp_department, emp_role, emp_joining_date])

#         # Update employee details in the dictionary
#         employee_details_dict[emp_name] = {
#             'id': emp_id,
#             'department': emp_department,
#             'role': emp_role,
#             'joining_date': emp_joining_date
#         }

#         # Save uploaded photo
#         image_path = os.path.join('emp_images', f'{emp_name}.jpg')
#         image_path = image_path.lower()  # Convert to lowercase
#         with open(image_path, 'wb') as f:
#             f.write(uploaded_photo.read())

#         st.sidebar.success('Registration successful!')

#         # Save employee details to JSON
#         with open(json_path, 'w') as json_file:
#             json.dump(employee_details_dict, json_file, indent=4)

#         # Clear form for next registration
#         clear_form()

#         # Provide a refresh button
#         if st.sidebar.button('Refresh'):
#             clear_form()

# # Display stored employee details
# if st.sidebar.button('Show Employee Details'):
#     st.write("Stored Employee Details:")
#     st.write(employee_details_dict)

import streamlit as st
import os
import csv
import json
from datetime import datetime
import cv2

# Create necessary folders
if not os.path.exists('emp_details'):
    os.makedirs('emp_details')

if not os.path.exists('emp_images'):
    os.makedirs('emp_images')

st.title('Employee Registration Form')

# Load employee details from JSON file
json_path = os.path.join('emp_details', 'employee_details.json')
if os.path.exists(json_path):
    with open(json_path, 'r') as json_file:
        employee_details_dict = json.load(json_file)
else:
    employee_details_dict = {}

def clear_form():
    global emp_id, emp_name, emp_department, emp_role, emp_joining_date, uploaded_photo
    emp_id = ''
    emp_name = ''
    emp_department = ''
    emp_role = ''
    emp_joining_date = ''
    uploaded_photo = None

# Employee Details
st.sidebar.header('Employee Details')
emp_id = st.sidebar.text_input('Employee ID')
emp_name = st.sidebar.text_input('Employee Name')
emp_department = st.sidebar.text_input('Employee Department')
emp_role = st.sidebar.text_input('Employee Role')
emp_joining_date = st.sidebar.text_input('Joining Date (YYYY-MM-DD)')

# Photo Upload
st.sidebar.header('Photo Upload')
uploaded_photo = st.sidebar.file_uploader('Upload Photo', type=['jpg', 'png', 'jpeg'])

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
