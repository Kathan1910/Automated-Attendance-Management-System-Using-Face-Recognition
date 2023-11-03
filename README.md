# Automated Attendance Management System

## Project Summary

The Automated Attendance Management System is a comprehensive solution for efficient attendance tracking in organizations. Leveraging Python with a variety of libraries including OpenCV, face_recognition, pandas, Matplotlib, FPDF, and smtplib, this system automates the process of capturing daily attendance using a webcam, storing it in a CSV file, generating detailed reports, and sending these reports via email. Below are the key features and project flow:

## Key Features

### Face Recognition
- The system utilizes OpenCV and face_recognition libraries for real-time face recognition.

### Attendance Tracking
- Attendance is tracked by matching recognized faces with known employees, and the data is stored in a CSV file.

### Employee Details
- Employee details such as department and role can be conveniently stored in a JSON file and associated with attendance records.

### Automatic Reporting
- The system generates daily attendance reports, including a bar chart representation of attendance, and saves them as PDF files.

### Email Integration
- Daily attendance reports are automatically sent via email to a specified recipient, streamlining the distribution process.

### Web Interface (Optional)
- The project can be extended with a web interface using Streamlit, providing a user-friendly platform for manual report requests and configuration adjustments.

### Auto Report Generation (Optional)
- An additional script can be scheduled to run daily, automating the report generation and email dispatch process.

## Project Flow

1. **Face Recognition:** The system captures faces using a webcam and recognizes employees in real-time.

2. **Attendance Tracking:** Recognized faces are matched with known employees, and their attendance is recorded in a CSV file.

3. **Daily Report Generation:** A daily attendance report is generated, complete with a bar chart illustrating attendance statistics.

4. **Report Storage:** The report is saved as a PDF file for archival and reference purposes.

5. **Email Dispatch:** Optionally, the system can send the daily attendance report via email to a designated recipient for review.

6. **Web Interface (Optional):** Users can interact with the system through a web interface built using Streamlit, enabling manual report requests and configuration changes.

7. **Auto Report Generation (Optional):** An automated script runs daily to simplify the process of generating and emailing daily reports, ensuring timely delivery.

This Automated Attendance Management System is designed to enhance efficiency and accuracy in attendance tracking, making it a valuable addition to any organization.




# Project Completion Report

## Project Title: Automated Attendance Management System

### Project Overview

The Automated Attendance Management System was created to streamline employee attendance tracking using facial recognition technology. Its primary goals were to provide accurate attendance records, generate daily reports, and automate report distribution via email.

### Project Phases

**Phase 1: Face Recognition and Attendance Tracking**
- Implemented face recognition using OpenCV and face_recognition libraries.
- Managed known employee details in a JSON file, including department and role.
- Successfully tracked attendance, recording employee names, departments, roles, and timestamps.

**Phase 2: Reporting and Emailing**
- Generated daily attendance reports in PDF format.
- Configured email settings for report distribution.
- Implemented auto-report generation, scheduled to run daily at 8:00 AM (optional).

**Phase 3: Web Interface (Optional)**
- Created a Streamlit-based web interface for user interaction.
- Included options for manual report generation, viewing, and configuration settings.
- Enabled users to request daily attendance reports by selecting a specific date.

### Project Completion Criteria

- The face recognition system accurately identified known employees.
- Attendance data was recorded and stored in CSV files with timestamps.
- Daily attendance reports were generated and included bar charts.
- Reports were sent via email to the specified recipient.
- The web interface allowed manual report generation and configuration.
- The auto-report generation script ran daily without errors (optional).

### Deliverables

- Python scripts for face recognition, attendance tracking, and report generation.
- CSV files containing recorded attendance data.
- PDF reports with daily attendance and optional charts.
- A functional web interface (if applicable).
- Documentation and instructions for setting up and configuring the system.

### Challenges and Solutions

- **Challenge:** Implementing automated report generation.
  - **Solution:** Utilized the schedule library to schedule daily report generation.

### Project Timeline

- **Phase 1:** 1 weeks
- **Phase 2:** 1 weeks
- **Phase 3 (Optional):** 2 weeks (depending on complexity)

### Conclusion

The Automated Attendance Management System has been successfully completed, meeting all project objectives. It now provides an efficient solution for attendance tracking and reporting, enhancing overall productivity.

### Lessons Learned

- Implementation of automation for daily tasks can significantly improve efficiency.
- Proper planning and documentation are crucial for project success.

### Recommendations

- Explore additional features such as monthly and weekly reports.
- Consider adding visualization tools to enhance reporting.

### Acknowledgments

- We acknowledge the contributions of the project team, including [Your Name], Team Member Names, and [Stakeholders].
- Special thanks to [Any external parties or consultants] for their support and guidance.

### Documentation and Instructions

- For setup and usage instructions, please refer to the provided documentation.

### Appendices

- [Include any additional materials or resources related to the project.]

### Project Sign-off

This project completion report has been reviewed and approved by the project stakeholders.

### Date of Completion

[Date of Project Completion]

### Project Team

- [Kathan Patel]: Project Manager

### Contact Information

- For inquiries or support, please contact [9974701017].