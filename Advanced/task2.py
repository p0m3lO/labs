import subprocess
import sys
import os
import re
import json

def check_package_installed(package_name):
    try:
        subprocess.run(["which", package_name], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def check_nginx_reverse_proxy(backend_server):
    nginx_conf_file = "/etc/nginx/sites-enabled/reverse-proxy"
    if not os.path.exists(nginx_conf_file):
        return False

    with open(nginx_conf_file, "r") as f:
        content = f.read()

    return f"proxy_pass {backend_server};" in content

def check_docker_container(container_name):
    result = subprocess.run(["docker", "ps", "--filter", f"name={container_name}", "--format", "{{json .}}"], stdout=subprocess.PIPE, text=True)
    containers = [json.loads(line) for line in result.stdout.splitlines()]

    return len(containers) > 0

if __name__ == "__main__":
    package_name = "nginx"
    backend_server = "http://127.0.0.1:3000"
    container_name = "gde-app"

    if (check_package_installed(package_name) and
        check_nginx_reverse_proxy(backend_server) and
        check_docker_container(container_name)):
        print("The Nginx reverse proxy to the Docker container is configured correctly.")
    else:
        print("The Nginx reverse proxy to the Docker container is NOT configured correctly.")
        sys.exit(1)