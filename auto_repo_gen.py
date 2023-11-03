# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from fpdf import FPDF  # Library for creating PDFs
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# import schedule
# import time
# import datetime

# # Function to generate the daily report
# def generate_daily_report():
#     try:
#         # Get the current date
#         today = datetime.datetime.now().strftime('%Y-%m-%d')

#         # Load attendance data from the CSV file
#         attendance_csv_path = os.path.join('attendance', f'attendance_{today}.csv')
#         if not os.path.exists(attendance_csv_path):
#             print(f"Attendance data file '{attendance_csv_path}' not found.")
#             return

#         df = pd.read_csv(attendance_csv_path)

#         # Generate a PDF report
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)

#         # Add a title to the PDF
#         pdf.cell(200, 10, txt="Daily Attendance Report", ln=True, align="C")

#         # Create a table for attendance data
#         pdf.set_fill_color(200, 220, 255)  # Set table cell fill color
#         pdf.cell(40, 10, "Name", 1, 0, "C", 1)
#         pdf.cell(40, 10, "Department", 1, 0, "C", 1)
#         pdf.cell(40, 10, "Role", 1, 0, "C", 1)
#         pdf.cell(40, 10, "Timestamp", 1, 1, "C", 1)

#         for index, row in df.iterrows():
#             name = row['Name']
#             department = row['Department']
#             role = row['Role']
#             timestamp = row['Timestamp']
#             pdf.cell(40, 10, name, 1)
#             pdf.cell(40, 10, department, 1)
#             pdf.cell(40, 10, role, 1)
#             pdf.cell(40, 10, timestamp, 1)
#             pdf.ln()

#         # Save the PDF report
#         report_file_path = os.path.join('reports', f'daily_report_{today}.pdf')
#         pdf.output(report_file_path)

#         # Send the report via email
#         send_report_email(report_file_path)

#     except Exception as e:
#         print(f"An error occurred while generating the daily report: {str(e)}")

# # Function to send the report via email
# def send_report_email(report_file_path):
#     try:
#         # Configure email settings
#         email_host = 'smtp.gmail.com'
#         email_port = 587
#         email_user = 'kathanpatel1910@gmail.com'
#         email_password = 'myavezkzegzpolff'
#         recipient_email = 'kp@radhyats.com'

#         # Create an email message
#         msg = MIMEMultipart()
#         msg['From'] = email_user
#         msg['To'] = recipient_email
#         msg['Subject'] = 'Daily Attendance Report'

#         # Add email body text (optional)
#         msg.attach(MIMEText('Please find the attached daily attendance report.'))

#         # Attach the report file
#         with open(report_file_path, 'rb') as report_file:
#             attach = MIMEApplication(report_file.read(), _subtype="pdf")
#         attach.add_header('Content-Disposition', 'attachment', filename=str(report_file_path))
#         msg.attach(attach)

#         # Send the email
#         server = smtplib.SMTP(email_host, email_port)
#         server.starttls()
#         server.login(email_user, email_password)
#         server.sendmail(email_user, recipient_email, msg.as_string())
#         server.quit()
#         print(f"Report sent to {recipient_email}")

#     except Exception as e:
#         print(f"An error occurred while sending the email: {str(e)}")

# # Schedule the script to run daily at a specific time (e.g., 8:00 AM)
# schedule.every().day.at("15:16").do(generate_daily_report)

# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Sleep for 60 seconds before checking the schedule again




import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import schedule
import time
import datetime

# Function to generate the daily report with a graph
def generate_daily_report():
    try:
        # Get the current date
        today = datetime.datetime.now().strftime('%Y-%m-%d')

        # Load attendance data from the CSV file
        attendance_csv_path = os.path.join('attendance', f'attendance_{today}.csv')
        if not os.path.exists(attendance_csv_path):
            print(f"Attendance data file '{attendance_csv_path}' not found.")
            return

        df = pd.read_csv(attendance_csv_path)

        # Create a bar chart of daily attendance
        fig, ax = plt.subplots()
        df['Name'].value_counts().plot(kind='bar', ax=ax)
        plt.title('Daily Attendance')
        plt.xlabel('Name')
        plt.ylabel('Count')
        plt.xticks(rotation=45)

        # Save the chart as an image
        chart_image_path = os.path.join('reports', f'daily_chart_{today}.png')
        plt.savefig(chart_image_path, bbox_inches='tight')
        plt.close()

        # Generate a PDF report
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add a title to the PDF
        pdf.cell(200, 10, txt="Daily Attendance Report", ln=True, align="C")

        # Insert the chart image into the PDF
        pdf.image(chart_image_path, x=10, w=190)

        # Add a section for attendance data (similar to previous code)
        pdf.set_fill_color(200, 220, 255)  # Set table cell fill color
        pdf.cell(40, 10, "Name", 1, 0, "C", 1)
        pdf.cell(40, 10, "Department", 1, 0, "C", 1)
        pdf.cell(40, 10, "Role", 1, 0, "C", 1)
        pdf.cell(40, 10, "Timestamp", 1, 1, "C", 1)

        for index, row in df.iterrows():
            name = row['Name']
            department = row['Department']
            role = row['Role']
            timestamp = row['Timestamp']
            pdf.cell(40, 10, name, 1)
            pdf.cell(40, 10, department, 1)
            pdf.cell(40, 10, role, 1)
            pdf.cell(40, 10, timestamp, 1)
            pdf.ln()

        # Save the PDF report
        report_file_path = os.path.join('reports', f'daily_report_{today}.pdf')
        pdf.output(report_file_path)

        # Send the report via email
        send_report_email(report_file_path)

    except Exception as e:
        print(f"An error occurred while generating the daily report: {str(e)}")

# Function to send the report via email (similar to previous code)
def send_report_email(report_file_path):
    try:
        # Configure email settings
        email_host = 'smtp.gmail.com'
        email_port = 587
        email_user = 'kathanpatel1910@gmail.com'
        email_password = 'myavezkzegzpolff'
        recipient_email = 'kp5640907@gmail.com'

        # Create an email message
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = recipient_email
        msg['Subject'] = 'Daily Attendance Report'

        # Add email body text (optional)
        msg.attach(MIMEText('Please find the attached daily attendance report.'))

        # Attach the report file
        with open(report_file_path, 'rb') as report_file:
            attach = MIMEApplication(report_file.read(), _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment', filename=str(report_file_path))
        msg.attach(attach)

        # Send the email
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, recipient_email, msg.as_string())
        server.quit()
        print(f"Report sent to {recipient_email}")

    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

# Schedule the script to run daily at a specific time (e.g., 8:00 AM)
schedule.every().day.at("15:32").do(generate_daily_report)

while True:
    schedule.run_pending()
    time.sleep(60)
