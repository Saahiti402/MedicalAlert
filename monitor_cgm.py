import random
import time
import sys

# Define the threshold CGM value
threshold = 200

# Simulated function to get CGM value
def get_cgm_value():
    # Replace this with the actual API request to get the CGM value from your device
    return random.randint(100, 250)

# Continuous monitoring loop
while True:
    cgm_value = get_cgm_value()
    print(f"Current CGM Value: {cgm_value}")
    sys.stdout.flush()

    # Check if CGM value exceeds the threshold
    if cgm_value > threshold:
        print(f"ALERT! CGM value {cgm_value} exceeds threshold of {threshold}. Exiting script.")
        sys.exit(0)  # Exit the script with a success status

    # Sleep for a while before checking again (e.g., every 10 seconds)
    time.sleep(10)
