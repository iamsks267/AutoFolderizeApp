import tkinter as tk
from tkinter import messagebox, filedialog
from pathlib import Path
import calendar

def create_folders():
    year = entry_year.get()
    
    if not year.isdigit() or len(year) != 4:
        messagebox.showerror("Invalid Input", "Please enter a valid 4-digit year.")
        # return
    
    # Open a dialog for folder selection
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        messagebox.showwarning("No Folder", "No folder selected!")
        return

    months_names = list(calendar.month_name[1:])
    days = ['Day1-Day7','Day8-Day14','Day15-Day21','Day22-Day28','Day29-LastDay']
    
    try:
        for i, month in enumerate(months_names):
            for day in days:
                Path(f'{folder_path}/{year}/{i+1}. {month}/{day}').mkdir(parents=True, exist_ok=True)
        messagebox.showinfo("Success", "Folders created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the tkinter window
root = tk.Tk()
root.title("Folder Structure Creator")

# Label and entry for year input
label_year = tk.Label(root, text="Enter the year for folder creation:")
label_year.pack(pady=10)

entry_year = tk.Entry(root)
entry_year.pack(pady=5)

# Button to trigger folder creation
btn_create = tk.Button(root, text="Create Folders", command=create_folders)
btn_create.pack(pady=20)

# Run the tkinter loop
root.mainloop()