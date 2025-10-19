import tkinter as tk
from tkinter import messagebox
import time
import threading

# Function to check alarm time
def check_alarm():
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time.get():
            messagebox.showinfo("Alarm", f"Time to wake up!\nMessage: {msg.get()}")
            break
        time.sleep(1)

# Function to start alarm
def start_alarm():
    threading.Thread(target=check_alarm, daemon=True).start()

# Tkinter window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x250")

# Heading
tk.Label(root, text="Alarm Clock", font=("Helvetica", 18, "bold")).pack(pady=10)

# Alarm time input
tk.Label(root, text="Set Time (HH:MM:SS):", font=("Arial", 12)).pack()
alarm_time = tk.Entry(root, width=15, font=("Arial", 12))
alarm_time.pack(pady=5)

# Message input
tk.Label(root, text="Message:", font=("Arial", 12)).pack()
msg = tk.Entry(root, width=30, font=("Arial", 12))
msg.pack(pady=5)

# Button to set alarm
tk.Button(root, text="Set Alarm", font=("Arial", 12, "bold"), command=start_alarm).pack(pady=15)

root.mainloop()
