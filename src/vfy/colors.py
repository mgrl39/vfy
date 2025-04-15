# Colors and formatting
RED    = "\033[0;31m"
GREEN  = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE   = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN   = "\033[0;36m"
WHITE  = "\033[0;37m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def print_title(text):
    """Print a nicely formatted title"""
    print(f"\n{BOLD}{CYAN}=== {text} ==={RESET}\n")

def print_success(text):
    """Print a success message"""
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    """Print an error message"""
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    """Print a warning message"""
    print(f"{YELLOW}⚠️ {text}{RESET}")

def print_info(text):
    """Print an info message"""
    print(f"{BLUE}ℹ️ {text}{RESET}") 