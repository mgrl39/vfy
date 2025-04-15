import os
import random
import subprocess
import shutil
import datetime
from pathlib import Path

from .config import *
from .colors import *
from .progress import *
from .utils import *

def list_levels():
    """List all available levels"""
    if not BASE_DIR.exists():
        print_error(f"Exercise directory not found at {BASE_DIR}")
        return
    
    levels = sorted([d for d in BASE_DIR.iterdir() if d.is_dir()])
    if not levels:
        print_warning("No levels available.")
        return
    
    print_title("Available levels")
    for level in levels:
        ex_count = len([d for d in level.iterdir() if d.is_dir()])
        print(f"  {CYAN}{level.name}{RESET}: {YELLOW}{ex_count}{RESET} exercises")

def list_exercises(level):
    """List all exercises for a level"""
    level_path = BASE_DIR / f"level_{level}"
    if not level_path.exists():
        print_error(f"Level {level} not found.")
        return
    
    exercises = sorted([d for d in level_path.iterdir() if d.is_dir()])
    if not exercises:
        print_warning(f"No exercises in level {level}.")
        return
    
    progress = get_progress()
    completed = progress["completed"]
    
    print_title(f"Exercises in level {level}")
    for ex in exercises:
        try:
            with open(ex / "subject.txt") as f:
                first_line = f.readline().strip()
            status = f"{GREEN}[COMPLETED]{RESET} " if str(ex) in completed else f"{YELLOW}[PENDING]{RESET}   "
            print(f"  {status}{CYAN}{ex.name}{RESET}: {first_line[:50]}...")
        except FileNotFoundError:
            print(f"  {ex.name}: {RED}[No description available]{RESET}")

def get_current_exercise_path():
    """Get the path to the current exercise"""
    if not LAST_ASSIGNED_FILE.exists():
        return None
        
    with open(LAST_ASSIGNED_FILE) as f:
        return Path(f.read().strip())

def get_random_exercise(level):
    """Assign a random exercise from the specified level"""
    level_path = BASE_DIR / f"level_{level}"
    if not level_path.exists():
        print_error(f"Level {level} not found.")
        return

    exercises = [d for d in level_path.iterdir() if d.is_dir()]
    if not exercises:
        print_warning(f"No exercises in level {level}.")
        return

    chosen = random.choice(exercises)
    print_title(f"Exercise assigned: {chosen.name}")
    
    # Create working directory for this exercise
    working_dir = get_exercise_dir(chosen.name)
    print(f"{BLUE}Working directory{RESET}: {CYAN}{working_dir}{RESET}")
    
    try:
        with open(chosen / "subject.txt") as f:
            content = f.read()
        display_exercise_text(content)
    except FileNotFoundError:
        print_warning("Exercise description file not found.")

    # Make sure configuration directory exists
    CONFIG_DIR.mkdir(exist_ok=True)
    with open(LAST_ASSIGNED_FILE, "w") as f:
        f.write(str(chosen))
        
    # Update progress
    update_progress(chosen)
    
    print_info(f"Save your solution in: {BOLD}{working_dir / 'solution.c'}{RESET}")
    
    # Check if we already have a template to show
    solution_template = chosen / "template.c"
    if solution_template.exists():
        print_info("Here's a template to get you started:")
        with open(solution_template) as f:
            template = f.read()
        print(f"\n{PURPLE}```c{RESET}")
        print(template)
        print(f"{PURPLE}```{RESET}")
        
        # Copy template to working directory if it doesn't exist
        user_solution = working_dir / "solution.c"
        if not user_solution.exists():
            with open(user_solution, "w") as f:
                f.write(template)
            print_info(f"Template copied to {user_solution}")

def show_status():
    """Show the status of the current exercise"""
    ex_path = get_current_exercise_path()
    if not ex_path:
        print_warning("No exercise assigned. Use 'vfy get <level>' first.")
        return
        
    progress = get_progress()
    completed = progress["completed"]
    
    print_title("Current Exercise Status")
    print(f"{BLUE}Exercise{RESET}: {CYAN}{ex_path.name}{RESET}")
    print(f"{BLUE}Level{RESET}: {CYAN}{ex_path.parent.name}{RESET}")
    print(f"{BLUE}Status{RESET}: {GREEN}COMPLETED{RESET}" if str(ex_path) in completed else f"{BLUE}Status{RESET}: {YELLOW}PENDING{RESET}")
    
    # Working directory
    working_dir = get_exercise_dir(ex_path.name)
    print(f"{BLUE}Working directory{RESET}: {CYAN}{working_dir}{RESET}")
    
    # Check if solution exists
    solution = working_dir / "solution.c"
    if solution.exists():
        print(f"{BLUE}Solution{RESET}: {GREEN}EXISTS{RESET}")
        # Show size and modification date
        size = solution.stat().st_size
        modified = solution.stat().st_mtime
        mod_time = datetime.datetime.fromtimestamp(modified)
        print(f"{BLUE}Last modified{RESET}: {CYAN}{mod_time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
        print(f"{BLUE}Size{RESET}: {CYAN}{size} bytes{RESET}")
    else:
        print(f"{BLUE}Solution{RESET}: {RED}NOT FOUND{RESET}")

def check_solution():
    """Check the solution for the current exercise"""
    ex_path = get_current_exercise_path()
    if not ex_path:
        print_warning("No exercise assigned. Use 'vfy get <level>' first.")
        return

    # Get the working directory where the solution should be
    working_dir = get_exercise_dir(ex_path.name)
    solution = working_dir / "solution.c"
    expected = ex_path / "expected_output.txt"
    binary = working_dir / "solution.out"
    user_output = working_dir / "user_output.txt"
    diff_file = working_dir / "diff.txt"

    if not working_dir.exists():
        print_error(f"Working directory not found: {working_dir}")
        print_info(f"You might need to create it with: mkdir -p {working_dir}")
        return

    if not solution.exists():
        print_error(f"Solution not found at {solution}")
        print_info(f"Remember to save your code at {solution}")
        return

    if not expected.exists():
        print_error(f"Expected output file not found at {expected}")
        return

    # Compile
    print_info("Compiling your solution...")
    compile_cmd = [CC, str(solution), "-o", str(binary)]
    result = subprocess.run(compile_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print_error("Compilation error:")
        print(f"{RED}{result.stderr}{RESET}")
        return

    # Execute
    print_info("Running your program...")
    with open(user_output, "w") as f:
        subprocess.run([str(binary)], stdout=f)

    # Compare outputs
    print_info("Checking output...")
    with open(user_output) as uo, open(expected) as eo:
        user_lines = uo.readlines()
        expected_lines = eo.readlines()

    if user_lines == expected_lines:
        print_success("Your solution is correct!")
        # Mark as completed in progress
        update_progress(ex_path, completed=True)
        if diff_file.exists():
            diff_file.unlink()
    else:
        print_error("Output doesn't match expected result.")
        display_diff(expected_lines, user_lines, diff_file)

def open_exercise():
    """Open the current exercise in the default text editor"""
    ex_path = get_current_exercise_path()
    if not ex_path:
        print_warning("No exercise assigned. Use 'vfy get <level>' first.")
        return

    working_dir = get_exercise_dir(ex_path.name)
    solution = working_dir / "solution.c"
    
    # If file doesn't exist, copy template or create new
    if not solution.exists():
        template = ex_path / "template.c"
        if template.exists():
            shutil.copy(template, solution)
        else:
            # Create empty file with basic structure
            with open(solution, "w") as f:
                f.write("#include <stdio.h>\n\nint main(void) {\n    // Your code here\n    \n    return 0;\n}")
    
    # Open the file in default editor
    open_file_in_editor(solution)

def show_help():
    """Show program help"""
    print_title("vfy Usage")
    print(f"  {BOLD}{CYAN}vfy get <level>{RESET}      - Assign a random exercise from the specified level")
    print(f"  {BOLD}{CYAN}vfy check{RESET}            - Check the solution for the current exercise")
    print(f"  {BOLD}{CYAN}vfy list{RESET}             - List all available levels")
    print(f"  {BOLD}{CYAN}vfy list <level>{RESET}     - List all exercises in a level")
    print(f"  {BOLD}{CYAN}vfy status{RESET}           - Show status of current exercise")
    print(f"  {BOLD}{CYAN}vfy edit{RESET}             - Open current exercise in text editor")
    print(f"  {BOLD}{CYAN}vfy help{RESET}             - Show this help")
    
    print_title("Tips")
    print(f"  {YELLOW}•{RESET} All exercises are saved in {BOLD}{EXERCISES_DIR}{RESET}")
    print(f"  {YELLOW}•{RESET} Run {BOLD}vfy edit{RESET} to edit your solution")
    print(f"  {YELLOW}•{RESET} Run {BOLD}vfy check{RESET} to verify your solution")
    print(f"  {YELLOW}•{RESET} Use {BOLD}EDITOR=nano vfy edit{RESET} to use a specific editor") 