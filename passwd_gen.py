import string
import random
from tkinter import filedialog, messagebox
from fpdf import FPDF
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk

password_generated = False
current_theme = "darkly"

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

def switch_theme():
    global current_theme
    if current_theme == "darkly":
        current_theme = "flatly"
    else:
        current_theme = "darkly"
    style.theme_use(current_theme)

def show_about():
    messagebox.showinfo("About", "Password Generator App\nAuthor: Raymond C. Turner.\nVersion 2.0-beta")

root = tk.Tk()
root.title("PassGen")

style = Style(theme=current_theme)

root.minsize(width=400, height=500)
root.maxsize(width=700, height=800)

title_frame = ttk.Frame(root, padding=(10, 5))
title_frame.pack(fill=tk.X)

title_label = ttk.Label(title_frame, text="PassGen", font=("Helvetica", 12), foreground="white")
title_label.pack(side=tk.LEFT, padx=10)

theme_switch_button = ttk.Button(title_frame, text="Switch Theme", command=switch_theme)
theme_switch_button.pack(side=tk.RIGHT, padx=10)

about_button = ttk.Button(title_frame, text="About", command=show_about)
about_button.pack(side=tk.RIGHT, padx=10)

length_label = ttk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = ttk.Entry(root)
length_entry.pack(pady=5)

uppercase_var = tk.IntVar()
uppercase_check = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_check.pack(pady=5)

lowercase_var = tk.IntVar()
lowercase_check = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_check.pack(pady=5)

digits_var = tk.IntVar()
digits_check = ttk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.pack(pady=5)

special_chars_var = tk.IntVar()
special_chars_check = ttk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_check.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_display = tk.Text(root, height=5, width=30)
password_display.config(state=tk.DISABLED)
password_display.pack(pady=5)

save_button = ttk.Button(root, text="Save to File", command=save_to_file)
save_button.pack(pady=10)

copy_clipboard_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_clipboard_button.pack(pady=10)

clear_button = ttk.Button(root, text="Clear Password", command=clear_password)
clear_button.pack(pady=10)

interface_label = ttk.Label(root, text="codestack.io", foreground="gray")
interface_label.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)


root.mainloop()