# Create a text editor with features like opening, editing, and saving text files.

import tkinter as tk  # Import tkinter for GUI
from tkinter import filedialog  # Import filedialog to handle file operations

# Function to open an existing text file
def open_file():
    """Opens an existing text file."""
    # Ask user to select a file to open
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            # Open the file in read mode
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)  # Clear the current content of the text area
                text_area.insert(tk.END, file.read())  # Insert the file content into the text area
            window.title(f"Text Editor - {file_path}")  # Update the window title with the file name
        except Exception as e:
            print(f"Error opening file: {e}")  # Print an error message if file opening fails

# Function to save the current content to a text file
def save_file():
    """Saves the current content to a text file."""
    # Ask user to select a file to save
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            # Open the file in write mode
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))  # Write the content of the text area to the file
            window.title(f"Text Editor - {file_path}")  # Update the window title with the file name
        except Exception as e:
            print(f"Error saving file: {e}")  # Print an error message if file saving fails

# Function to create a new text file
def new_file():
    """Creates a new text file."""
    text_area.delete(1.0, tk.END)  # Clear the text area
    window.title("Text Editor - New File")  # Update the window title

# Create the main window
window = tk.Tk()
window.title("Text Editor")  # Set window title
window.geometry("600x400")  # Set window size

# Create a text area widget
text_area = tk.Text(window, wrap='word')
text_area.pack(expand=1, fill='both')

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Add file menu options
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)  # New file option
file_menu.add_command(label="Open", command=open_file)  # Open file option
file_menu.add_command(label="Save", command=save_file)  # Save file option
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)  # Exit option

# Run the application
window.mainloop()  
