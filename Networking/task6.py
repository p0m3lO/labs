import os
import sys
import subprocess


def check_package_installed(package_name):
    try:
        result = subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def check_iptables_rules():
    try:
        result = subprocess.run(['sudo', 'iptables', '-S'], stdout=subprocess.PIPE, text=True)
        rules = result.stdout.split('\n')
        rules = [' '.join(rule.split()) for rule in rules]

        expected_rules = {
            '-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT',
            '-A INPUT -s 192.168.10.20/32 -p tcp -m tcp --dport 80 -j ACCEPT',
            '-A INPUT -s 192.168.10.20/32 -p tcp -m tcp --dport 443 -j ACCEPT',
            '-A INPUT -s 192.168.10.20/32 -p tcp -m tcp --dport 2049 -j ACCEPT',
            '-A INPUT -s 192.168.10.20/32 -p tcp -m tcp --dport 25 -j ACCEPT',
            '-A INPUT -p tcp -m tcp --dport 5000 -j ACCEPT',
            '-A INPUT -p tcp -m tcp --dport 7681 -j ACCEPT',
            '-A INPUT -p tcp -m tcp --dport 22 -j ACCEPT',
            '-A INPUT -j DROP'
        }

        return expected_rules.issubset(set(rules)), expected_rules
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False, {}


def check_persistence(expected_rules):
    # Check if the package iptables-persistent is installed
    package_installed = check_package_installed("iptables-persistent")
    if package_installed:
        return True

def check_manual_persistence():
    script_path = "/etc/network/if-pre-up.d/iptables"
    expected_line = "iptables-restore < /etc/iptables/rules.v4"

    # Check that the script file exists
    if not os.path.exists(script_path):
        return False

    # Check the content of the script file
    with open(script_path, 'r') as f:
        lines = f.readlines()

    if expected_line not in [line.strip() for line in lines]:
        return False

    # Check that the script file is executable
    if not os.access(script_path, os.X_OK):
        return False

    return True

    # Check for manual persistence
    try:
        with open('/etc/iptables/rules.v4', 'r') as f:
            rules = f.read().splitlines()
        for rule in expected_rules:
            if rule not in rules:
                return False
        return True
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    rules_ok, expected_rules = check_iptables_rules()
    if not rules_ok:
        print("The iptables rules are not configured correctly.")
        sys.exit(1)

    if check_persistence(expected_rules):
        print("The iptables rules are persistent.")

    elif not check_persistence(expected_rules):
        if check_manual_persistence():
            print("The iptables manual persistency is set up correctly.")
        else:
            print("The iptables manual persistency is not set up correctly.")
            sys.exit(1)
    else:
        print("The iptables rules are not persistent.")
        sys.exit(1)


    print("The iptables rules are configured correctly and persistent!")