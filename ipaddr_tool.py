

from utils import ask, run_command, print_flag_menu, check_tool_installed

FLAG_OPTIONS = [
    ("Show all interfaces (ip addr show)", "addr show"),
    ("Show a specific interface", "IFACE"),
    ("Show routing table (ip route)", "route"),
    ("Show public IP (curl ifconfig.me)", "PUBLIC"),
]


def run():
    print("\n=== IP ADDRESS INFO ===")
    print_flag_menu("Choose what to display twin", FLAG_OPTIONS)
    choice = ask("Select an option twin: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        flags = FLAG_OPTIONS[int(choice) - 1][1]

        if flags == "IFACE":
            iface = ask("Enter interface name (e.g. eth0, wlan0) twin: ")
            cmd = f"ip addr show {iface}"
            run_command(cmd)
            return

        if flags == "PUBLIC":
            if not check_tool_installed("curl"):
                print("[!] curl is not installed twin. Install it with: sudo apt install curl")
                input("Press Enter to return to the menu twin...")
                return
            cmd = "curl -s ifconfig.me"
            run_command(cmd)
            return

        cmd = f"ip {flags}"
        run_command(cmd)
        return

    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        flags = ask("Enter custom 'ip' command flags (e.g. -s link show) twin: ")
        cmd = f"ip {flags}"
        run_command(cmd)
        return

    else:
        print("[!] Invalid choice. Returning to menu twin.")


#CREATED BY MAHZEND
