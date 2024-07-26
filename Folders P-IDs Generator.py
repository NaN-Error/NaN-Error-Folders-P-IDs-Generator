import os
import string
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_product_ids(start, end):
    def increment_pid(pid):
        if pid[-1] == 'Z':
            if pid[-2] == 'Z':
                return pid[0] + chr(ord(pid[1]) + 1) + '0'
            return pid[0] + chr(ord(pid[1]) + 1) + '0'
        if pid[-1] == '9':
            return pid[:-1] + 'A'
        return pid[:-1] + chr(ord(pid[-1]) + 1)
    
    product_ids = []
    current_pid = start
    while current_pid != end:
        product_ids.append(current_pid)
        current_pid = increment_pid(current_pid)
    product_ids.append(end)  # Include the end product ID in the list
    return product_ids

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_var.set(folder_path)

def start_program():
    start_pid = start_entry.get().strip()
    end_pid = end_entry.get().strip()
    folder_path = folder_var.get().strip()
    
    if not start_pid or not end_pid or not folder_path:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    product_ids = generate_product_ids(start_pid, end_pid)
    created_count = 0
    
    for pid in product_ids:
        folder_exists = False
        for folder in os.listdir(folder_path):
            if folder.startswith(pid):
                folder_exists = True
                break
        if not folder_exists:
            os.makedirs(os.path.join(folder_path, pid))
            created_count += 1
    
    messagebox.showinfo("Success", f"{created_count} folders created successfully!")

# Setup GUI
root = tk.Tk()
root.title("Product ID Folder Generator")

tk.Label(root, text="Start Product ID:").grid(row=0, column=0, padx=10, pady=5)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="End Product ID:").grid(row=1, column=0, padx=10, pady=5)
end_entry = tk.Entry(root)
end_entry.grid(row=1, column=1, padx=10, pady=5)

folder_var = tk.StringVar()
tk.Button(root, text="Select Folder", command=select_folder).grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=folder_var, state='readonly').grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Start", command=start_program).grid(row=3, columnspan=2, pady=10)

root.mainloop()
