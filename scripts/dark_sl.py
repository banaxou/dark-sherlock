# code by ovax | dark sherlock 1.1 - proxy

import requests

WHITE   = "\033[1;97m"
RED     = "\033[1;91m"
RESET   = "\033[0m"

user = input(f"{RED}╭──\n╰─>{RESET} {WHITE}enter username:{RESET} ").strip() or "ZeroBytes"
proxy = input(f"{RED}╭──\n╰─>{RESET} {WHITE}proxy (ex: socks5h://127.0.0.1:9050) [skip] ─ :{RESET} ").strip()


if proxy.startswith("socks5://"):
    proxy = "socks5h://" + proxy[len("socks5://"):]

proxies = {"http": proxy, "https": proxy} if proxy else None

print(f"\n[{RED}*{RESET}] {WHITE}Checking username {user} on:{RESET}\n")

try:
    if proxies:
        ip = requests.get("https://api.ipify.org", proxies=proxies, timeout=10).text.strip()
        print(f"[{RED}*{RESET}] {WHITE}IP via proxy: {ip}{RESET}\n")

    req = requests.get(f"https://threatactorusernames.com/api/search?q={user}", proxies=proxies, timeout=10)
    data = req.json()

    results = data.get("results", [])

    req_x = requests.get(f"https://x.com/{user}", proxies=proxies, timeout=10)
    x = req_x.status_code == 200

    req_github = requests.get(f"https://api.github.com/users/{user}", proxies=proxies, timeout=10)
    g = req_github.status_code == 200

    allx = len(results) + (1 if x else 0) + (1 if g else 0)

    print(f"[{RED}+{RESET}] {WHITE}Results: {allx}{RESET}\n")

    if not results and not x and not g:
        print(f"[{RED}-{RESET}] No results found")
    else:
        for item in results:
            source = item.get("forum", item.get("source", "Unknown"))
            print(f"[{RED}+{RESET}] {WHITE}{source}: {user}{RESET}")

        if x:
            print(f"[{RED}+{RESET}] {WHITE}x | twitter: {user}{RESET}")

        if g:
            print(f"[{RED}+{RESET}] {WHITE}github: {user}{RESET}")

except requests.exceptions.RequestException as e:
    print(f"[{RED}-{RESET}] Error: {e}")
except Exception as e:
    print(f"[{RED}-{RESET}] Unexpected error: {e}")
