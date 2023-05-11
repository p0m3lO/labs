import os
import sys
import subprocess

def check_luks_container():
    user_home = os.path.expanduser('~')
    container_path = os.path.join(user_home, 'secret_container')
    result = subprocess.run(['sudo', 'cryptsetup', 'isLuks', container_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        return False
    return True

def check_crypttab_entry():
    with open('/etc/crypttab', 'r') as f:
        return "secret /home/vagrant/secret_container /root/keyfile luks" in f.read()

def check_fstab_entry():
    with open('/etc/fstab', 'r') as f:
        return "/dev/mapper/secret /mnt/secret ext4 defaults 0 0" in f.read()

def check_mounted():
    result = subprocess.run(['mount'], stdout=subprocess.PIPE, text=True)
    return "/dev/mapper/secret on /mnt/secret type ext4" in result.stdout

if __name__ == "__main__":
    if not check_luks_container():
        print("The LUKS container is not configured correctly.")
        sys.exit(1)

    if not check_crypttab_entry():
        print("The /etc/crypttab entry is missing or incorrect.")
        sys.exit(1)

    if not check_fstab_entry():
        print("The /etc/fstab entry is missing or incorrect.")
        sys.exit(1)

    if not check_mounted():
        print("The LUKS container is not mounted.")
        sys.exit(1)

    print("The LUKS container is configured correctly and mounted!")
