import os
import sys
import subprocess

def check_swap_size():
    result = subprocess.run(['sudo', 'swapon', '--show=size'], stdout=subprocess.PIPE, text=True)
    swap_size = result.stdout.strip()
    return swap_size == '1G'

def check_swap_file():
    return os.path.exists('/mnt/swap')

def check_fstab():
    with open('/etc/fstab', 'r') as f:
        lines = f.readlines()
    return '/mnt/swap none swap sw 0 0' in [line.strip() for line in lines]

def main():
    if not check_swap_size():
        print("The swap size is not 1GB.")
        sys.exit(1)

    if not check_swap_file():
        print("The swap file '/mnt/swap' does not exist.")
        sys.exit(1)

    if not check_fstab():
        print("The swap file is not set up to persist after reboot.")
        sys.exit(1)

    print("Swap file is set up correctly!")

if __name__ == "__main__":
    main()
