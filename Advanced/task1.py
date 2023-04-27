import subprocess
import sys
import json

def check_docker_installed():
    try:
        subprocess.run(["docker", "--version"], check=True)
        return True
    except FileNotFoundError:
        return False

def check_docker_service_running():
    try:
        subprocess.run(["systemctl", "is-active", "--quiet", "docker"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_nginx_container():
    result = subprocess.run(["docker", "ps", "-a", "--format", "{{json .}}"], stdout=subprocess.PIPE, text=True)
    containers = [json.loads(line) for line in result.stdout.splitlines()]

    for container in containers:
        if container["Image"] == "nginx" and "0.0.0.0:8080->80/tcp" in container["Ports"]:
            return True
    return False

if __name__ == "__main__":
    if check_docker_installed() and check_docker_service_running() and check_nginx_container():
        print("The Docker container is configured correctly.")
    else:
        print("The Docker container is NOT configured correctly.")
        sys.exit(1)