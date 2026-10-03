<div align="center">
  <img width="737" height="461" alt="image" src="https://github.com/user-attachments/assets/933fdc70-e167-49da-be75-d9fdec9f1867" />
</div>

# New folder (3) 📂
---

Don't judge a book by its cover, or a repository by its name. **New folder (3)** is my official **Project Cemetery and Automation Lab** — a curated monorepo where all your loose scripts, scrapers, utility tools, and half-baked ideas on your File Explorer come together to serve a purpose.

Instead of letting useful code rot in forgotten directories on your local PC, everything is organized, documented, and version-controlled right here.

---

## 🗺️ Repository Structure

*   📂 `automations/` — Scripts that handle repetitive daily digital tasks.
*   📂 `scrapers/` — Web scraping tools and data extraction experiments.
*   📂 `utils/` — Command-line utilities, text formatting toolkits, and quick helpers.
*   📂 `abandoned/` — Projects that were too big to finish but contain snippet gems worth keeping.

---

## 🚀 Featured Tool: File Organizer (`organizer.py`)

The first official resident of this folder is a fully functional script designed to clean up messy directories (like your cluttered Desktop or Downloads folder) by sorting loose files into categorized subfolders automatically.

### How to Run it

1. Clone this repository:
   ```bash
   git clone https://github.com
   cd New-folder-3
   ```

2. Open `organizer.py` and modify the `TARGET_DIR` path to target your desired messy folder:
   ```python
   TARGET_DIR = Path.home() / "Downloads"
   ```

3. Run the script:
   ```bash
   python organizer.py
   ```

---

## 🛠️ Tech Stack Used Across Scripts
*   **Language:** Python / Bash / Node.js
*   **Main Modules:** `os`, `shutil`, `pathlib`, `requests`

---
