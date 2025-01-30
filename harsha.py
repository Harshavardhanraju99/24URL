import os
import sys
import time
import subprocess
import importlib.util
import signal
import requests
import re
import urllib.parse
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
import validators

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_package_installed(package):
    return importlib.util.find_spec(package) is not None

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"{Fore.GREEN}[+] {package} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Failed to install {package}.")

def check_and_install_packages(packages):
    for package in packages:
        if is_package_installed(package):
            print(f"{Fore.GREEN}[+] {package} is already installed.")
        else:
            print(f"{Fore.YELLOW}[!] {package} is missing. Installing...") 
            install_package(package)

def load_config():
    return ["colorama", "requests", "validators"]

def handle_interrupt(signal, frame):
    print(f"\n{Fore.RED}[!] Program interrupted. Exiting...")
    sys.exit(0)

def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain

def fetch_status_code(url):
    try:
        head_response = requests.head(url, timeout=5)
        return url, head_response.status_code
    except requests.exceptions.Timeout:
        return url, "Error: Timeout"
    except requests.exceptions.RequestException as e:
        return url, "UNKNOWN"

def fetch_and_filter_wayback_info(domain):
    found_urls = 0
    urls_to_save = []
    start_time = time.time()
    print(f"{Fore.MAGENTA}Starting the Scan on: {Fore.WHITE}{domain}")
    time.sleep(2)
    print(f"{Fore.YELLOW}\n[i] Loading, please wait...\n")

    base_url = "https://web.archive.org/cdx/search/cdx"
    
    params = {
        'url': f"*.{domain}/*",
        'collapse': 'urlkey',
        'output': 'text',
        'fl': 'original'
    }

    file_extensions_regex = r'\.xls|\.xml|\.xlsx|\.json|\.pdf|\.sli|\.doc|\.docx|\.pptx|\.txt|\.zip|\.tar|\.gz|\.tgz|\.bak|\.7z|\.rar|\.log|\.cache|\.secret|\.db|\.backup|\.yml|\.gz|\.config|\.csv|\.yaml|\.md|\.md5|\.exe|\.dll|\.bin|\.ini|\.bat|\.sh|\.deb|\.rpm|\.iso|\.img|\.apk|\.msi|\.dmg|\.tmp|\.crt|\.pem|\.key|\.pub|\.asc'
    
    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            urls = response.text.splitlines()
            filtered_urls = [url.strip() for url in urls if re.search(file_extensions_regex, url)]
            
            if filtered_urls:
                with ThreadPoolExecutor() as executor:
                    futures = {executor.submit(fetch_status_code, url): url for url in filtered_urls}
                    
                    for idx, future in enumerate(as_completed(futures), start=1):
                        url, status_code = future.result()
                        encoded_url = urllib.parse.quote(url, safe=':/')
                        
                        index_str = f"({idx:02})" 
                        
                        if "Error" in str(status_code):
                            print(f"{Fore.MAGENTA}{index_str}{Fore.GREEN} Found: {Fore.WHITE}{url} {Fore.BLUE} - Status code: {status_code}")
                        else:
                            print(f"{Fore.MAGENTA}{index_str}{Fore.GREEN} Found: {Fore.WHITE}{url} {Fore.BLUE} - Status code: {status_code}")
                        print(f"{Fore.MAGENTA} → {Fore.CYAN}URL: {Fore.WHITE}https://web.archive.org/web/*/{encoded_url}")
                        print()
                        found_urls += 1
                        urls_to_save.append(url)
            else:
                print(f"{Fore.RED}[!] No matching URLs found.\n")
        else:
            print(f"{Fore.RED}[!] Failed to fetch data Status code. Please try again...\n")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")
    
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"{Fore.YELLOW}[*] Scanning Finished.")
    time.sleep(1)
    print(f"{Fore.YELLOW}[*] Total Found: {found_urls}")
    print(f"{Fore.YELLOW}[*] Time Taken: {time_taken:.2f} seconds")

    if found_urls > 0:
        save_urls = input(f"{Fore.WHITE}\n[?] Do you want to save the URLs to output.txt? (y/n) [default: n]: ").strip().lower()
        if save_urls == 'y':
            with open("output.txt", "w") as f:
                for url in urls_to_save:
                    f.write(url + "\n")
            print(f"{Fore.GREEN}[+] URLs saved to output.txt")
        else:
            print(f"{Fore.RED}[-] URLs not saved")

def validate_url(url):
    if validators.url(url):
        return True
    else:
        print(f"{Fore.RED}[!] Invalid URL. Please enter a valid URL.")
        return False

def Banner():
    print(rf"{Fore.GREEN}  _____ _                                 _ _    ")
    print(rf"{Fore.GREEN} /__   (_)_ __ ___   ___/\   /\__ _ _   _| | |_  ")
    print(rf"{Fore.GREEN}   / /\/ | '_ ` _ \ / _ \ \ / / _` | | | | | __| ")
    print(rf"{Fore.GREEN}  / /  | | | | | | |  __/\ V / (_| | |_| | | |_  ")
    print(rf"{Fore.GREEN}  \/   |_|_| |_| |_|\___| \_/ \__,_|\__,_|_|\__| ")
                                                                                  
    print("")

    created_by_text = "Program created by: AnonKryptiQuz"
    ascii_width = 49
    padding = (ascii_width - len(created_by_text)) // 2
    print(" " * padding + f"{Fore.RED}{created_by_text}")
    print("")

def main():
    signal.signal(signal.SIGINT, handle_interrupt)
    
    clear_screen()
    print(f"{Fore.YELLOW}[i] Checking for required packages...\n")
    
    required_packages = load_config()
    check_and_install_packages(required_packages)

    time.sleep(3)

    clear_screen()
    Banner()
    
    while True:
        url = input("[?] Enter the website URL (e.g., https://google.com): ")
        if validate_url(url):
            break
        input(f"{Fore.YELLOW}[i] Press Enter to try again...")
        clear_screen()
        Banner()

    print(f"{Fore.YELLOW}\n[i] Loading, please wait...")
    time.sleep(3)
    clear_screen()

    domain = get_domain(url)
    fetch_and_filter_wayback_info(domain)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n[!] Operation interrupted. Exiting...")