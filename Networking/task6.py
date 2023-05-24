import os
import sys
import subprocess


def check_package_installed(package_name):
    try:
        result = subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def test_connections(ssh_alias, ip, ports):
    for port in ports:
        command = ['ssh', ssh_alias, 'nc', '-zv', ip, str(port)]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if 'succeeded' in result.stdout:
                print(f"Connection to {ip} on port {port} succeeded.")
            else:
                print(f"Connection to {ip} on port {port} failed.")
                return False
        except subprocess.CalledProcessError as e:
            print(f"Connection to {ip} on port {port} failed: {e}")
            return False
    return True

def check_connections():
    all_ports = [22, 5000, 7681, 80, 443, 2049, 25]
    if not test_connections('example-server', '192.168.20.10', all_ports):
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
