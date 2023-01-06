import datetime
import subprocess

# Set the target times and corresponding commands in a dictionary
# Format: {(hour, minute, second): "command"}
commands = {
    (12, 0, 0): "command 1",
    (18, 0, 0): "command 2",
    (22, 0, 0): "command 3"
}

while True:
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Check if the current time matches any of the target times
    for target_time, cmd in commands.items():
        if (current_time.hour, current_time.minute, current_time.second) == target_time:
            # Run the command in CMD
            subprocess.run(cmd, shell=True)
            # Leave the target time and command in the dictionary
            break
