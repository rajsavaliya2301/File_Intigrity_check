import hashlib
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Create hash of a file
def get_file_hash(path):
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

# Make a dictionary of file hashes
def scan_folder(folder):
    hashes = {}
    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, folder)
            hashes[rel_path] = get_file_hash(full_path)
    return hashes

# GUI Application
class IntegrityChecker:
    def __init__(self, root):
        self.root = root
        root.title("Simple Integrity Checker")

        self.folder = ''
        self.hash_file = 'hashes.json'

        tk.Button(root, text="Choose Folder", command=self.choose_folder).pack(pady=5)
        tk.Button(root, text="Save Baseline", command=self.save_baseline).pack(pady=5)
        tk.Button(root, text="Check Changes", command=self.check_changes).pack(pady=5)

        self.output = scrolledtext.ScrolledText(root, width=70, height=20)
        self.output.pack(pady=10)

    def choose_folder(self):
        self.folder = filedialog.askdirectory()
        self.log(f"Folder selected: {self.folder}")

    def save_baseline(self):
        if not self.folder:
            messagebox.showerror("Error", "Please select a folder first.")
            return
        hashes = scan_folder(self.folder)
        with open(self.hash_file, 'w') as f:
            json.dump(hashes, f, indent=4)
        self.log("Baseline saved successfully.")

    def check_changes(self):
        if not self.folder:
            messagebox.showerror("Error", "Please select a folder first.")
            return

        if not os.path.exists(self.hash_file):
            messagebox.showerror("Error", "No baseline found. Please save it first.")
            return

        with open(self.hash_file, 'r') as f:
            old_hashes = json.load(f)
        new_hashes = scan_folder(self.folder)

        old_files = set(old_hashes)
        new_files = set(new_hashes)

        added = new_files - old_files
        removed = old_files - new_files
        modified = [f for f in old_files & new_files if old_hashes[f] != new_hashes[f]]

        self.log("=== Integrity Check Report ===")
        if added:
            self.log(f"[+] Added: {', '.join(added)}")
        if removed:
            self.log(f"[-] Removed: {', '.join(removed)}")
        if modified:
            self.log(f"[!] Modified: {', '.join(modified)}")
        if not (added or removed or modified):
            self.log("[✓] No changes detected.")
    def log(self, message):
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)

# Run the app
if __name__ == '__main__':
    root = tk.Tk()
    app = IntegrityChecker(root)
    root.mainloop()
