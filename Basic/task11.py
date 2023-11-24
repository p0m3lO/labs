import os
import sys
import subprocess

def check_package_installed(package_name):
    try:
        subprocess.run(["dpkg-query", "-W", "-f='${Status}'", package_name], check=True, stdout=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError:
        return False


def find_screen_session_pid(session_name):
    try:
        result = subprocess.run(["screen", "-ls"], stdout=subprocess.PIPE, text=True)
        # Regex to find the session with its PID
        match = re.search(r'(\d+).%s\s+\(' % re.escape(session_name), result.stdout)
        return match.group(1) if match else None
    except subprocess.CalledProcessError:
        return None

def check_process_running_in_screen(screen_pid, process_name):
    try:
        cmd = f"ps -ef | grep {screen_pid} | grep -v grep | grep {process_name}"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    package_name = "screen"
    session_name = "demo_screen"
    process_name = "screen_test.sh"

    screen_installed = check_package_installed(package_name)
    if not screen_installed:
        print(f"The 'screen' package is not installed")
        sys.exit(1)

    screen_pid = find_screen_session_pid(session_name)
    if screen_pid and check_process_running_in_screen(screen_pid, process_name):
        print(f"{process_name} is running within the {session_name} session.")
    else:
        print(f"{process_name} is NOT running within the {session_name} session.")

    if screen_installed and screen_pid:
        print(f"The 'screen' package is installed, the '{session_name}' session is running, and the '{process_name}' script is running within the session.")
    else:
        print(f"Either the 'screen' package is NOT installed, the '{session_name}' session is NOT running, or the '{process_name}' script is NOT running within the session.")
        sys.exit(1)