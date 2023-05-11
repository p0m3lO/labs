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

def check_autofs_config():
    try:
        with open('/etc/auto.master', 'r') as f:
            return "/- /etc/gde.sshfs" in f.read()
    except FileNotFoundError:
        return False

    try:
        with open('/etc/gde.sshfs', 'r') as f:
            return "/mnt/shared -fstype=fuse.sshfs,uid=1000,gid=1000,allow_other,_netdev :gde-server:/mnt/mount" in f.read()
    except FileNotFoundError:
        return False


def check_write_permissions():
    return os.access('/mnt/shared', os.W_OK)

def check_file_creation():
    try:
        with open('/mnt/shared/test_file', 'w') as f:
            f.write('test')
        os.remove('/mnt/shared/test_file')
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if not check_sshfs_mount():
        print("The SSHFS mount is not configured correctly.")
        sys.exit(1)

    if not check_autofs_config():
        print("The AutoFS configuration is not set up correctly.")
        sys.exit(1)

    if not check_write_permissions():
        print("Write permissions on the mount point are not set correctly.")
        sys.exit(1)

    if not check_file_creation():
        print("A file could not be created in the mount point.")
        sys.exit(1)

    print("The SSHFS mount is configured correctly and set to auto-mount at startup!")
