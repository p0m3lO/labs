import os
import sys
import subprocess
import re

def check_locale(target_locale):
    try:
        result = subprocess.run(["localectl", "status"], stdout=subprocess.PIPE, text=True)
        current_locale = re.search(r'LANG=(.+)', result.stdout)
        if current_locale:
            return current_locale.group(1) == target_locale
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    target_locale = "hu_HU.UTF-8"

    locale_result = check_locale(target_locale)

    if locale_result:
        print(f"The locale is set to '{target_locale}'.")
    else:
        print(f"The locale is NOT set to '{target_locale}'.")
        sys.exit(1)
