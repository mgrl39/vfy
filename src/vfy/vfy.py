#!/usr/bin/python3
import sys
import os
from pathlib import Path

# Ensure we can import from src/ directory
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))

# Import our modules
from config import EXERCISES_DIR
from colors import print_error, print_success, print_title
from progress import setup_progress
from commands import *

def main():
    """Main entry point for vfy command"""
    # Create necessary directories
    EXERCISES_DIR.mkdir(exist_ok=True, parents=True)
    setup_progress()
    
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    cmd = sys.argv[1]

    try:
        if cmd == "get" and len(sys.argv) >= 3:
            get_random_exercise(sys.argv[2])
        elif cmd == "check":
            check_solution()
        elif cmd == "status":
            show_status()
        elif cmd == "edit":
            open_exercise()
        elif cmd == "list":
            if len(sys.argv) >= 3:
                list_exercises(sys.argv[2])
            else:
                list_levels()
        elif cmd == "create":
            create_exercise()
        elif cmd == "config":
            if len(sys.argv) == 2:
                show_config()
            elif len(sys.argv) >= 4:
                set_config(sys.argv[2], sys.argv[3])
            else:
                print_error("Usage: vfy config <key> <value>")
        elif cmd == "help":
            show_help()
        else:
            print_error("Invalid command.")
            show_help() 
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")
        # For debugging:
        # import traceback
        # traceback.print_exc()

if __name__ == "__main__":
    main() 