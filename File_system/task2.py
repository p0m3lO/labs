import subprocess
import sys

def check_raid_array(devices, level):
    try:
        result = subprocess.run(["sudo", "mdadm", "--detail", "/dev/md0"], stdout=subprocess.PIPE, text=True)
        output_lines = result.stdout.split('\n')
        
        # Check RAID level
        raid_level_correct = any(f"Raid Level : {level}" in line for line in output_lines)

        # Check each device
        devices_correct = all(any(device in line for line in output_lines) for device in devices)

        return raid_level_correct and devices_correct

    except subprocess.CalledProcessError as e:
        print(f"Error executing mdadm: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    devices = ["/dev/loop3", "/dev/loop4"]
    level = "raid1"

    if check_raid_array(devices, level):
        print("The RAID array is configured correctly.")
    else:
        print("The RAID array is NOT configured correctly.")
        sys.exit(1)
