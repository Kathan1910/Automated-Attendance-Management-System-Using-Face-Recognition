# import cv2
# import face_recognition
# import os

# # Load known faces
# known_face_encodings = []
# known_face_names = []

# # Load your known images and encode them
# known_image_path = 'E:\END TO END PROJECTS\Radhya Software Solutions\Final Project\emp_images'
# for filename in os.listdir(known_image_path):
#     image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
#     face_encoding = face_recognition.face_encodings(image)[0]
#     known_face_encodings.append(face_encoding)
#     known_face_names.append(os.path.splitext(filename)[0])  # Use filename without extension as name

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find all face locations and encodings in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Loop through each detected face
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"  # Default name

#         # If a match is found, use the name of the known face
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#         # Draw a rectangle around the face and label it with the name
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()


# import cv2
# import face_recognition
# import os
# import json

# # Load known faces
# known_face_encodings = []
# known_face_names = []
# known_face_departments = {}
# known_face_roles = {}

# # Load your known images and encode them
# known_image_path = 'emp_images'
# for filename in os.listdir(known_image_path):
#     image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
#     face_encoding = face_recognition.face_encodings(image)[0]
#     employee_name = os.path.splitext(filename)[0].lower()  # Convert to lowercase
#     known_face_encodings.append(face_encoding)
#     known_face_names.append(employee_name)

#     # Retrieve employee details from JSON
#     with open('emp_details/employee_details.json', 'r') as json_file:
#         employee_details = json.load(json_file)
#         if employee_name in employee_details:
#             known_face_departments[employee_name] = employee_details[employee_name]['department']
#             known_face_roles[employee_name] = employee_details[employee_name]['role']

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find all face locations and encodings in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Loop through each detected face
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"  # Default name
#         department = "Unknown Department"
#         role = "Unknown Role"

#         # If a match is found, use the name of the known face
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]
#             department = known_face_departments.get(name, "Unknown Department")
#             role = known_face_roles.get(name, "Unknown Role")

#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green square
        
#         # Display the name, department, and role below the box with new lines
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text = f'Name: {name}\nDepartment: {department}\nRole: {role}'
#         text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
#         text_lines = text.split('\n')
#         line_height = text_size[1] + 5
#         for i, line in enumerate(text_lines):
#             cv2.putText(frame, line, (left + 6, bottom + (i+1)*line_height), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()

#############################################################################################

# import cv2
# import face_recognition
# import os
# import json

# # Load known faces
# known_face_encodings = []
# known_face_names = []

# # Load your known images and encode them
# known_image_path = 'emp_images'
# for filename in os.listdir(known_image_path):
#     image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
#     face_encoding = face_recognition.face_encodings(image)[0]
#     employee_name = os.path.splitext(filename)[0].lower()  # Convert to lowercase
#     known_face_encodings.append(face_encoding)
#     known_face_names.append(employee_name)

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find all face locations and encodings in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Loop through each detected face
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"  # Default name

#         # If a match is found, use the name of the known face
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green square

#         # Initialize department and role as "Unknown"
#         department = "Unknown"
#         role = "Unknown"

#         # Load employee details from JSON file based on the name
#         json_path = 'emp_details/employee_details.json'
#         if os.path.exists(json_path):
#             with open(json_path, 'r') as json_file:
#                 employee_details_dict = json.load(json_file)
#                 if name in employee_details_dict:
#                     department = employee_details_dict[name]['department']
#                     role = employee_details_dict[name]['role']

#         # Display the name, department, and role below the box with new lines
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text = f'Name: {name}\nDepartment: {department}\nRole: {role}'
#         text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
#         text_lines = text.split('\n')
#         line_height = text_size[1] + 5
#         for i, line in enumerate(text_lines):
#             cv2.putText(frame, line, (left + 6, bottom + (i + 1) * line_height), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()

#########################################################################################

# import cv2
# import face_recognition
# import os
# import json
# import csv
# import datetime

# # Load known faces
# known_face_encodings = []
# known_face_names = []

# # Load your known images and encode them
# known_image_path = 'emp_images'
# for filename in os.listdir(known_image_path):
#     image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
#     face_encoding = face_recognition.face_encodings(image)[0]
#     employee_name = os.path.splitext(filename)[0].lower()  # Convert to lowercase
#     known_face_encodings.append(face_encoding)
#     known_face_names.append(employee_name)

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# # Initialize attendance data
# attendance_data = {}

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find all face locations and encodings in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Get current date and time
#     current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     # Loop through each detected face
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"  # Default name

#         # If a match is found, use the name of the known face
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#         # Initialize department and role as "Unknown"
#         department = "Unknown"
#         role = "Unknown"

#         # Load employee details from JSON file based on the name
#         json_path = 'emp_details/employee_details.json'
#         if os.path.exists(json_path):
#             with open(json_path, 'r') as json_file:
#                 employee_details_dict = json.load(json_file)
#                 if name in employee_details_dict:
#                     department = employee_details_dict[name]['department']
#                     role = employee_details_dict[name]['role']

#         # Capture attendance if not already marked for today
#         if name != "Unknown" and name not in attendance_data:
#             attendance_data[name] = {
#                 'department': department,
#                 'role': role,
#                 'timestamps': [current_datetime],
#             }
#         elif name != "Unknown" and current_datetime not in attendance_data[name]['timestamps']:
#             attendance_data[name]['timestamps'].append(current_datetime)

#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green square

#         # Display the name, department, role, and timestamp below the box with new lines
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text = f'Name: {name}\nDepartment: {department}\nRole: {role}\nTimestamp: {current_datetime}'
#         text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
#         text_lines = text.split('\n')
#         line_height = text_size[1] + 5
#         for i, line in enumerate(text_lines):
#             cv2.putText(frame, line, (left + 6, bottom + (i + 1) * line_height), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()

# # Save attendance to a single CSV file named with the current date
# attendance_directory = 'attendance'
# if not os.path.exists(attendance_directory):
#     os.makedirs(attendance_directory)

# current_date = datetime.datetime.now().strftime('%Y-%m-%d')
# csv_file_path = os.path.join(attendance_directory, f'attendance_{current_date}.csv')
# with open(csv_file_path, mode='w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Name', 'Department', 'Role', 'Timestamp'])
#     for employee_name, data in attendance_data.items():
#         department = data['department']
#         role = data['role']
#         timestamps = data['timestamps']
#         for timestamp in timestamps:
#             csv_writer.writerow([employee_name, department, role, timestamp])

################################################################################################

# import cv2
# import face_recognition
# import os
# import json
# import csv
# import datetime

# # Load known faces
# known_face_encodings = []
# known_face_names = []

# # Load your known images and encode them
# known_image_path = 'emp_images'
# for filename in os.listdir(known_image_path):
#     image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
#     face_encoding = face_recognition.face_encodings(image)[0]
#     employee_name = os.path.splitext(filename)[0].lower()  # Convert to lowercase
#     known_face_encodings.append(face_encoding)
#     known_face_names.append(employee_name)

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

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find all face locations and encodings in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Get current date and time
#     current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     # Loop through each detected face
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"  # Default name

#         # If a match is found, use the name of the known face
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#             # Initialize department and role as "Unknown"
#             department = "Unknown"
#             role = "Unknown"

#             # Load employee details from JSON file based on the name
#             json_path = 'emp_details/employee_details.json'
#             if os.path.exists(json_path):
#                 with open(json_path, 'r') as json_file:
#                     employee_details_dict = json.load(json_file)
#                     if name in employee_details_dict:
#                         department = employee_details_dict[name]['department']
#                         role = employee_details_dict[name]['role']

#             # Capture attendance if not already recorded for today and not in the existing attendance data
#             if name != "Unknown" and name not in attendance_data:
#                 attendance_data[name] = {
#                     'department': department,
#                     'role': role,
#                     'timestamp': current_datetime,
#                 }

#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green square

#         # Display the name, department, role, and timestamp below the box with new lines
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text = f'Name: {name}\nDepartment: {department}\nRole: {role}\nTimestamp: {current_datetime}'
#         text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
#         text_lines = text.split('\n')
#         line_height = text_size[1] + 5
#         for i, line in enumerate(text_lines):
#             cv2.putText(frame, line, (left + 6, bottom + (i + 1) * line_height), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()

# # Save the updated attendance data to the CSV file
# with open(csv_file_path, mode='w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Name', 'Department', 'Role', 'Timestamp'])
#     for employee_name, data in attendance_data.items():
#         department = data['department']
#         role = data['role']
#         timestamp = data['timestamp']
#         csv_writer.writerow([employee_name, department, role, timestamp])

## Working Perfectly Fine


# import cv2
# import face_recognition
# import os
# import json
# import csv
# import datetime
# import time

# # Load known faces
# known_face_encodings = []
# known_face_names = []

# # Load your known images and encode them
# known_image_path = 'emp_images'
# for filename in os.listdir(known_image_path):
#     image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
#     face_encoding = face_recognition.face_encodings(image)[0]
#     employee_name = os.path.splitext(filename)[0].lower()  # Convert to lowercase
#     known_face_encodings.append(face_encoding)
#     known_face_names.append(employee_name)

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

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find all face locations and encodings in the current frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Get current date and time
#     current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     # Loop through each detected face
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"  # Default name

#         # If a match is found, use the name of the known face
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#             # Initialize department and role as "Unknown"
#             department = "Unknown"
#             role = "Unknown"

#             # Load employee details from JSON file based on the name
#             json_path = 'emp_details/employee_details.json'
#             if os.path.exists(json_path):
#                 with open(json_path, 'r') as json_file:
#                     employee_details_dict = json.load(json_file)
#                     if name in employee_details_dict:
#                         department = employee_details_dict[name]['department']
#                         role = employee_details_dict[name]['role']

#             # Capture attendance if not already recorded for today and not in the existing attendance data
#             if name != "Unknown" and name not in attendance_data:
#                 attendance_data[name] = {
#                     'department': department,
#                     'role': role,
#                     'timestamp': current_datetime,
#                 }

#     # Automatically save the updated attendance every update_interval seconds
#     if time.time() - last_update_time >= update_interval:
#         with open(csv_file_path, mode='w', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerow(['Name', 'Department', 'Role', 'Timestamp'])
#             for employee_name, data in attendance_data.items():
#                 department = data['department']
#                 role = data['role']
#                 timestamp = data['timestamp']
#                 csv_writer.writerow([employee_name, department, role, timestamp])
#         last_update_time = time.time()

#     # Draw rectangles and display the resulting frame
#     for (top, right, bottom, left), name in zip(face_locations, known_face_names):
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green square
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text = f'Name: {name}\nDepartment: {department}\nRole: {role}\nTimestamp: {current_datetime}'
#         text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
#         text_lines = text.split('\n')
#         line_height = text_size[1] + 5
#         for i, line in enumerate(text_lines):
#             cv2.putText(frame, line, (left + 6, bottom + (i + 1) * line_height), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()

######################################################################

import cv2
import face_recognition
import os
import json
import csv
import datetime
import time

# Load known faces
known_face_encodings = []
known_face_names = []

# Load your known images and encode them
known_image_path = 'emp_images'
for filename in os.listdir(known_image_path):
    image = face_recognition.load_image_file(os.path.join(known_image_path, filename))
    face_encoding = face_recognition.face_encodings(image)[0]
    employee_name = os.path.splitext(filename)[0].lower()  # Convert to lowercase
    known_face_encodings.append(face_encoding)
    known_face_names.append(employee_name)

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Initialize attendance data
attendance_data = {}

# Load existing attendance data from a CSV file
attendance_directory = 'attendance'
if not os.path.exists(attendance_directory):
    os.makedirs(attendance_directory)

current_date = datetime.datetime.now().strftime('%Y-%m-%d')
csv_file_path = os.path.join(attendance_directory, f'attendance_{current_date}.csv')

if os.path.exists(csv_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            employee_name, department, role, timestamp = row
            attendance_data[employee_name] = {
                'department': department,
                'role': role,
                'timestamp': timestamp,
            }

# Set the update interval in seconds
update_interval = 60  # Update every minute

last_update_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Get current date and time
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')  # 12-hour clock format

    # Loop through each detected face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"  # Default name

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # Initialize department and role as "Unknown"
            department = "Unknown"
            role = "Unknown"

            # Load employee details from JSON file based on the name
            json_path = 'emp_details/employee_details.json'
            if os.path.exists(json_path):
                with open(json_path, 'r') as json_file:
                    employee_details_dict = json.load(json_file)
                    if name in employee_details_dict:
                        department = employee_details_dict[name]['department']
                        role = employee_details_dict[name]['role']

            # Capture attendance if not already recorded for today and not in the existing attendance data
            if name != "Unknown" and name not in attendance_data:
                attendance_data[name] = {
                    'department': department,
                    'role': role,
                    'timestamp': current_datetime,
                }

    # Automatically save the updated attendance every update_interval seconds
    if time.time() - last_update_time >= update_interval:
        with open(csv_file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Department', 'Role', 'Timestamp'])
            for employee_name, data in attendance_data.items():
                department = data['department']
                role = data['role']
                timestamp = data['timestamp']
                csv_writer.writerow([employee_name, department, role, timestamp])
        last_update_time = time.time()

    # Draw rectangles and display the resulting frame
    for (top, right, bottom, left), name in zip(face_locations, known_face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Green square
        font = cv2.FONT_HERSHEY_DUPLEX
        text = f'Name: {name}\nDepartment: {department}\nRole: {role}\nTimestamp: {current_datetime}'
        text_size = cv2.getTextSize(text, font, 0.5, 1)[0]
        text_lines = text.split('\n')
        line_height = text_size[1] + 5
        for i, line in enumerate(text_lines):
            cv2.putText(frame, line, (left + 6, bottom + (i + 1) * line_height), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
