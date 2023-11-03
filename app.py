# import streamlit as st
# import pandas as pd
# import os
# import datetime

# # Function to generate the daily report
# def generate_daily_report(date):
#     try:
#         # Generate the attendance file path based on the selected date and directory
#         attendance_csv_path = os.path.join('attendance', f'attendance_{date}.csv')

#         # Check if the attendance file exists
#         if not os.path.exists(attendance_csv_path):
#             st.error(f"Attendance data file '{attendance_csv_path}' not found for the selected date. Please make sure it exists.")
#             return

#         # Load attendance data from the CSV file
#         df = pd.read_csv(attendance_csv_path)

#         # Generate and display the daily report
#         st.subheader(f"Attendance Report for {date}")
#         st.write(df)

#         # Create the "reports" directory if it doesn't exist
#         if not os.path.exists('reports'):
#             os.makedirs('reports')

#         # Add a button to generate the report
#         if st.button("Generate Report"):
#             # Export the report to a CSV file within the "reports" directory
#             report_csv_path = os.path.join('reports', f'daily_report_{date}.csv')
#             df.to_csv(report_csv_path, index=False)
#             st.success(f"Report exported to {report_csv_path}")

#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")

# def main():
#     st.title("Attendance System")

#     # List available dates based on files in the "attendance" directory
#     available_dates = [f.split('_')[1].split('.')[0] for f in os.listdir('attendance') if f.startswith('attendance_')]

#     # Add a date selection widget
#     selected_date = st.selectbox("Select a Date", available_dates)

#     # Display attendance data for the selected date
#     try:
#         generate_daily_report(selected_date)
#     except ValueError:
#         st.warning("Please select a date to view the attendance report.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.title("Attendance System")

    # List available dates based on files in the "attendance" directory
    available_dates = [f.split('_')[1].split('.')[0] for f in os.listdir('attendance') if f.startswith('attendance_')]

    # Add a date selection widget
    selected_date = st.selectbox("Select a Date", available_dates)

    # Add options for generating different types of reports
    report_type = st.selectbox("Select Report Type", ["Daily", "Weekly", "Monthly"])

    # Display attendance data or generate reports based on user selection
    if st.button("Generate Report"):
        generate_report(selected_date, report_type)

if __name__ == "__main__":
    main()