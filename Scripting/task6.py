import os
import sys
import subprocess

def check_scp_script():
    user_home_dir = os.path.expanduser("~")
    script_path = os.path.expanduser("~/scripts/remote_copy.sh")

    # Check if the script exists
    if not os.path.isfile(script_path):
        print("The scp script does not exist.")
        return False

    # Check if the script is executable
    if not os.access(script_path, os.X_OK):
        print("The scp script is not executable.")
        return False

    # Run the script and check if it completes without errors
    result = subprocess.run([script_path, '-a', '7', '-s', '10k'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"The scp script returned an error: {result.stderr.decode('utf-8')}")
        return False

    # Check if the remote_logs directory exists and contains files
    remote_logs_dir = os.path.expanduser("~/remote_logs")
    if not os.path.isdir(remote_logs_dir) or not os.listdir(remote_logs_dir):
        print("The remote_logs directory does not exist or is empty.")
        return False

    # SSH into the other server and issue the find command
    find_command = ["ssh", "gde-server", "sudo find /var/log -name '*.log' -mtime 7 -size +10k"]
    result = subprocess.run(find_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the list of files found by the find command
    found_files = [f for f in result.stdout.decode('utf-8').split('\n') if f]

    # Check each file in found_files exists in remote_logs_dir
    for file in found_files:
        local_file_path = os.path.join(remote_logs_dir, os.path.basename(file))
        if not os.path.isfile(local_file_path):
            print(f"The file {file} was not copied to the local machine.")
            return False

    return True

if __name__ == "__main__":
    if not check_scp_script():
        sys.exit(1)

    print("The scp script is working correctly!")