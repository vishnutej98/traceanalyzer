import tkinter as tk
from tkinter import filedialog

def get_file_path():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()  # Open file dialog window for choosing a file
    return file_path

def main():
    file_path = get_file_path()
    print("Selected file path:", file_path)
    # Perform further actions using the selected file_path

if __name__ == "__main__":
    main()
