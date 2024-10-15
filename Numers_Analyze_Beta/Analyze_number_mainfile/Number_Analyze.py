import json
import tkinter
import threading
import webbrowser
import urllib.request
from tkinter import ttk
import tkinter.messagebox
from concurrent.futures import ThreadPoolExecutor
class Analyze_All_Function():
    def __init__(self):
        self.total_process=0
        self.Windows=tkinter.Tk()
        self.title=self.Windows.title("Numbers Analyze tool")
        self.Windows_height=600
        self.Windows_width=1000
        self.progress_windows=None
        self.unsizeale=self.Windows.resizable(False, False)
        self.computer_info_height=self.Windows.winfo_screenheight()
        self.computer_info_width=self.Windows.winfo_screenwidth()
        self.screen_x=int((self.computer_info_width-1000)/2)
        self.screen_y=int((self.computer_info_height-600)/2)
        self.size_position_str="{}x{}+{}+{}".format(self.Windows_width, self.Windows_height, self.screen_x, self.screen_y)
        self.New_Windows=self.Windows.geometry(self.size_position_str)
        self.windows_icon=self.Windows.iconbitmap(r"./prog_addition/download_photo.ico")
    def Entry_Function(self):
        self.entery=tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体",15,"underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry=50
        self.y_entry=80/3
        self.entery.place(x=self.x_entry, y=self.y_entry)
    def Windows_Button(self):
        self.button_download=tkinter.Button(
            self.Windows, text="下载", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_download_width=self.button_download.winfo_width()
        self.button_download_height=self.button_download.winfo_height()
        self.x=int(self.Windows_width-self.button_download_width)
        self.y=10
        self.butoon_download_place_S_D=self.button_download.place(x=self.x, y=self.y, anchor="ne")
        self.button_search=tkinter.Button(
            self.Windows, text="搜索", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_width = self.button_search.winfo_width()
        self.button_search_height = self.button_search.winfo_height()
        self.x_1=int(self.Windows_width - self.button_search_width)
        self.y_1=40
        self.button_search_place_S_D=self.button_search.place(x=self.x_1, y=self.y_1, anchor="ne")
    def download_check_bind(self):
        self.downloader_run_result = self.button_download.bind("<Button-1>", lambda event: self.thread_spider())
    def search_check_bind(self):
        self.search_run_result=self.button_search.bind("<Button-1>", lambda event_1: self.thread_search_open_chrom())
    def progress_bar(self):
        self.file_size=self.respond.getheader("Content-Length")
        self.progress_windows=ttk.Progressbar(self.Windows, orient="horizontal", length=300, mode="determinate")
        self.progress_windows.pack(pady=20)
    def url_get(self):
        self.entery_get = self.entery.get()
        return self.entery_get
    def filename_get_and_writein(self):
        self.condition=0
        self.filename_entry_get=None
        self.filename_entry_get=self.file_name_entery.get()
        self.windows_filename_quite=self.windows_filename.destroy()
        if self.filename_entry_get != None:
            self.file_name = "{}{}".format(self.filename_entry_get, self.file_type)
            self.writing_type = "wb"
            with open(self.file_name, self.writing_type) as self.creat_file:
                self.creat_file.write(self.read_respond)
            self.condition+=1
        while True:
            if self.condition==1:
                self.okay_box=tkinter.messagebox.showinfo(
                    title="download", message="the file is downloaded successfully!")
                break
    def Downloader_get(self):
        self.read_respond=None
        self.header={
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Cookie":
                True}
        self.Url_Get=self.url_get()
        self.respond=None
        if self.Url_Get==None or self.Url_Get=='':
            self.error_messagebox_download=tkinter.messagebox.showerror(
                title="enter error", message="You MUST enter a url which you want to download!")
        else:
            self.add_url_headers=urllib.request.Request(url=self.Url_Get, headers=self.header)
            self.total_process+=100
            self.respond=urllib.request.urlopen(self.add_url_headers)
            self.read_respond=self.respond.read()
            self.total_process+=100
            self.url_type = self.respond.getheader("Content-Type")
            self.text_list_url_type = []
            for a in self.url_type:
                self.text_list_url_type.append(a)
            self.text_list_url_type.append(";")
            self.find_element = "/"
            self.element_position = self.text_list_url_type.index(self.find_element)
            self.semicolon = ";"
            self.judge_type_url = ""
            self.count_limit=None
            self.count_limit=self.text_list_url_type.index(self.semicolon)
            self.total_process+=100
            for b in range(self.element_position + 1, self.count_limit):
                self.judge_type_url += self.text_list_url_type[b]
            with open(r"./prog_addition/url_type.json", "r", encoding="utf-8") as self.url_type_file:
                self.file_data = json.load(self.url_type_file)
            self.content = self.file_data[0]
            self.file_type_in_dic = []
            self.content_type_in_dic = []
            for d in self.content:
                self.file_type_in_dic.append(d)
            for e in self.file_type_in_dic:
                self.get_content_type = self.content[e]
                self.content_type_in_dic.append(self.get_content_type)
            self.file_type_position = self.content_type_in_dic.index(self.judge_type_url)
            self.file_type=self.file_type_in_dic[self.file_type_position]
            self.filename=self.filename_windows()
    def filename_windows(self):
        self.windows_filename=tkinter.Toplevel()
        self.windows_filename_icon=self.windows_filename.iconbitmap(r"./prog_addition/download_photo.ico")
        self.file_name_entery = tkinter.Entry(
            self.windows_filename, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.file_name_entery.place(x=self.x_entry, y=self.y_entry)
        self.title_1=self.windows_filename.title("Please write a file title.")
        self.windows_filename_height=200
        self.windows_filename_width=500
        self.unresizeable=self.windows_filename.resizable(False, False)
        self.screen_filename_x = int((self.computer_info_width - self.windows_filename_width) / 2)
        self.screen_filename_y = int((self.computer_info_height - self.windows_filename_height) / 2)
        self.file_name_size_position_str = "{}x{}+{}+{}".format(
            self.windows_filename_width, self.windows_filename_height, self.screen_filename_x, self.screen_filename_y)
        self.New_downloadtype_Windows = self.windows_filename.geometry(self.file_name_size_position_str)
        self.ensure_filename = tkinter.Button(
            self.windows_filename, text="确定", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_ensure_width = self.ensure_filename.winfo_width()
        self.button_ensure_height=self.ensure_filename.winfo_height()
        self.windows_file_name_width=self.windows_filename.winfo_width()
        self.windows_file_name_height=self.windows_filename.winfo_height()
        self.x_1 = int((self.windows_file_name_width+self.button_ensure_width)/2)
        self.y_1 = 150
        self.button_ensure_pack = self.ensure_filename.place(x=self.x_1, y=self.y_1)
        self.button_ensure_filename_and_wirtein_bind=self.ensure_filename.bind(
            "<Button-1>", lambda event_2: self.thread_getfilename_and_wirtein())
    def search_open_chrome(self):
        self.url_open=self.url_get()
        if self.url_open==None or self.url_open==' ':
            self.error_messagebox_search = tkinter.messagebox.showerror(title="enter error", message="You MUST enter a url which you want to download!")
        else:
            self.webbrowser_open_url=webbrowser.open(self.url_open)
    def thread_spider(self):
        self.thread_run=threading.Thread(target=self.Downloader_get, name="thread1", daemon=True)
        self.thread_run.start()
        self.thread_process_bar=threading.Thread(target=self.progress_bar(), name="thread4", daemon=True)
        self.thread_process_bar.start()
    def thread_search_open_chrom(self):
        self.thread_open_url=threading.Thread(target=self.search_open_chrome, name="thread2", daemon=True)
        self.thread_open_url.start()
    def thread_getfilename_and_wirtein(self):
        self.thread_get_filename_and_wirtein=threading.Thread(target=self.filename_get_and_writein, name="thread3", daemon=True)
        self.thread_get_filename_and_wirtein.start()
    def thread_pool_concurrent(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=None)
        self.threed_1 = self.thread_pool.submit(self.download_check_bind)
        self.thread_2 = self.thread_pool.submit(self.search_check_bind)
    def main_loop(self):
        self.mainloop = tkinter.mainloop()
if __name__=="__main__":
    run=Analyze_All_Function()
    Entry_Function=run.Entry_Function()
    button_windows=run.Windows_Button()
    thread_pool_run=run.thread_pool_concurrent()
    main_loop=run.main_loop()
