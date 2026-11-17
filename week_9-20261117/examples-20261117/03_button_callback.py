"""Step 3: an event callback triggered by a button click."""
import tkinter as tk

root = tk.Tk()
root.title("Event handling")
root.geometry("400x220")

message = tk.Label(root, text="Click the button")
message.pack(pady=16)

def on_click():
    message.config(text="Button clicked! The callback ran.")

button = tk.Button(root, text="Rent Camera", command=on_click)
button.pack(pady=8)
root.mainloop()
