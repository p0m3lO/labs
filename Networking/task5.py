import os
import sys
import subprocess

def check_iptables_rules():
    try:
        result = subprocess.run(['iptables', '-S'], stdout=subprocess.PIPE, text=True)
        rules = result.stdout.split('\n')

        expected_rules = {
            '-A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT',
            '-A INPUT -p tcp -s 192.168.10.20 --dport 80 -j ACCEPT',
            '-A INPUT -p tcp -s 192.168.10.20 --dport 443 -j ACCEPT',
            '-A INPUT -p tcp -s 192.168.10.20 --dport 2049 -j ACCEPT',
            '-A INPUT -p tcp -s 192.168.10.20 --dport 25 -j ACCEPT',
            '-A INPUT -p tcp --dport 22 -j ACCEPT',
            '-A INPUT -j DROP'
        }

        return expected_rules.issubset(set(rules))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

def check_persistence(expected_rules):
    # Check if the package iptables-persistent is installed
    package_installed = check_package_installed("iptables-persistent")
    if package_installed:
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
    if not check_iptables_rules():
        print("The iptables rules are not configured correctly.")
        sys.exit(1)

    if not check_persistence():
        print("The iptables rules are not persistent.")
        sys.exit(1)

    print("The iptables rules are configured correctly and persistent!")