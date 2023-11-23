import os
import sys
import subprocess

def check_swap_size():
    try:
        result = subprocess.run(['sudo', 'swapon', '--show=NAME,SIZE'], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.strip().split('\n')
        for line in lines[1:]:  # Skip the header line
            name, size = line.split()
            if name == '/mnt/swap' and size == '1024M':
                return True
        return False
    except Exception as e:
        print(f"Error checking swap size: {e}")
        return False

def check_swap_file():
    if os.path.exists('/mnt/swap'):
        return os.stat('/mnt/swap').st_size == 1024 * 1024 * 1024  # Checking the file size is 1GB
    return False

def check_fstab():
    try:
        with open('/etc/fstab', 'r') as f:
            lines = f.readlines()
        return '/mnt/swap none swap sw 0 0' in [line.strip() for line in lines]
    except Exception as e:
        print(f"Error reading fstab: {e}")
        return False

def main():
    if not check_swap_size():
        print("The swap size is not 1GB or not correctly configured.")
        sys.exit(1)

    if not check_swap_file():
        print("The swap file '/mnt/swap' does not exist or has incorrect size.")
        sys.exit(1)

    if not check_fstab():
        print("The swap file is not set up to persist after reboot.")
        sys.exit(1)

    print("Swap file is set up correctly!")

if __name__ == "__main__":
    main()
