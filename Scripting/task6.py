import os
import sys
import subprocess

def check_random_script(target_dir, num_dirs, num_files):
    script_path = os.path.expanduser("~/scripts/random.sh")
    if not os.path.exists(script_path):
        print("Error: Script 'random.sh' not found in '~/scripts/'.")
        return False
    
    try:
        subprocess.run([script_path, "--directory", str(num_dirs), "--files", str(num_files), target_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

    for i in range(1, num_dirs + 1):
        dir_name = f"test_dir{i}"
        dir_path = os.path.join(target_dir, dir_name)

        if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
            print(f"Error: Directory '{dir_path}' not found.")
            return False
        
        for j in range(1, num_files + 1):
            file_name = f"file{j}.txt"
            file_path = os.path.join(dir_path, file_name)

            if not os.path.exists(file_path) or not os.path.isfile(file_path):
                print(f"Error: File '{file_path}' not found.")
                return False

    return True

if __name__ == "__main__":
    target_dir = "/tmp/test_random_script"
    num_dirs = 10
    num_files = 5

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    result = check_random_script(target_dir, num_dirs, num_files)
    if result:
        print(f"The 'random.sh' script works correctly. {num_dirs} directories with {num_files} files each were created in '{target_dir}'.")
    else:
        print(f"The 'random.sh' script does NOT work correctly.")
        sys.exit(1)