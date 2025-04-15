import os
import shutil
import subprocess
from pathlib import Path
from difflib import unified_diff

from .config import EXERCISES_DIR
from .colors import *

def get_exercise_dir(exercise_name):
    """Get the working directory for an exercise"""
    # Create directory in EXERCISES_DIR with exercise name
    exercise_dir = EXERCISES_DIR / exercise_name
    exercise_dir.mkdir(exist_ok=True)
    return exercise_dir

def display_exercise_text(content, width=80):
    """Display exercise text with a nice border"""
    print(f"\n{CYAN}╔{'═' * (width-2)}╗{RESET}")
    for line in content.split('\n'):
        # Wrap long lines
        while line and len(line) > width-4:
            print(f"{CYAN}║{RESET} {line[:width-4]} {CYAN}║{RESET}")
            line = line[width-4:]
        if line:
            print(f"{CYAN}║{RESET} {line}{' ' * (width-4-len(line))} {CYAN}║{RESET}")
    print(f"{CYAN}╚{'═' * (width-2)}╝{RESET}\n")

def display_diff(expected_lines, user_lines, diff_file):
    """Display colorized diff between expected and actual output"""
    # Write diff to file
    with open(diff_file, "w") as f:
        diff = unified_diff(expected_lines, user_lines,
                            fromfile="expected", tofile="your_output")
        f.writelines(diff)
    
    # Show a more detailed diff with colors
    print_title("Diff Details")
    print(f"{BLUE}Expected output{RESET} vs {YELLOW}Your output{RESET}:")
    
    for line in unified_diff(expected_lines, user_lines,
                           fromfile="expected", tofile="your_output"):
        if line.startswith('+'):
            print(f"{GREEN}{line.rstrip()}{RESET}")
        elif line.startswith('-'):
            print(f"{RED}{line.rstrip()}{RESET}")
        elif line.startswith('@@'):
            print(f"{CYAN}{line.rstrip()}{RESET}")
        else:
            print(line.rstrip())
            
    print(f"\nCheck {BOLD}{diff_file}{RESET} for full details")

def open_file_in_editor(file_path):
    """Open a file in the default editor"""
    editor = os.getenv("EDITOR", "vi")  # Use EDITOR or vi by default
    try:
        subprocess.run([editor, file_path])
        return True
    except Exception as e:
        print_error(f"Error opening editor: {e}")
        print_info(f"You can edit the file manually at: {file_path}")
        return False 