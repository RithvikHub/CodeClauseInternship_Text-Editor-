# ----------------------------
# Simple Text Editor - Notepad Clone
# By: Rithvik Reddy Gudipati
# CodeClause Internship Project
# ----------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Create the main window
app = tk.Tk()
app.title("Text Editor - Rithvik")
app.geometry("700x500")

# Create the Text widget for typing area
text_area = tk.Text(app, wrap="word", font=("Arial", 12))
text_area.pack(expand=1, fill="both")

# ----------------------------
# Functions
# ----------------------------

def new_file():
    text_area.delete(1.0, tk.END)
    app.title("Untitled - Text Editor")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
        app.title(os.path.basename(file_path) + " - Text Editor")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        app.title(os.path.basename(file_path) + " - Text Editor")
        messagebox.showinfo("Saved", "File saved successfully!")

def exit_app():
    app.destroy()

# ----------------------------
# Menu Bar
# ----------------------------

menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

# ----------------------------
# Run the Application
# ----------------------------

app.mainloop()
