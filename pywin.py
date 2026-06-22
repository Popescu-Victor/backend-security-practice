import win32gui
import win32con

def find_window(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        raise Exception(f"Window with title '{title}' not found.")
    return hwnd


def enum_windows_callback(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        # Get the title text of the window
        window_text = win32gui.GetWindowText(hwnd)
        
        # Filter out empty titles (many background system processes have no title)
        if window_text:
            print(window_text)

# EnumWindows takes a callback function and a custom extra argument (we pass None)
print("Listing all open, visible windows:\n" + "="*40)
win32gui.EnumWindows(enum_windows_callback, None)