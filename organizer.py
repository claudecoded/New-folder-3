import os
import shutil
from pathlib import Path

# --- CONFIGURATION ---
# Replace with the path you want to clean up (e.g., your Downloads folder)
# Example: TARGET_DIR = Path.home() / "Downloads"
TARGET_DIR = Path("./test_cleanup_folder") 

# Mapping of file extensions to target directories
TRACKED_EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Audio_Video": [".mp3", ".wav", ".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code_Files": [".py", ".js", ".html", ".css", ".json", ".sh"]
}

def setup_environment():
    """Creates the target directory for testing if it doesn't exist."""
    if not TARGET_DIR.exists():
        TARGET_DIR.mkdir(parents=True, exist_ok=True)
        # Create a dummy file for testing purposes
        (TARGET_DIR / "dummy_notes.txt").write_text("Hello World!")
        (TARGET_DIR / "sample_image.png").write_text("")
        print(f" [INFO] Created sample folder at '{TARGET_DIR}' with mock files for testing.")

def clean_directory():
    """Scans the target directory and organizes files by category."""
    print(f"🧹 Starting cleanup in: {TARGET_DIR.resolve()}\n")
    
    if not any(TARGET_DIR.iterdir()):
        print(" Looking clean! No files found to organize.")
        return

    moved_count = 0

    for item in TARGET_DIR.iterdir():
        # Skip directories to avoid accidental nested moving
        if item.is_dir():
            continue
            
        file_extension = item.suffix.lower()
        moved = False

        for category, extensions in TRACKED_EXTENSIONS.items():
            if file_extension in extensions:
                category_folder = TARGET_DIR / category
                category_folder.mkdir(exist_ok=True)
                
                destination = category_folder / item.name
                
                try:
                    shutil.move(str(item), str(destination))
                    print(f" [MOVED] {item.name} ➡️  {category}/{item.name}")
                    moved_count += 1
                    moved = True
                    break
                except Exception as e:
                    print(f" [ERROR] Could not move {item.name}: {e}")
                    
        if not moved and file_extension:
            # Move unknown file extensions to an 'Others' folder
            others_folder = TARGET_DIR / "Others"
            others_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(others_folder / item.name))
                print(f" [MOVED] {item.name} ➡️  Others/{item.name}")
                moved_count += 1
            except Exception as e:
                print(f" [ERROR] Could not move {item.name}: {e}")

    print(f"\n Clean completed! Total files organized: {moved_count}")

if __name__ == "__main__":
    # Sets up fake files if you just run it standalone to test
    setup_environment()
    # Runs the actual organizer logic
    clean_directory()
