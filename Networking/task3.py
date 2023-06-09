import os
import subprocess
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_text = None
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_endtag(self, tag):
        self.current_tag = None

    def handle_data(self, data):
        if self.current_tag == "h1":
            self.h1_text = data


def check_nginx_installed():
    try:
        result = subprocess.run(['sudo', 'nginx', '-v'], stderr=subprocess.PIPE, text=True)
        return "nginx" in result.stderr
    except FileNotFoundError:
        return False


def check_custom_welcome_page():
    custom_page_path = "/var/www/gde/index.html"
    if not os.path.exists(custom_page_path):
        return False

    with open(custom_page_path, "r") as f:
        content = f.read()

    parser = MyHTMLParser()
    parser.feed(content)

    return parser.h1_text == "Welcome to My GDE lab test Site!"


def check_nginx_running():
    result = subprocess.run(['systemctl', 'is-active', 'nginx'], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip() == 'active'


def main():
    if not check_nginx_installed():
        print("Nginx is not installed.")
        sys.exit(1)

    if not check_custom_welcome_page():
        print("The custom welcome page is not configured correctly.")
        sys.exit(1)

    if not check_nginx_running():
        print("Nginx is not running.")
        sys.exit(1)

    print("Everything is set up correctly!")


if __name__ == "__main__":
    main()