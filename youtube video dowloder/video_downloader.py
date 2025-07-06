import tkinter as tk
from tkinter import filedialog
import yt_dlp

def  open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please entern the YouTube URL: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print('Please select a folder!')
    else:
        savepath = "/Users/rahul/Desktop/Projects/python/Automate"
        yt_dlp.YoutubeDL().download([video_url])