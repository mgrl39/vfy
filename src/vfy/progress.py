import json
from pathlib import Path
from config import CONFIG_DIR, PROGRESS_FILE

def setup_progress():
    """Ensure progress file exists"""
    CONFIG_DIR.mkdir(exist_ok=True)
    
    # Initialize progress file if it doesn't exist
    if not PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "w") as f:
            json.dump({"completed": [], "current": None}, f)
            
def get_progress():
    """Get user progress"""
    if not PROGRESS_FILE.exists():
        return {"completed": [], "current": None}
    
    try:
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If file is corrupt, create a new one
        with open(PROGRESS_FILE, "w") as f:
            data = {"completed": [], "current": None}
            json.dump(data, f)
        return data
        
def update_progress(exercise_path, completed=False):
    """Update user progress"""
    progress = get_progress()
    exercise_str = str(exercise_path)
    
    if completed and exercise_str not in progress["completed"]:
        progress["completed"].append(exercise_str)
        
    progress["current"] = exercise_str
    
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f) 