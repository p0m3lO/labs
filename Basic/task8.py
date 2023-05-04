import os
import sys
import subprocess
from datetime import datetime, timedelta

def check_find_logs(target_directory, size, days):
    try:
        output = subprocess.run(
            ["sudo", "find", target_directory, "-type", "f", "-iname", "*.log", "-mtime", f"-{days}", "-size", f"+{size}k"],
            check=True,
            stdout=subprocess.PIPE,
            text=True
        )
        log_files = output.stdout.strip().split('\n')
        if log_files == ['']:
            log_files = []
        return set(log_files)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def read_find_output(output_file):
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
        log_files = [line.strip() for line in lines]
        return set(log_files)
    except FileNotFoundError:
        print(f"Error: Output file '{output_file}' not found.")
        return None

def check_second_output(output_file):
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            if not line.startswith("found directory: ./") or not line.strip().endswith(")"):
                return False
        return True
    except FileNotFoundError:
        print(f"Error: Output file '{output_file}' not found.")
        return False


if __name__ == "__main__":
    target_directory = "/var/log"
    size = 10
    days = 7
    log_output_file = "/tmp/first_output.log"
    dir_output_file = "/tmp/second_output.log"

    expected_log_files = check_find_logs(target_directory, size, days)
    find_log_files = read_find_output(log_output_file)

    if expected_log_files is not None and find_log_files is not None:
        if expected_log_files == find_log_files:
            print("The first output file matches the expected log files.")
        else:
            print("The first output file does NOT match the expected log files.")
            sys.exit(1)
    else:
        print("An error occurred while checking the first output file.")
        sys.exit(1)
    
    if check_second_output(dir_output_file):
        print("The second output file has the expected content.")
    else:
        print("The second output file does NOT have the expected content.")
        sys.exit(1)
