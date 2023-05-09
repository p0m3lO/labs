import os
import sys
import subprocess

def check_package_installed(package_name):
    try:
        subprocess.run(["dpkg-query", "-W", "-f='${Status}'", package_name], check=True, stdout=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_chrony_config():
    config_file = "/etc/chrony/chrony.conf"
    if not os.path.exists(config_file):
        return False

    with open(config_file, "r") as f:
        content = f.read()

    return "pool" in content or "server" in content

def check_ntp_config():
    config_file = "/etc/ntp.conf"
    if not os.path.exists(config_file):
        return False

    with open(config_file, "r") as f:
        content = f.read()

    return "pool" in content or "server" in content

def check_timezone(target_timezone):
    try:
        result = subprocess.run(["timedatectl", "show", "--property=Timezone"], stdout=subprocess.PIPE, text=True)
        current_timezone = result.stdout.strip().split('=')[-1]
        return current_timezone == target_timezone
    except subprocess.CalledProcessError:
        return False

def check_timezone_tzdata(target_timezone):
    tzdata_file = "/etc/localtime"
    if not os.path.exists(tzdata_file):
        return False

    tzdata_target_path = os.path.join("/usr/share/zoneinfo", target_timezone)
    return os.path.realpath(tzdata_file) == tzdata_target_path

def check_service_status(service_name):
    try:
        subprocess.run(["systemctl", "is-active", "--quiet", service_name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    target_timezone = "Europe/Budapest"
    timezone_result = check_timezone(target_timezone) or check_timezone_tzdata(target_timezone)

    chrony_installed = check_package_installed("chrony")
    ntp_installed = check_package_installed("ntp")
    chrony_service = check_service_status("chronyd")

    if not (chrony_installed or ntp_installed):
        print("Neither Chrony nor NTP is installed.")
        sys.exit(1)

    if chrony_installed and chrony_service:
        config_ok = check_chrony_config()
        service_ok = check_service_status("chronyd")
        package_name = "Chrony"
    else:
        config_ok = check_ntp_config()
        service_ok = check_service_status("ntp")
        package_name = "NTP"

    if timezone_result:
        print(f"The timezone is set to '{target_timezone}'")
    else:
        print(f"The timezone is NOT set to '{target_timezone}'")
        sys.exit(1)

    if service_ok:
        print(f"The NTP service with {package_name} is running")

    else:
        print(f"The NTP service with {package_name} is NOT running")
        sys.exit(1)

    if config_ok:
        print(f"The NTP service is configured correctly.")

    else:
        print(f"The NTP service is NOT configured correctly.")
        sys.exit(1)
