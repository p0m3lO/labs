import subprocess
import sys
import os
import time
import re
import chardet

def check_cron_job_exists():
    try:
        result = subprocess.run(["crontab", "-l"], stdout=subprocess.PIPE, text=True)
        match = re.search(r'\*/2 \* \* \* \*', result.stdout)
        return match is not None
    except subprocess.CalledProcessError:
        return False

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def check_file_content(file_path):
    if not os.path.exists(file_path):
        return False

    encoding = detect_encoding(file_path)

    with open(file_path, 'r', encoding=encoding) as f:
        lines = f.readlines()

    if not lines:
        return False

    last_line = lines[-1].strip()

    # Check if the last line in the file contains a timestamp
    match = re.search(r'(\w{3}\s\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}:\d{2}\s(?:AM|PM)\sUTC|\d{4}.\s\w+.\s\d{2}.,\s\w+,\s\d{2}:\d{2}:\d{2}\sUTC)', last_line)
    return match is not None

if __name__ == "__main__":
    file_path = "/tmp/timestamps.txt"

    if check_cron_job_exists():
        print("The cron job is configured correctly.")
        time.sleep(5)

        if check_file_content(file_path):
            print("The cron job is running and appending to the file.")
        else:
            print("The cron job is NOT running or appending to the file.")
            sys.exit(1)
    else:
        print("The cron job is NOT configured correctly.")
        sys.exit(1)

