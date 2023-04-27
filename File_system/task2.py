import subprocess
import sys

def check_raid_array(devices, level):
    try:
        result = subprocess.run(["mdadm", "--detail", "/dev/md0"], stdout=subprocess.PIPE, text=True)
        devices_str = " ".join(devices)
        return f"Raid Level : {level}" in result.stdout and devices_str in result.stdout
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    devices = ["/dev/loop3", "/dev/loop4"]
    level = "raid1"

    if check_raid_array(devices, level):
        print("The RAID array is configured correctly.")
    else:
        print("The RAID array is NOT configured correctly.")
        sys.exit(1)