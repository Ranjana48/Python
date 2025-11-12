import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
try:
    cn = mysql.connector.connect(
        database="TODOApp",
        user="root",
        password="ranjana@2024",
        host="localhost",
        port="3306"
    )
    c = cn.cursor()
except mysql.connector.Error as err:
    print("Database connection failed:", err)

# GUI setup
mwin = tk.Tk()
mwin.title("To-Do List Application")
mwin.geometry("400x300+200+200")  # Corrected size and position

# You can now continue with GUI elements: entries, buttons, listboxes, etc.
mwin.mainloop()
