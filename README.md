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
