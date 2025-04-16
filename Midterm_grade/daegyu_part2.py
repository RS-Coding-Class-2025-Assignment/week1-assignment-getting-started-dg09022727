import tkinter as tk
from tkinter import ttk
import time
import threading 

root = tk.Tk()
root.title("Threaded Progress Bar")
root.geometry("400x200") 

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

percent_label = tk.Label(root, text="0%")
percent_label.pack()

start_button = tk.Button(root, text="Start")
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop")
stop_button.pack(pady=10)

root.mainloop()