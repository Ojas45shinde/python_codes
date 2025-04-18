import tkinter as tk
import string
import secrets


def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(12))  
    password_entry.delete(0, tk.END)  
    password_entry.insert(tk.END, password)  


root = tk.Tk()
root.title("Password Generator")
label = tk.Label(root, text="Click below to generate a password:")
label.pack(pady=10)


password_entry = tk.Entry(root, width=30, font=("Helvetica", 16))
password_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


root.mainloop()
