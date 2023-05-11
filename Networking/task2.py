import os
import sys
import subprocess

def check_sshfs_mount():
    try:
        result = subprocess.run(['mount'], stdout=subprocess.PIPE, text=True)
        return "gde-server:/mnt/mount on /mnt/shared type fuse.sshfs" in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

def check_sshfs_auto_mount():
    with open('/etc/fstab', 'r') as f:
        return "sshfs#gde-server:/mnt/mount /mnt/shared fuse defaults 0 0" in f.read()

if __name__ == "__main__":
    if not check_sshfs_mount():
        print("The SSHFS mount is not configured correctly.")
        sys.exit(1)

    if not check_sshfs_auto_mount():
        print("The SSHFS mount is not set to auto-mount at startup.")
        sys.exit(1)

    print("The SSHFS mount is configured correctly and set to auto-mount at startup!")
