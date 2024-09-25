import tkinter
class all_button:
    def __init__(self, Window, Window_width, Window_height):
        self.Windows=Window
        self.Windows_width=Window_width
        self.Windows_height=Window_height
    # 窗口GUI按钮
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
