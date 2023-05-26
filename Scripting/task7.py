import subprocess
import sys
import os

# Check if the bash script is running
def check_script_running():
    process = subprocess.run(['pgrep', '-f', '(^|/|./)system_monitor.sh($|\s)'], capture_output=True, text=True)
    return len(process.stdout.strip()) > 0

# Check the latest log entry
def check_latest_log_entry():
    if not os.path.isfile("/tmp/system.log"):
        print("Log file not found.")
        sys.exit(1)

    with open("/tmp/system.log", "r") as log_file:
        lines = log_file.readlines()
        if lines:
            return lines[-1].strip()
        else:
            return "No log entries found"
            sys.exit(1)

# Main function to check the script and log
def main():
    if check_script_running():
        print("The script is running.")
        latest_log_entry = check_latest_log_entry()
        print("Latest log entry:", latest_log_entry)
    else:
        print("The script is not running.")
        sys.exit(1)

# Run the main function
if __name__ == "__main__":
    main()