#!/usr/bin/env python3
"""
WH_toolkit.py
Entry point for WH TOOL KIT. Shows the banner + main menu and dispatches
to the correct tool module based on the user's choice.

Run with:  python3 WH_toolkit.py
(some options like nmap SYN scan or nc listen on low ports may need sudo)
"""

import os
import sys

from banner import print_banner
import nmap_tool, whois_tool, nslookup_tool, ipaddr_tool, nc_tool

MENU_ITEMS = [
    ("NMAP", nmap_tool.run),
    ("WHOIS", whois_tool.run),
    ("NSLOOKUP", nslookup_tool.run),
    ("IP ADDRESS", ipaddr_tool.run),
    ("NC (Netcat)", nc_tool.run),
]


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def print_menu():
    print_banner()
    name=input("ENTER YOUR NAME TWIN:")
    print("MAIN MENU")
    print("=========")
    for i, (label, _) in enumerate(MENU_ITEMS, start=1):
        print(f"[{i}] {label}")
    print(f"[{len(MENU_ITEMS) + 1}] Exit")
    print()


def main():
    while True:
        clear_screen()
        print_menu()
        choice = input(f"Select an option {name}: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(MENU_ITEMS):
            clear_screen()
            MENU_ITEMS[int(choice) - 1][1]()
        elif choice.isdigit() and int(choice) == len(MENU_ITEMS) + 1:
            print(f"Goodbye {name}")
            sys.exit(0)
        else:
            input(f"[!] Invalid choice. Press Enter to try again {name} ...")


if __name__ == "__main__":
    main()
