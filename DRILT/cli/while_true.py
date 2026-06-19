while True:
    try:
        command = input(">   ").lower().strip()
        if command.split(">")[0] == "file":
            if command.split(">")[1].strip() == "upload":
                from tkinter import filedialog
                from tkinter import Tk
                file_path = filedialog.askopenfilename()
                print(f"Selected file: {file_path}")
        else:
                print("Unknown file command. Use 'file upload'.")  
    except Exception as e:
        print(f"An error occurred: {e}")