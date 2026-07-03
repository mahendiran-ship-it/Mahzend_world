

from utils import ask, run_command, print_flag_menu, check_tool_installed

FLAG_OPTIONS = [
    ("Listen on a port (server mode: -lvnp)", "LISTEN"),
    ("Connect to a host:port (client mode: -v)", "CONNECT"),
    ("Port scan a host with nc (-zv)", "SCAN"),
]


def run():
    if not check_tool_installed("nc"):
        print("[!] nc (netcat) is not installed twin . Install it with: sudo apt install netcat")
        input("Press Enter to return to the menu twin...")
        return

    print("\n=== NETCAT (nc) ===")
    print_flag_menu("Choose a mode twin", FLAG_OPTIONS)
    choice = ask("Select an option twin: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        mode = FLAG_OPTIONS[int(choice) - 1][1]

        if mode == "LISTEN":
            port = ask("Enter port number to listen on (e.g. 4444): ")
            cmd = f"nc -lvnp {port}"

        elif mode == "CONNECT":
            host = ask("Enter target host/IP twin: ")
            port = ask("Enter target port twin: ")
            cmd = f"nc -v {host} {port}"

        elif mode == "SCAN":
            host = ask("Enter target host/IP: ")
            port_range = ask("Enter port or port range (e.g. 20-80): ")
            cmd = f"nc -zv {host} {port_range}"

        run_command(cmd)
        return

    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        custom = ask("Enter full custom nc arguments (e.g. -lvnp 8080): ")
        cmd = f"nc {custom}"
        run_command(cmd)
        return

    else:
        print("[!] Invalid choice. Returning to menu twin.")


#CREATED BY MAHZEND
