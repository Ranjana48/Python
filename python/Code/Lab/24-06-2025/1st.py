import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x150")

# Function to run when button is clicked
def say_hello():
    label.config(text="Hello, buddy!")

# Label
label = tk.Label(root, text="Click the button")
label.pack(pady=10)

# Button
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack(pady=10)

# Run the app
root.mainloop()
