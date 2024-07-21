import tkinter as tk
from tkinter import ttk, messagebox
import json
import base64

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("500x400")

        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.setup_widgets()
        self.load_passwords()

    def setup_widgets(self):
        # Entry fields
        ttk.Label(self.main_frame, text="Website:").grid(row=0, column=0, sticky="w")
        self.website_entry = ttk.Entry(self.main_frame, width=30)
        self.website_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.main_frame, text="Username:").grid(row=1, column=0, sticky="w")
        self.username_entry = ttk.Entry(self.main_frame, width=30)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.main_frame, text="Password:").grid(row=2, column=0, sticky="w")
        self.password_entry = ttk.Entry(self.main_frame, width=30, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add button
        self.add_button = ttk.Button(self.main_frame, text="Add Password", command=self.add_password)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Treeview for displaying passwords
        self.tree = ttk.Treeview(self.main_frame, columns=("Website", "Username", "Password"), show="headings")
        self.tree.heading("Website", text="Website")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.grid(row=4, column=0, columnspan=2, sticky="nsew")

        # Show Password button
        self.show_password_button = ttk.Button(self.main_frame, text="Show Password", command=self.show_password)
        self.show_password_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Configure grid weights
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(4, weight=1)

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website and username and password:
            encrypted_password = self.simple_encrypt(password)
            self.tree.insert("", "end", values=(website, username, self.mask_password(encrypted_password)))
            self.save_passwords()
            self.clear_entries()

    def clear_entries(self):
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def save_passwords(self):
        passwords = []
        for item in self.tree.get_children():
            values = self.tree.item(item)["values"]
            passwords.append(values)
        
        with open("passwords.json", "w") as f:
            json.dump(passwords, f)

    def load_passwords(self):
        try:
            with open("passwords.json", "r") as f:
                passwords = json.load(f)
            
            for password in passwords:
                self.tree.insert("", "end", values=(password[0], password[1], self.mask_password(password[2])))
        except FileNotFoundError:
            pass

    def show_password(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item[0])
            values = item['values']
            website, username, masked_password = values
            
            # Retrieve the actual password from the JSON file
            with open("passwords.json", "r") as f:
                passwords = json.load(f)
            
            for stored_password in passwords:
                if stored_password[0] == website and stored_password[1] == username:
                    decrypted_password = self.simple_decrypt(stored_password[2])
                    
                    # Show the password in a messagebox
                    tk.messagebox.showinfo("Password", f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}")
                    return

        tk.messagebox.showwarning("No Selection", "Please select a password to reveal.")

    def simple_encrypt(self, password):
        return base64.b64encode(password.encode()).decode()

    def simple_decrypt(self, encrypted):
        return base64.b64decode(encrypted.encode()).decode()

    def mask_password(self, password):
        return "*" * len(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()