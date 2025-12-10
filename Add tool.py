import requests
import json
import os

# COLORS
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(f"""
{BLUE}=================================================={RESET}
{GREEN}        SAFE OSINT TOOL - ADVANCED TEMPLATE{RESET}
{BLUE}=================================================={RESET}
""")

def username_lookup(username):
    print(f"\n{BLUE}[+] Checking username: {username}{RESET}\n")

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}"
    }

    for site, url in sites.items():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"{GREEN}[FOUND] {site}: {url}{RESET}")
            else:
                print(f"{RED}[NOT FOUND] {site}{RESET}")
        except:
            print(f"{RED}[ERROR] Could not check {site}{RESET}")

def ip_lookup(ip):
    print(f"\n{BLUE}[+] Getting info for IP: {ip}{RESET}\n")
    try:
        api = f"http://ip-api.com/json/{ip}"
        data = requests.get(api).json()
        for key, value in data.items():
            print(f"{GREEN}{key}: {value}{RESET}")
    except:
        print(f"{RED}Error while fetching IP data.{RESET}")

def main():
    clear()
    banner()

    print(f"{GREEN}1. Username Lookup{RESET}")
    print(f"{BLUE}2. IP Lookup{RESET}")
    print(f"{RED}3. Exit{RESET}")

    choice = input("\nEnter choice: ")

    if choice == "1":
        user = input("Enter username: ")
        username_lookup(user)

    elif choice == "2":
        ip = input("Enter IP address: ")
        ip_lookup(ip)

    else:
        print(f"{RED}Goodbye!{RESET}")

if __name__ == "__main__":
    main()
