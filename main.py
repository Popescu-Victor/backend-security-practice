from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")

if __name__ == "__main__":
    open_file()