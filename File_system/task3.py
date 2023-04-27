import os
import sys

def check_chroot_env(directory_path):
    required_files = ["bin", "boot", "dev", "etc", "home", "lib", "lib64", "media", "mnt", "opt", "proc", "root", "run", "sbin", "srv", "sys", "tmp", "usr", "var"]
    if not os.path.isdir(directory_path):
        return False
    return all(os.path.exists(os.path.join(directory_path, file)) for file in required_files)

def check_debian_version(directory_path, expected_version):
    os_release_path = os.path.join(directory_path, "etc/os-release")
    if not os.path.exists(os_release_path):
        return False

    with open(os_release_path, "r") as os_release_file:
        content = os_release_file.read()

    return f'VERSION_CODENAME={expected_version}' in content

if __name__ == "__main__":
    directory_path = "/tmp/gde_chroot"
    expected_version = "buster"

    if check_chroot_env(directory_path) and check_debian_version(directory_path, expected_version):
        print(f"The chroot environment with Debian {expected_version} at '{directory_path}' is configured correctly.")
    else:
        print(f"The chroot environment with Debian {expected_version} at '{directory_path}' is NOT configured correctly.")
        sys.exit(1)
