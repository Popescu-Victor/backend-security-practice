import firebase_admin
from firebase_admin import credentials, firestore
from functools import lru_cache
from tkinter import filedialog

def get_credentials():
    file_path = filedialog.askopenfilename(title="Select Firebase Service Account Key", filetypes=[("JSON files", "*.json")])
    if not file_path:
        raise Exception("No file selected for Firebase credentials.")
    return credentials.Certificate(file_path)


@lru_cache(maxsize=1)
def get_db():
    if not firebase_admin._apps:
        cred = get_credentials()
        firebase_admin.initialize_app(cred)
    return firestore.client()

get_db()