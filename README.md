# File_Intigrity_check
to check file update or change in a folder via a hash value
# 🔐 File Integrity Checker (Simple GUI Tool)

A simple Python-based GUI application that monitors the integrity of files in a selected directory by computing and comparing SHA-256 hashes. Useful for detecting unexpected changes, additions, or deletions in important folders.

---

## 🚀 Features

- Select any folder to monitor.
- Generate a **baseline** (initial hash record).
- Check for:
  - ✅ Added files
  - ✅ Removed files
  - ✅ Modified files
- Clear output report in a scrollable text box.
- Lightweight and beginner-friendly GUI built with `tkinter`.

---

## 🛠️ How It Works

1. **Choose Folder**: Select a directory to monitor.
2. **Save Baseline**: The program scans all files and stores their hashes in a file named `hashes.json`.
3. **Check Changes**: Compares the current state of the folder with the saved baseline and reports any differences.

---

## 📦 Requirements

- Python 3.6 or higher

No external libraries required. All dependencies are part of the Python standard library:
- `hashlib`
- `os`
- `json`
- `tkinter`

---

## 🧪 Usage

### Run the App

```bash
python integrity_checker.py
```
📝 Example Output

Folder selected: /Users/yourname/Documents/important_data
Baseline saved successfully.
=== Integrity Check Report ===
Added files: report2.docx
Modified files: notes.txt
Removed files: summary.xlsx
