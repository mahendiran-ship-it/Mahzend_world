"""
modules/whois_tool.py
Asks for a domain/website, then a flag choice, then runs whois.
"""

from utils import ask, run_command, print_flag_menu, check_tool_installed

FLAG_OPTIONS = [
    ("Basic whois lookup", ""),
    ("Hide legal disclaimers (-H)", "-H"),
    ("Query a specific whois server (-h)", "-h"),
]


def run():
    if not check_tool_installed("whois"):
        print("[!] whois is not installed. Install it with: sudo apt install whois")
        input("Press Enter to return to the menu...")
        return

    print("\n=== WHOIS ===")
    target = ask("Enter website / domain (e.g. example.com): ")
    if not target:
        print("[!] No target entered. Returning to menu.")
        return

    print_flag_menu("Choose a lookup type", FLAG_OPTIONS)
    choice = ask("Select an option: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        flags = FLAG_OPTIONS[int(choice) - 1][1]
        if flags == "-h":
            server = ask("Enter whois server (e.g. whois.iana.org): ")
            flags = f"-h {server}"
    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        flags = ask("Enter custom whois flags: ")
    else:
        print("[!] Invalid choice. Returning to menu.")
        return

    cmd = f"whois {flags} {target}".replace("  ", " ")
    run_command(cmd)
