import clipboard
import tkinter.messagebox as tm
import tkinter as tk
from tkinter import ttk
from tkinter import *

def login():
    username = Username_entry.get()
    password = Password_entry.get()

    if user



root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Administrator Panel")

User_frame = ttk.Frame(root, padding=(50, 1, 50, 1))
User_frame.pack(fill="x")
Username_label = ttk.Label(User_frame, text="Username:")
Username_label.pack(side="left", padx=7)
Username_entry = ttk.Entry(User_frame)
Username_entry.pack(side="right")

Pass_frame = ttk.Frame(root, padding=(50, 1, 50, 1))
Pass_frame.pack(fill="x")
Password_label = ttk.Label(Pass_frame, text="Password:")
Password_label.pack(side="left", padx=8)
Password_entry = ttk.Entry(Pass_frame, show="*")
Password_entry.pack(side="right", padx=1)

login_btn = ttk.Button(root, text="Login")
login_btn.pack(side="top", pady=2)

root.mainloop()