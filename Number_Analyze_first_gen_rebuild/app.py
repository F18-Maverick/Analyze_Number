import tkinter as tk
from tkinter import ttk, messagebox
import threading
import webbrowser
from downloader import Downloader
class AnalyzeAllFunction:
    def __init__(self):
        self.downloader = Downloader()
        self.init_window()
        self.create_widgets()
    def init_window(self):
        self.window = tk.Tk()
        self.window.title("Numbers Analyze Tool")
        self.window.geometry("1000x600+{}+{}".format(
            (self.window.winfo_screenwidth() - 1000) // 2,
            (self.window.winfo_screenheight() - 600) // 2))
        self.window.resizable(False, False)
        self.window.iconbitmap(r"./prog_addition/download_photo.ico")
    def create_widgets(self):
        self.entry = tk.Entry(self.window, background="#FFFFFF", foreground="#4B0082",
                              font=("宋体", 15, "underline"), width=88, relief="solid")
        self.entry.place(x=50, y=80)
        self.button_download = tk.Button(self.window, text="下载", command=self.start_download)
        self.button_download.place(x=950, y=10, anchor="ne")
        self.button_search = tk.Button(self.window, text="搜索", command=self.open_url)
        self.button_search.place(x=950, y=40, anchor="ne")
    def start_download(self):
        threading.Thread(target=self.download).start()
    def download(self):
        url = self.entry.get()
        if not url:
            messagebox.showerror("错误", "请输入有效的 URL")
            return
        self.downloader.show_progress_bar(self.window)
        try:
            data = self.downloader.download(url)
            self.downloader.save_file(data)
        except Exception as e:
            messagebox.showerror("下载错误", str(e))
        finally:
            self.downloader.progress_window.destroy()
    def open_url(self):
        url = self.entry.get()
        if not url:
            messagebox.showerror("错误", "请输入有效的 URL")
            return
        webbrowser.open(url)
    def run(self):
        self.window.mainloop()
