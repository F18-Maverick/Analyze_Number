import urllib.request
import tkinter as tk
from tkinter import ttk, messagebox
class Downloader:
    def __init__(self):
        self.progress_window = None
        self.progress_bar = None
    def show_progress_bar(self, parent_window):
        # self.progress_window = tk.Toplevel(parent_window)
        # self.progress_window.title("进度条")
        # self.progress_window.geometry("400x100")
        self.progress_bar = ttk.Progressbar(self.progress_window, orient="horizontal", length=300, mode="indeterminate")
        self.progress_bar.pack(pady=20)
        self.progress_bar.start()
    def download(self, url):
        response = urllib.request.urlopen(url)
        return response.read()
    def save_file(self, data):
        filename = "downloaded_file"
        with open(filename, "wb") as file:
            file.write(data)
        messagebox.showinfo("成功", f"文件已保存为 {filename}")










