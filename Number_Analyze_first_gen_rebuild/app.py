import tkinter
from tkinter import ttk
from downloader import Downloader
from search import Search
class AnalyzeAllFunction:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Numbers Analyze Tool")
        self.setup_window()
        self.downloader = Downloader(self)
        self.search = Search(self)
    def setup_window(self):
        self.window.geometry("1000x600")
        self.window.resizable(False, False)
        self.create_widgets()
    def create_widgets(self):
        self.entry = tkinter.Entry(self.window)
        self.entry.place(x=50, y=80)
        self.button_download = tkinter.Button(self.window, text="下载", command=self.downloader.start_download)
        self.button_download.place(x=950, y=10, anchor="ne")
        self.button_search = tkinter.Button(self.window, text="搜索", command=self.search.start_search)
        self.button_search.place(x=950, y=40, anchor="ne")
    def run(self):
        self.window.mainloop()