# net-toolkit

A simple Python-based menu interface that wraps common Linux networking
commands (`nmap`, `whois`, `nslookup`, `ip addr`, `nc`) behind an easy
numbered menu. Each tool asks for a target and lets you pick from a
list of common flags (or type your own), runs the real command, shows
you the output, then returns to the main menu.

## Requirements

- Linux (Debian/Ubuntu commands shown below)
- Python 3.6+
- The underlying command-line tools installed:

```bash
sudo apt update
sudo apt install nmap whois dnsutils iproute2 netcat curl -y
```

## Project structure

```
net-toolkit/
├── main.py                 # menu loop, dispatches to each tool
├── banner.py                # your ASCII art lives here
├── utils.py                 # shared helpers (run_command, ask, etc.)
├── modules/
│   ├── __init__.py
│   ├── nmap_tool.py
│   ├── whois_tool.py
│   ├── nslookup_tool.py
│   ├── ipaddr_tool.py
│   └── nc_tool.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/net-toolkit.git
   cd net-toolkit
   ```
2. Paste your ASCII art into `banner.py`, inside the `BANNER` string.
3. Run it:
   ```bash
   python3 main.py
   ```
   Some operations (nmap SYN scans, nc listening on ports < 1024) need
   root, so run with `sudo python3 main.py` if you hit permission errors.

## How each tool works

Every tool module follows the same pattern:
1. Ask for a target (IP / domain / port).
2. Show a numbered list of common flags for that command, plus a
   "Custom flags" option to type your own.
3. Build the final command string and run it with `subprocess`.
4. Print the real command output, then wait for Enter before
   returning to the main menu.

## Procedure: adding a new tool to the menu

Say you want to add a 6th option, e.g. `traceroute`. Follow these steps:

### 1. Create the new module file

Create `modules/traceroute_tool.py` and copy the pattern used by the
other tools:

```python
"""
modules/traceroute_tool.py
"""

from utils import ask, run_command, print_flag_menu, check_tool_installed

FLAG_OPTIONS = [
    ("Basic traceroute", ""),
    ("Use ICMP instead of UDP (-I)", "-I"),
    ("Set max hops (-m)", "-m"),
]


def run():
    if not check_tool_installed("traceroute"):
        print("[!] traceroute is not installed. Install it with: sudo apt install traceroute")
        input("Press Enter to return to the menu...")
        return

    print("\n=== TRACEROUTE ===")
    target = ask("Enter target IP or hostname: ")
    if not target:
        print("[!] No target entered. Returning to menu.")
        return

    print_flag_menu("Choose an option", FLAG_OPTIONS)
    choice = ask("Select an option: ")

    if choice.isdigit() and 1 <= int(choice) <= len(FLAG_OPTIONS):
        flags = FLAG_OPTIONS[int(choice) - 1][1]
        if flags == "-m":
            hops = ask("Enter max hops (e.g. 15): ")
            flags = f"-m {hops}"
    elif choice.isdigit() and int(choice) == len(FLAG_OPTIONS) + 1:
        flags = ask("Enter custom traceroute flags: ")
    else:
        print("[!] Invalid choice. Returning to menu.")
        return

    cmd = f"traceroute {flags} {target}".replace("  ", " ")
    run_command(cmd)
```

### 2. Import it in `main.py`

```python
from modules import nmap_tool, whois_tool, nslookup_tool, ipaddr_tool, nc_tool, traceroute_tool
```

### 3. Register it in the `MENU_ITEMS` list in `main.py`

```python
MENU_ITEMS = [
    ("NMAP", nmap_tool.run),
    ("WHOIS", whois_tool.run),
    ("NSLOOKUP", nslookup_tool.run),
    ("IP ADDRESS", ipaddr_tool.run),
    ("NC (Netcat)", nc_tool.run),
    ("TRACEROUTE", traceroute_tool.run),   # <-- new line
]
```

That's it — `main.py` automatically numbers the menu based on the
list, so your new tool shows up as the next number with zero other
changes needed.

### Rules of thumb for any new module

- Always guard with `check_tool_installed("<binary>")` first so users
  get a clear "install this" message instead of a crash.
- Always build the command as a single string and pass it to
  `run_command()` from `utils.py` — it handles the actual execution.
- Always give a "Custom flags" fallback option so advanced users
  aren't limited to your presets.
- Keep each module's `run()` function taking no arguments and
  returning `None`, so it plugs straight into `MENU_ITEMS`.

## Disclaimer

These tools (especially `nmap` and `nc`) can be used for network
scanning and access. Only run them against systems and networks you
own or have explicit permission to test.
