"""
modules/nslookup_tool.py
Asks for a site, then a DNS record type / flag choice, then runs nslookup.
"""

from utils import ask, run_command, print_flag_menu, check_tool_installed

FLAG_OPTIONS = [
    ("Default lookup (A record)", ""),
    ("MX records (mail servers)", "-type=MX"),
    ("NS records (name servers)", "-type=NS"),
    ("TXT records", "-type=TXT"),
    ("Query a specific DNS server", "SERVER"),
]


def run():
    if not check_tool_installed("nslookup"):
        print("[!] nslookup is not installed. Install it with: sudo apt install dnsutils")
        input("Press Enter to return to the menu...")
        return

    print("\n=== NSLOOKUP ===")
    target = ask("Enter website / domain (e.g. example.com): ")
    if not target:
        print("[!] No target entered. Returning to menu.")
        return

    print_flag_menu("Choose a query type", FLAG_OPTIONS)
    choice = ask("Select an option: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        flags = FLAG_OPTIONS[int(choice) - 1][1]
        if flags == "SERVER":
            dns_server = ask("Enter DNS server (e.g. 8.8.8.8): ")
            cmd = f"nslookup {target} {dns_server}"
            run_command(cmd)
            return
    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        flags = ask("Enter custom nslookup flags: ")
    else:
        print("[!] Invalid choice. Returning to menu.")
        return

    cmd = f"nslookup {flags} {target}".replace("  ", " ")
    run_command(cmd)
