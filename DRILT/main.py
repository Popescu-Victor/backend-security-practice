from tkinter import filedialog
import zipfile

# I prefer to have this part in every practice program, so I can run it directly from the terminal while handling files.


class FilePath(): # Storing filepath as object for further reference
    def __init__(self, path):
        self.path = path

    def get_path(self):
        return self.path



def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_obj = FilePath(file_path)
        return file_path_obj.get_path()
    else:
        return "No file selected."

if __name__ == "__main__":
    file_path_obj = FilePath(open_file())
    with zipfile.ZipFile(file_path_obj.get_path()) as zf:
        print(zf.namelist())