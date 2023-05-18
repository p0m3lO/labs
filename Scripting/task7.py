import subprocess
import sys

# Check if the bash script is running
def check_script_running():
    process = subprocess.run(["pgrep", "-f", "system_monitor.sh"], capture_output=True, text=True)
    return process.returncode == 0

# Check the latest log entry
def check_latest_log_entry():
    with open("/tmp/system_monitor.log", "r") as log_file:
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