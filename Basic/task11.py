import os
import sys
import subprocess

def check_package_installed(package_name):
    try:
        subprocess.run(["dpkg-query", "-W", "-f='${Status}'", package_name], check=True, stdout=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def find_screen_session(session_name):
    try:
        result = subprocess.run(["screen", "-ls"], stdout=subprocess.PIPE, text=True)
        return session_name in result.stdout
    except subprocess.CalledProcessError:
        return False

def check_process_running(process_name):
    try:
        result = subprocess.run(["pgrep", "-a", process_name], stdout=subprocess.PIPE, text=True)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    package_name = "screen"
    session_name = "demo_screen"
    process_name = "screen_test.sh"

    screen_installed = check_package_installed(package_name)
    screen_session_found = find_screen_session(session_name)
    process_running = check_process_running(process_name)

    if screen_installed and screen_session_found and process_running:
        print(f"The 'screen' package is installed, the '{session_name}' session is running, and the '{process_name}' script is running within the session.")
    else:
        print(f"Either the 'screen' package is NOT installed, the '{session_name}' session is NOT running, or the '{process_name}' script is NOT running within the session.")
        sys.exit(1)