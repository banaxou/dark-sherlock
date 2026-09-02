# code by ovax | dark sherlock 1.0

import requests

WHITE   = "\033[1;97m"
RED     = "\033[1;91m"
RESET   = "\033[0m"

user = input(f"{RED}╭──\n╰─>{RESET} {WHITE}enter username:{RESET} ").strip() or "ZeroBytes"

print(f"\n[{RED}*{RESET}] {WHITE}Checking username {user} on:{RESET}\n")

try:
    req = requests.get(f"https://threatactorusernames.com/api/search?q={user}", timeout=10)
    data = req.json()
    
    results = data.get("results", [])

   
    req_x = requests.get(f"https://x.com/{user}", timeout=10)
    status_x = req_x.status_code
    x = status_x == 200
    
   
    req_github = requests.get(f"https://api.github.com/users/{user}", timeout=10)
    s = req_github.status_code
    g = s == 200
    
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
