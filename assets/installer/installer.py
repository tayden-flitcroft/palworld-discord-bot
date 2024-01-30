import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def get_bundle_dir():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return base_path

def copy_files(source_directory, destination_directory, status_label):
    try:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        for filename in os.listdir(source_directory):
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, destination_directory)
        status_label.config(text="Mods copied successfully.")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_directory(entry_widget):
    directory = filedialog.askdirectory(initialdir="C:/", title="Select Destination Folder")
    if directory:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, directory)

def parse_vdf(path):
    libraries = []
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if '"path"' in line:
                    path = line.split('"')[3].replace('\\\\', '\\')
                    libraries.append(path)
        return libraries
    except Exception as e:
        messagebox.showerror("Error", f"Could not parse libraryfolders.vdf: {e}")
        return []

def find_palworld_library():
    possible_steam_paths = [
        os.path.expanduser("~\Steam\steamapps\libraryfolders.vdf"),
        "C:\Program Files (x86)\Steam\steamapps\libraryfolders.vdf",
        "C:\Program Files\Steam\steamapps\libraryfolders.vdf"
    ]
    for steam_path in possible_steam_paths:
        if os.path.exists(steam_path):
            libraries = parse_vdf(steam_path)
            for lib in libraries:
                palworld_path = os.path.join(lib, "steamapps", "common", "Palworld", "Pal", "Content", "Paks")
                if os.path.exists(palworld_path):
                    return palworld_path
    return None

def create_gui():
    root = tk.Tk()
    root.title("Palworld Mod Installer")

    tk.Label(root, text="Select Destination Directory for Palworld Mods:").pack(pady=10)
    tk.Label(root, text="Ensure the installation folder is the '\Pal\Content\Paks' folder inside the Palworld game directory.").pack()

    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    default_path = find_palworld_library()
    if default_path:
        entry.insert(0, default_path)
    else:
        entry.insert(0, "Palworld directory not found, please select manually")

    tk.Button(root, text="Browse", command=lambda: select_directory(entry)).pack(pady=5)

    status_label = tk.Label(root, text="", fg="red")
    status_label.pack(pady=10)

    source_dir = os.path.join(get_bundle_dir(), 'mods')

    tk.Button(root, text="Install Mods", command=lambda: copy_files(source_dir, entry.get(), status_label)).pack(pady=10)

    root.mainloop()

create_gui()