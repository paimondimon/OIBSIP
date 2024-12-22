import tkinter as tk
from tkinter import messagebox
import hashlib
import random
import string

# Hashing function (with reverse and hex addition)
def process_password(password):
    # Step 1: Hash the password using SHA-256
    hash_obj = hashlib.sha256(password.encode())
    hash_hex = hash_obj.hexdigest()

    # Step 2: Reverse the hash
    reversed_hash = hash_hex[::-1]

    # Step 3: Append a hex string (e.g., "abc123") to the reversed hash
    hex_code = "abc123"
    final_hash = reversed_hash + hex_code

    # Display the steps in the terminal for debugging
    print(f"Original Password: {password}")
    print(f"SHA-256 Hash of Password: {hash_hex}")
    print(f"Reversed Hash: {reversed_hash}")
    print(f"Final Hashed Password with Hex Code: {final_hash}")

    return final_hash

# Function to generate a random password
def generate_password():
    # Generate a random password with at least 25 characters
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(25))

    # Process the password and display the steps
    final_hash = process_password(random_password)

    # Display the generated password and hash in the UI
    password_display.config(text=f"Generated Password: {random_password}")
    hash_display.config(text=f"Final Hashed Password: {final_hash}")

    return random_password, final_hash

# Function to handle user input
def process_user_input():
    user_password = input_field.get()

    if len(user_password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters!")
        return

    # Process the user-provided password
    final_hash = process_password(user_password)

    # Display the processed hash in the UI
    password_display.config(text=f"Entered Password: {user_password}")
    hash_display.config(text=f"Final Hashed Password: {final_hash}")

    # Provide feedback to the user about the password strength
    if len(user_password) >= 25:
        messagebox.showinfo("Success", "Your password is strong!")
    else:
        messagebox.showinfo("Info", "Consider using a password with at least 25 characters for better security.")

# Main application window
root = tk.Tk()
root.title("Password Generator with Input")

# Label for the input section
tk.Label(root, text="Enter Your Password", font=("Arial", 16)).pack(pady=10)

# Text entry for user to input a custom password
input_field = tk.Entry(root, show='*', font=("Arial", 12), width=30)
input_field.pack(pady=10)

# Button to process the user-provided password
tk.Button(root, text="Process My Password", command=process_user_input).pack(pady=10)

# Button to generate a random strong password
tk.Button(root, text="Generate Strong Password", command=generate_password).pack(pady=10)

# Label to display the generated/processed password and hash
password_display = tk.Label(root, text="", font=("Arial", 12), wraplength=500)
password_display.pack(pady=10)

hash_display = tk.Label(root, text="", font=("Arial", 12), wraplength=500)
hash_display.pack(pady=10)

# Start the main UI loop
root.mainloop()
