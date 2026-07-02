"""
modules/nmap_tool.py
Asks for a target IP, then a flag choice, then runs nmap.
"""

from utils import ask, run_command, print_flag_menu, check_tool_installed

FLAG_OPTIONS = [
    ("Quick scan (fast, common ports)", "-T4 -F"),
    ("Service/version detection", "-sV"),
    ("OS detection", "-O"),
    ("Aggressive scan (OS + version + script + traceroute)", "-A"),
    ("Full port scan (all 65535 ports)", "-p-"),
    ("Ping scan only (host discovery, no port scan)", "-sn"),
]


def run():
    if not check_tool_installed("nmap"):
        print("[!] nmap is not installed. Install it with: sudo apt install nmap")
        input("Press Enter to return to the menu...")
        return

    print("\n=== NMAP ===")
    target = ask("Enter target IP address or hostname: ")
    if not target:
        print("[!] No target entered. Returning to menu.")
        return

    print_flag_menu("Choose a scan type", FLAG_OPTIONS)
    choice = ask("Select an option: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        flags = FLAG_OPTIONS[int(choice) - 1][1]
    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        flags = ask("Enter custom nmap flags (e.g. -sS -p 22,80,443): ")
    else:
        print("[!] Invalid choice. Returning to menu.")
        return

    cmd = f"nmap {flags} {target}"
    run_command(cmd)
