import tkinter
class choose_start_station:
    def __init__(self, computer_info_width, computer_info_height):
        self.windows_choose_start_station = tkinter.Toplevel()
        self.windows_choose_start_station_icon = self.windows_choose_start_station.iconbitmap(
            r"./12306_prog_addition/download_photo.ico")
        self.start_station_entery = tkinter.Entry(
            self.windows_choose_start_station, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.start_station_entery.place(x=self.x_entry, y=self.y_entry)
        self.title_1 = self.windows_choose_start_station.title("请选择出发车站")
        self.windows_choose_start_station_height = 600
        self.windows_choose_start_station_width = 500
        self.unresizeable = self.windows_choose_start_station.resizable(False, False)
        self.screen_choose_start_station_x = int((computer_info_width - self.windows_choose_start_station_width) / 2)
        self.screen_choose_start_station_y = int((computer_info_height - self.windows_choose_start_station_height) / 2)
        self.windows_choose_start_station_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_start_station_width, self.windows_choose_start_station_height,
            self.screen_choose_start_station_x, self.screen_choose_start_station_y)
        self.New_choose_start_station_Windows = self.windows_choose_start_station.geometry(
            self.windows_choose_start_station_position_str)
class Get_ticket_interface:
    def __init__(self):
        self.Windows = tkinter.Tk()
        self.title = self.Windows.title("Numbers Analyze tool")
        self.Windows_height = 600
        self.Windows_width = 1000
        self.progress_windows = None
        self.computer_info_height = self.Windows.winfo_screenheight()
        self.computer_info_width = self.Windows.winfo_screenwidth()
        self.screen_x = int((self.computer_info_width - 1000) / 2)
        self.screen_y = int((self.computer_info_height - 600) / 2)
        self.size_position_str = "{}x{}+{}+{}".format(
            self.Windows_width, self.Windows_height, self.screen_x, self.screen_y)
        self.New_Windows = self.Windows.geometry(self.size_position_str)
        self.windows_icon = self.Windows.iconbitmap(r"./12306_prog_addition/download_photo.ico")
        self.entery_start=None
        self.label_start=tkinter.Label(self.Windows, text="出发城市/车站:", font=("微软雅黑", 12))
        self.label_start_pack=self.label_start.pack(side="top", pady=20)
        self.label_end = tkinter.Label(self.Windows, text="到达城市/车站:", font=("微软雅黑", 12))
        self.label_end_place = self.label_end.place(x=self.Windows_width/2-58, y=75)
        self.label_date = tkinter.Label(self.Windows, text="出发日期:", font=("微软雅黑", 12))
        self.label_date_place = self.label_date.place(x=self.Windows_width / 2 - 58, y=125)
    def Entry_Function(self):
        self.entery_start=tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体",15,"underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry_start=50
        self.y_entry_start=50
        self.entery_start.place(x=self.x_entry_start, y=self.y_entry_start)
        self.entery_end = tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry_end = 50
        self.y_entry_end = 100
        self.entery_end.place(x=self.x_entry_end, y=self.y_entry_end)
        self.entery_date = tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry_date = 50
        self.y_entry_date = 150
        self.entery_date.place(x=self.x_entry_date, y=self.y_entry_date)
    def Windows_Button(self):
        self.button_search_start_station=tkinter.Button(
            self.Windows, text="查询车站", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_start_station_width=self.button_search_start_station.winfo_width()
        self.button_search_start_station_height=self.button_search_start_station.winfo_height()
        self.x=int(self.Windows_width-self.button_search_start_station_width)
        self.y=25
        self.butoon_search_start_station_place=self.button_search_start_station.place(x=self.x, y=self.y, anchor="ne")
        self.button_search_end_station=tkinter.Button(
            self.Windows, text="查询车站", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_end_station_width = self.button_search_end_station.winfo_width()
        self.button_search_end_station_height = self.button_search_end_station.winfo_height()
        self.x_1=int(self.Windows_width - self.button_search_end_station_width)
        self.y_1=75
        self.button_search_end_station_place=self.button_search_end_station.place(x=self.x_1, y=self.y_1, anchor="ne")
        self.button_search_date = tkinter.Button(
            self.Windows, text="选择日期", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_date_width = self.button_search_date.winfo_width()
        self.button_search_date_height = self.button_search_date.winfo_height()
        self.x_2 = int(self.Windows_width - self.button_search_date_width)
        self.y_2 = 125
        self.button_search_date_place = self.button_search_date.place(x=self.x_2, y=self.y_2, anchor="ne")











