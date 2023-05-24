import os
import sys
import re

def check_permanent_hostname(target_hostname):
    hostname_file = "/etc/hostname"
    hosts_file = "/etc/hosts"

    try:
        with open(hostname_file, 'r') as f:
            hostname = f.read().strip()

        if hostname != target_hostname:
            return False
        else:
            return True

    except FileNotFoundError:
        print("Error: File not found. Make sure the script is run as root or with proper permissions.")
        return False


def check_hostfile(target_hostname):
    hosts_file = "/etc/hosts"
    try:
        with open(hosts_file, 'r') as f:
            hosts = f.readlines()

        for line in hosts:
            if line.startswith('127.0.0.1') or line.startswith('127.0.1.1'):
                if re.search(r'\b' + re.escape(target_hostname) + r'\b', line):
                    return True

        return False

    except FileNotFoundError:
        print(f"Error: {hosts_file} file not found.")
        return False


if __name__ == "__main__":
    target_hostname = "gde-exam"
    result = check_permanent_hostname(target_hostname)
    hosts_result = check_hostfile(target_hostname)
    if result and hosts_result:
        print(f"The hostname is set permanently to '{target_hostname} and set in hosts file'.")
        points = 8
        print(f"Points: {points}")
    elif not hosts_result:
        print(f"The '{target_hostname}' is NOT set in hosts file")
        sys.exit(1)
    else:
        print(f"The hostname is NOT set permanently to '{target_hostname}'.")
        sys.exit(1)