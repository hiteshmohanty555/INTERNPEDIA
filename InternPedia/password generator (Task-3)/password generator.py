import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_password():
    length = random.randint(10, 20)  # Random password length between 10 and 20 characters
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generate_password(length))

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")

def generate_password_handler():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6 characters.")
        else:
            password = generate_password(length)
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

# GUI Setup
window = tk.Tk()
window.title("Password Generator")

# Label and Entry for Password Length
length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to Generate Password
generate_button = tk.Button(window, text="Generate Password", command=generate_password_handler)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Entry for Displaying Generated Password
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to Generate Random Password
random_button = tk.Button(window, text="Generate Random Password", command=generate_random_password)
random_button.grid(row=3, column=0, columnspan=2, pady=10)

# Button to Copy Password to Clipboard
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
