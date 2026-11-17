"""Step 2: widgets and pack layout."""
import tkinter as tk

root = tk.Tk()
root.title("Labels and buttons")
root.geometry("400x220")

label = tk.Label(root, text="Welcome to Camera Rental")
label.pack(pady=16)

button = tk.Button(root, text="Rent Camera")
button.pack(pady=8)

root.mainloop()
