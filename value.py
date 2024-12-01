import random
import sys

# List of possible messages
messages = ["Need help", "I'm fine"]

# Generate a random message
message = random.choice(messages)

# Print the generated message
print(message)

# Exit with code 0 if "I'm fine", else exit with code 1
if message == "I'm fine":
    sys.exit(0)
else:
    sys.exit(1)
