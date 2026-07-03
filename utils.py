
import subprocess
import shlex
import shutil


def run_command(cmd_str):
    """
    Runs a real Linux command and streams its output live to the terminal.
    cmd_str : the full command as a string, e.g. "nmap -sV 192.168.1.1"
    """
    print("\n[+] Running: " + cmd_str + "\n")
    print("-" * 60)
    try:
        cmd_list = shlex.split(cmd_str)
        subprocess.run(cmd_list)
    except FileNotFoundError:
        print("[!] Command not found twin. Is the required tool installed?")
    except KeyboardInterrupt:
        print("\n[!] Command interrupted by you twin.")
    except Exception as e:
        print(f"[!] Error running command: {e}")
    print("-" * 60)
    input("\nPress Enter to return to the menu twin...")


def check_tool_installed(tool_name):
    """Returns True if the given binary exists on the system PATH."""
    return shutil.which(tool_name) is not None


def ask(prompt_text):
    """Simple wrapper around input() so every module asks questions the same way."""
    return input(prompt_text).strip()


def print_flag_menu(title, options):
    """
    Prints a numbered flag menu.
    options: list of tuples (label, flag_string)
    Returns the list so the caller can index into it after asking for a choice.
    """
    print(f"\n{title}")
    print("-" * len(title))
    for i, (label, _) in enumerate(options, start=1):
        print(f"[{i}] {label}")
    print(f"[{len(options)+1}] Custom flags (type your own)")
    return options

#CREATED BY MAHZEND
