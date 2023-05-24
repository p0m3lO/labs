import os
import sys
import subprocess
import re

def check_locale():
    try:
        result = subprocess.run(["localectl", "status"], stdout=subprocess.PIPE, text=True)
        current_locale = re.search(r'LANG=(.+)', result.stdout)
        if current_locale:
            # Now checking if 'hu_' is in the string
            return 'hu_' in current_locale.group(1)
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    locale_result = check_locale()

    if locale_result:
        print("The locale is set to a Hungarian language option.")

    else:
        print("The locale is NOT set to a Hungarian language option.")
        sys.exit(1)