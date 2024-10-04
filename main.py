import tkinter as tk
from tkinter import messagebox
import requests

# Function to shorten URL using TinyURL API
def shorten_url():
    original_url = url_entry.get()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
    tinyurl_api = f"http://tinyurl.com/api-create.php?url={original_url}"
    
    try:
        response = requests.get(tinyurl_api)
        if response.status_code == 200:
            shortened_url = response.text
            result_label.config(text=shortened_url)
        else:
            messagebox.showerror("Error", "Failed to shorten URL. Try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to copy shortened URL to clipboard
def copy_to_clipboard():
    shortened_url = result_label.cget("text")
    if shortened_url:
        window.clipboard_clear()
        window.clipboard_append(shortened_url)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard")
    else:
        messagebox.showerror("Error", "No URL to copy")

# Main window setup
window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x300")
window.config(bg="black")

# URL Entry label and textbox
label = tk.Label(window, text="Enter URL to Shorten:", bg="black", fg="white", font=("Arial", 12))
label.pack(pady=10)

url_entry = tk.Entry(window, width=40, font=("Arial", 12))
url_entry.pack(pady=10)

# Generate Button
generate_button = tk.Button(window, text="Generate", bg="white", fg="black", font=("Arial", 12), command=shorten_url)
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", bg="grey", fg="white", font=("Arial", 12), width=40)
result_label.pack(pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(window, text="Copy to Clipboard", bg="white", fg="black", font=("Arial", 12), command=copy_to_clipboard)
copy_button.pack(pady=10)

window.mainloop()