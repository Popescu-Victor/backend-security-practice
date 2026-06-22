import win32gui
import win32con

def find_window(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        raise Exception(f"Window with title '{title}' not found.")
    return hwnd

win_title = input("Enter the title of the window to minimize: ")