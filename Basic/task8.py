import subprocess
import sys
import os
import re
import time

def check_package_installed(package_name):
    try:
        subprocess.run(["which", package_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def check_postfix_config():
    config_file = "/etc/postfix/main.cf"
    if not os.path.exists(config_file):
        return False

    with open(config_file, "r") as f:
        content = f.read()

    myhostname = re.search(r'^myhostname\s*=\s*(.+)$', content, re.MULTILINE)
    inet_interfaces = re.search(r'^inet_interfaces\s*=\s*(.+)$', content, re.MULTILINE)
    
    return (myhostname and myhostname.group(1) == "gdemailserver" and
            inet_interfaces and inet_interfaces.group(1) == "localhost")

def send_test_email(user):
    try:
        subprocess.run(["echo", "This is a test email", "|", "mail", "-s", "Test Email", user], check=True)
    except subprocess.CalledProcessError:
        return False
    return True

def check_test_email(user):
    result = subprocess.run(["sudo", "mail", "-u", user, "-H"], stdout=subprocess.PIPE, text=True)
    return "Test Email" in result.stdout

if __name__ == "__main__":
    package_name = "postfix"
    test_user = "gde"

    if (check_package_installed(package_name) and
        check_postfix_config() and
        send_test_email(test_user)):
        time.sleep(10)  # Wait a few seconds to ensure the email is delivered
        if check_test_email(test_user):
            print("The local email server with Postfix is configured and working correctly.")
        else:
            print("The local email server with Postfix is NOT working correctly.")
            sys.exit(1)
    else:
        print("The local email server with Postfix is NOT configured correctly.")
        sys.exit(1)
