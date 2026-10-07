import tkinter as tk
from time import strftime


# ----------------------------
# Update Time Function
# ----------------------------
def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)

    # Update every 1000 milliseconds (1 second)
    clock_label.after(1000, update_time)


# ----------------------------
# Create Main Window
# ----------------------------
window = tk.Tk()

window.title("Digital Clock")
window.geometry("500x250")
window.resizable(False, False)
window.configure(bg="black")


# ----------------------------
# Heading
# ----------------------------
title = tk.Label(
    window,
    text="DIGITAL CLOCK",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="cyan"
)

title.pack(pady=20)


# ----------------------------
# Clock Label
# ----------------------------
clock_label = tk.Label(
    window,
    font=("Arial", 48, "bold"),
    bg="black",
    fg="lime"
)

clock_label.pack(pady=20)


# ----------------------------
# Start Clock
# ----------------------------
update_time()

window.mainloop()