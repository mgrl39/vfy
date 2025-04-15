import os
from pathlib import Path

# Use a standard location for files
HOME = Path.home()
BASE_DIR = Path(os.getenv("VFY_SUBJECTS_DIR", HOME / ".vfy/subjects"))
CONFIG_DIR = HOME / ".vfy"
EXERCISES_DIR = HOME / "vfy_exercises"  # Specific directory for exercises
LAST_ASSIGNED_FILE = CONFIG_DIR / ".last_exercise"
PROGRESS_FILE = CONFIG_DIR / "progress.json"
CC = os.getenv("CC", "cc")  # Use CC environment variable if set, otherwise use cc 