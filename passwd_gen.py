import tkinter as tk
from tkinter import ttk
import random
import string
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF
from ttkbootstrap import Style

password_generated = False

def generate_password():
    global password_generated
    password_length = length_entry.get()
    if not password_length:
        messagebox.showwarning("Warning", "Please input Password Length")
        return

    password_length = int(password_length)
    complexity = ""
    if uppercase_var.get():
        complexity += string.ascii_uppercase
    if lowercase_var.get():
        complexity += string.ascii_lowercase
    if digits_var.get():
        complexity += string.digits
    if special_chars_var.get():
        complexity += string.punctuation

    password = ''.join(random.choice(complexity) for _ in range(password_length))
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state=tk.DISABLED)
    password_generated = True

def save_to_file():
    global password_generated
    if not password_generated:
        messagebox.showerror("Error", "No password generated yet!")
        return

    password = password_display.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])

    if file_path:
        if file_path.endswith(".pdf"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Generated Password", ln=True)
            pdf.cell(200, 10, txt=password, ln=True)
            pdf.output(file_path)
        else:
            with open(file_path, "w") as file:
                file.write(password)

def copy_to_clipboard():
    global password_generated
    if not password_generated:
        messagebox.showerror("Error", "No password generated yet!")
        return

    password = password_display.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard!")

def clear_password():
    global password_generated
    if not password_generated:
        messagebox.showerror("Error", "No password generated yet!")
        return

    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.config(state=tk.DISABLED)
    password_generated = False

def show_about():
    messagebox.showinfo("About", "Password Generator App\nAuthor: Raymond C. Turner.\nApp Version 1.1.0")

root = tk.Tk()
root.title("PassGen")

# Set minimum and maximum window size
root.minsize(width=400, height=500)  # Change these values as needed
root.maxsize(width=700, height=800)  # Change these values as needed

# Create ttkbootstrap style
style = Style(theme="darkly")  # Change the theme as desired

# Title bar
title_frame = ttk.Frame(root, padding=(10, 5))  # Using ttk.Frame
title_frame.pack(fill=tk.X)

title_label = ttk.Label(title_frame, text="PassGen", font=("Helvecta", 12), foreground="white")  # Using ttk.Label
title_label.pack(side=tk.LEFT)

about_button = ttk.Button(title_frame, text="About", command=show_about)  # Using ttk.Button
about_button.pack(side=tk.RIGHT)

# Length selection
length_label = ttk.Label(root, text="Password Length:")  # Using ttk.Label
length_label.pack()

length_entry = ttk.Entry(root)  # Using ttk.Entry
length_entry.pack()

# Character complexity options
uppercase_var = tk.IntVar()
uppercase_check = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)  # Using ttk.Checkbutton
uppercase_check.pack()

lowercase_var = tk.IntVar()
lowercase_check = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)  # Using ttk.Checkbutton
lowercase_check.pack()

digits_var = tk.IntVar()
digits_check = ttk.Checkbutton(root, text="Digits", variable=digits_var)  # Using ttk.Checkbutton
digits_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = ttk.Checkbutton(root, text="Special Characters", variable=special_chars_var)  # Using ttk.Checkbutton
special_chars_check.pack()

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)  # Using ttk.Button
generate_button.pack(pady=5)

# Display generated password
password_display = tk.Text(root, height=5, width=30)
password_display.config(state=tk.DISABLED)
password_display.pack()

# UI Buttons for Save to File, Copy to Clipboard, Clear Password
save_button = ttk.Button(root, text="Save to File", command=save_to_file)  # Using ttk.Button
save_button.pack(pady=5)

copy_clipboard_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)  # Using ttk.Button
copy_clipboard_button.pack(pady=5)

clear_button = ttk.Button(root, text="Clear Password", command=clear_password)  # Using ttk.Button
clear_button.pack(pady=5)

# Interface label at bottom right
interface_label = ttk.Label(root, text="codestak.io", foreground="gray")  # Using ttk.Label
interface_label.pack(side=tk.RIGHT, anchor=tk.SE)

root.mainloop()
