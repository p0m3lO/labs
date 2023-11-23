import os
import sys
import subprocess
import time

def check_package_installed(package_name):
    try:
        result = subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def check_established_connections(ip, timeout=2):
    try:
        # Send a single ping packet and wait for up to 'timeout' seconds for a reply
        result = subprocess.run(['ping', '-c', '1', '-W', str(timeout), ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode == 0:
            print("Established connections are working correctly.")
            return True
        else:
            print("Established connections are not working correctly.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


def test_connections(ssh_alias, ip, ports):
    # Check each port
    listeners = []
    for port in ports:
        # Check if the port is already being listened on
        try:
            result = subprocess.run(['lsof', '-i', f':{port}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # If the port is not being listened on, start a listener
            if result.returncode != 0:
                listener = subprocess.Popen(['sudo', 'nc', '-l', '-p', str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                listeners.append(listener)
                time.sleep(0.5)  # Give the listener time to start
        except Exception as e:
            print(f"Error occurred while checking port {port}. Exception: {e}")
            return False

    # Check iptables rules
    for port in ports:
        command = f'ssh {ssh_alias} "nc -znv {ip} {port}"'
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Check for specific conditions in the stderr output
            if "smtp" in result.stderr and "UNKNOWN" in result.stderr:
                print(f"Port {port} might be open (detected SMTP service).")
                return True
            elif result.returncode != 0:
                print(f"Error occurred while checking port {port}. Command output: {result.stderr}")
                return False
            else:
                return True
        except Exception as e:
            print(f"Error occurred while checking port {port}. Exception: {e}")
            return False


    # Close all listeners
    for listener in listeners:
        listener.terminate()

    return True

def check_iptables_drop_policy():
    try:
        result = subprocess.run(['sudo', 'iptables', '-L', 'INPUT'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"Error occurred while checking iptables policy. Command output: {result.stderr}")
            return False

        lines = result.stdout.split("\n")
        for line in lines:
            if "DROP" in line:
                return True

        print("The iptables does not have a DROP policy or rule for INPUT chain.")
        return False
    except Exception as e:
        print(f"Error occurred while checking iptables policy. Exception: {e}")
        return False

def check_connections():
    all_ports = [22, 5000, 7681, 80, 443, 2049, 25]
    if not test_connections('gde-server', '192.168.10.10', all_ports):
        return False
    return True

def check_persistence():
    package_installed = check_package_installed("iptables-persistent")
    if package_installed:
        return True

def check_manual_persistence():
    script_path = "/etc/network/if-pre-up.d/iptables"
    expected_line = "iptables-restore < /etc/iptables/rules.v4"

    if not os.path.exists(script_path):
        return False

    with open(script_path, 'r') as f:
        lines = f.readlines()

    if expected_line not in [line.strip() for line in lines]:
        return False

    if not os.access(script_path, os.X_OK):
        return False

    return True

if __name__ == "__main__":
    if not check_established_connections('1.1.1.1'):
        sys.exit(1)

    if not check_iptables_drop_policy():
            print("The iptables default input policy is not DROP.")
            sys.exit(1)

    if not check_connections():
        print("The iptables rules are not configured correctly.")
        sys.exit(1)

    if check_persistence():
        print("The iptables rules are persistent.")

    elif not check_persistence():
        if check_manual_persistence():
            print("The iptables manual persistency is set up correctly.")
        else:
            print("The iptables manual persistency is not set up correctly.")
            sys.exit(1)
    else:
        print("The iptables rules are not persistent.")
        sys.exit(1)

    print("The iptables rules are configured correctly and persistent!")
