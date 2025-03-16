import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters for security.")
            return
        
        use_symbols = symbols_var.get()
        use_numbers = numbers_var.get()
        use_alphabets = alphabets_var.get()
        
        characters = ""
        if use_alphabets:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        
        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

symbols_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
alphabets_var = tk.BooleanVar()

symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, font=("Arial", 10))
symbols_check.pack()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, font=("Arial", 10))
numbers_check.pack()
alphabets_check = tk.Checkbutton(root, text="Include Alphabets", variable=alphabets_var, font=("Arial", 10))
alphabets_check.pack()

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12), width=30)
password_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard)
copy_btn.pack(pady=10)

root.mainloop()