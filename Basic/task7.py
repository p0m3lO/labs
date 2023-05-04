import subprocess
import sys
import os
import time

def check_cron_job_exists(command):
    try:
        result = subprocess.run(["crontab", "-l"], stdout=subprocess.PIPE, text=True)
        return command in result.stdout
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    command = "*/2 * * * * date >> /tmp/timestamps.txt"
    file_path = "/tmp/timestamps.txt"

    if check_cron_job_exists(command):
        print("The cron job is configured correctly.")
        print("Waiting for 65 seconds to check if the cron job is running...")
        time.sleep(125)

        if os.path.exists(file_path):
            print("The cron job is running and appending to the file.")
        else:
            print("The cron job is NOT running or appending to the file.")
            sys.exit(1)
    else:
        print("The cron job is NOT configured correctly.")
        sys.exit(1)