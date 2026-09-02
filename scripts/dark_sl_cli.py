# code by ovax | dark sherlock argparse 1.0

import requests
import argparse
import json
import sys
from datetime import datetime

WHITE = "\033[1;97m"
RED   = "\033[1;91m"
RESET = "\033[0m"

def parsey():
    parser = argparse.ArgumentParser(
        prog="dark-sl",
        description="Dark Sherlock - Username CSINT Tool : Find Usernames Across  Dark web ;) v1.0",
        usage="%(prog)s [username] [-u USERNAME] [--json] [--txt]",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "usernames",
        nargs="*",
        help="Username to check"
    )

    parser.add_argument(
        "-u", "--user",
        dest="users",
        nargs="+",
        help="Username target | Double username target"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Save results in JSON file + display normal output"
    )

    parser.add_argument(
        "--txt",
        action="store_true",
        help="Save results in TXT file"
    )

    return parser.parse_args()

def dsherlock(user, jsonx=False, txt=False):
    if not jsonx:
        print(f"\n[{RED}*{RESET}] {WHITE}Checking username {user} on:{RESET}\n")

    results_data = {
        "tool": "[dark-sherlock]",
        "username": user,
        "platforms": [],
        "total": 0
    }

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
        results_data["total"] = allx

        if not jsonx:
            print(f"[{RED}+{RESET}] {WHITE}Results: {allx}{RESET}\n")

        if not results and not x and not g:
            if not jsonx:
                print(f"[{RED}-{RESET}] No results found")
        else:
            for item in results:
                source = item.get("forum", item.get("source", "Unknown"))
                results_data["platforms"].append({
                    "platform": source,
                    "username": user,
                    "found_by": "[dark-sherlock]"
                })
                if not jsonx:
                    print(f"[{RED}+{RESET}] {WHITE}{source}: {user}{RESET}")

            if x:
                results_data["platforms"].append({
                    "platform": "x | twitter",
                    "username": user,
                    "found_by": "[dark-sherlock]"
                })
                if not jsonx:
                    print(f"[{RED}+{RESET}] {WHITE}x | twitter: {user}{RESET}")

            if g:
                results_data["platforms"].append({
                    "platform": "github",
                    "username": user,
                    "found_by": "[dark-sherlock]"
                })
                if not jsonx:
                    print(f"[{RED}+{RESET}] {WHITE}github: {user}{RESET}")

        if jsonx:
            filename = f"dark-sherlock_{user}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(results_data, f, indent=2, ensure_ascii=False)
            print(f"[{RED}+{RESET}] JSON saved → {filename}")

        if txt:
            filename = f"dark-sherlock_{user}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"[dark-sherlock] Results for {user}\n")
                f.write(f"Total: {results_data['total']}\n\n")
                for p in results_data["platforms"]:
                    f.write(f"[+] {p['platform']}: {user}\n")
            print(f"[{RED}+{RESET}] TXT saved → {filename}")

    except requests.exceptions.RequestException as e:
        if jsonx:
            print(json.dumps({"error": str(e)}, indent=2))
        else:
            print(f"[{RED}-{RESET}] Error: {e}")
        sys.exit(1)
    except Exception as e:
        if jsonx:
            print(json.dumps({"error": str(e)}, indent=2))
        else:
            print(f"[{RED}-{RESET}] Unexpected error: {e}")
        sys.exit(1)

def main():
    args = parsey()

    usernames = []
    if args.usernames:
        usernames.extend(args.usernames)
    if args.users:
        usernames.extend(args.users)

    if not usernames:
        user = input(f"{RED}╭──\n╰─>{RESET} {WHITE}enter username:{RESET} ").strip() or "ZeroBytes"
        usernames = [user]

    for user in usernames:
        dsherlock(user, jsonx=args.json, txt=args.txt)


if __name__ == "__main__":
    main()