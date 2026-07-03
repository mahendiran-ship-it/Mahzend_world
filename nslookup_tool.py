
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
        print("[!] nslookup is not installed twin. Install it with: sudo apt install dnsutils")
        input("Press Enter to return to the menu twin...")
        return

    print("\n=== NSLOOKUP ===")
    target = ask("Enter website / domain (e.g. Darkweb.com) twin: ")
    if not target:
        print("[!] No target entered. Returning to menu twin.")
        return

    print_flag_menu("Choose a query type twin", FLAG_OPTIONS)
    choice = ask("Select an option twin: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        flags = FLAG_OPTIONS[int(choice) - 1][1]
        if flags == "SERVER":
            dns_server = ask("Enter DNS server (e.g. 8.8.8.8) twin: ")
            cmd = f"nslookup {target} {dns_server}"
            run_command(cmd)
            return
    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        flags = ask("Enter custom nslookup flags twin: ")
    else:
        print("[!] Invalid choice. Returning to menu twin.")
        return

    cmd = f"nslookup {flags} {target}".replace("  ", " ")
    run_command(cmd)


#CREATED BY MAHZEND
