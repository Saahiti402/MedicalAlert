# Medical Alert System Using Kestra

## Overview

This project implements a **Medical Alert System** designed to monitor continuous glucose monitoring (CGM) values and send alerts during emergencies. It utilizes **Kestra**, a powerful workflow orchestration platform, to automate the alerting process. The system ensures timely intervention by notifying emergency contacts if the user does not respond within a given time frame.

## Key Features

1. **Real-Time CGM Monitoring**: 
   - The system generates simulated CGM values to mimic real-world scenarios.
   - If the CGM value exceeds a threshold (e.g., 200), the system initiates the alert process.

2. **Alert Notification**:
   - When abnormal values are detected, an alert message is sent to the user via SMS.
   - Utilizes the **Twilio API** to send alerts.

3. **User Response Timeout**:
   - The user has 5 minutes to respond to the alert.
   - If the user acknowledges the alert within the time frame, the process stops.

4. **Emergency Contact Notification**:
   - If the user fails to respond within 5 minutes, the system automatically notifies emergency contacts.

5. **Dynamic Task Execution**:
   - Utilizes Kestra's **Pause** and **Conditional Workflow Execution** to handle user input and automate decision-making based on responses.

## Workflow Structure

1. **CGM Value Monitoring**:
   - `monitor_cgm.py` generates random CGM values.
   - If the value exceeds 200, the workflow proceeds to alert the user.

2. **User Alert and Response**:
   - `main.py` sends an SMS alert to the user.
   - The workflow pauses for 5 minutes to wait for the user's input via `value.py`.

3. **Conditional Actions**:
   - If the user responds, a confirmation log is recorded.
   - If no response is received, the system sends an alert to emergency contacts.

## Technologies Used

- **Kestra**: Workflow orchestration and automation.
- **Python**: Backend logic and scripting.
- **Twilio API**: SMS notifications.
- **Docker**: Task containerization for seamless execution.

## Project Structure
├── monitor_cgm.py       # Simulates CGM value generation.

├── main.py              # Sends SMS alerts using Twilio.

├── value.py             # Simulates user response to alerts.

├── README.md            # Project documentation.

├── Dockerfile           # Docker configuration for running tasks.

└── kestra.yml           # Kestra workflow definition.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Saahiti402/MedicalAlert.git
   cd MedicalAlert
2. **Set Up Dependencies**:
Ensure Docker and Kestra are installed.
3.**Configure Environment Variables**:

- Create a `.env` file with your Twilio credentials:
  TWILIO_ACCOUNT_SID=your_account_sid
  TWILIO_AUTH_TOKEN=your_auth_token
  TWILIO_PHONE_NUMBER=your_twilio_number
  USER_PHONE_NUMBER=user_phone_number
4.**Run the Workflow**:
Deploy the Kestra workflow:
kestra-cli start --namespace medical.alert --id alert-system

## Usage

1. The system monitors CGM values in real-time.
2. If a critical value is detected, the user receives an SMS alert.
3. The user must respond within 5 minutes. If they fail, the system escalates the alert to emergency contacts.


## Future Enhancements

- Integration with real CGM devices.
- Dashboard for visualizing CGM data trends.
- Machine learning models to predict abnormal CGM patterns.

## Screenshots and videos
<img src="/picture.jpg" width="50%" height="80">
![Medical Alert System alert](/picture.jpg)

