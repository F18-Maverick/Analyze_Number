import tkinter
from all_threads import thread_all
class Get_ticket_interface:
    def __init__(self):
        self.entery_start=None
        self.entery_end=None
        self.entery_date=None
        self.Windows = tkinter.Tk()
        self.title = self.Windows.title("Numbers Analyze tool")
        self.Windows_height = 450
        self.Windows_width = 1000
        self.progress_windows = None
        self.computer_info_height = self.Windows.winfo_screenheight()
        self.computer_info_width = self.Windows.winfo_screenwidth()
        self.screen_x = int((self.computer_info_width - 1000) / 2)
        self.screen_y = int((self.computer_info_height - 600) / 2)
        self.size_position_str = "{}x{}+{}+{}".format(
            self.Windows_width, self.Windows_height, self.screen_x, self.screen_y)
        self.New_Windows = self.Windows.geometry(self.size_position_str)
        self.windows_icon = self.Windows.iconbitmap(r"./ticket_12306_prog_addition/download_photo.ico")
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
        self.use_choose_start_station_UI=self.button_search_start_station.bind(
            "<Button-1>", lambda event: thread_all().choose_start_station_UI_thread(
                self.computer_info_width, self.computer_info_height))
        self.button_search_end_station=tkinter.Button(
            self.Windows, text="查询车站", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_end_station_width = self.button_search_end_station.winfo_width()
        self.button_search_end_station_height = self.button_search_end_station.winfo_height()
        self.x_1=int(self.Windows_width - self.button_search_end_station_width)
        self.y_1=75
        self.button_search_end_station_place=self.button_search_end_station.place(x=self.x_1, y=self.y_1, anchor="ne")
        self.use_choose_end_station_UI=self.button_search_end_station.bind(
            "<Button-1>", lambda event_1: thread_all().choose_end_station_UI_thread(
                self.computer_info_width, self.computer_info_height))
        self.button_search_date = tkinter.Button(
            self.Windows, text="选择日期", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_search_date_width = self.button_search_date.winfo_width()
        self.button_search_date_height = self.button_search_date.winfo_height()
        self.x_2 = int(self.Windows_width - self.button_search_date_width)
        self.y_2 = 125
        self.button_search_date_place = self.button_search_date.place(x=self.x_2, y=self.y_2, anchor="ne")
        self.use_choose_start_time_UI = self.button_search_date.bind(
            "<Button-1>", lambda event_1: thread_all().choose_start_time_UI_thread(
                self.computer_info_width, self.computer_info_height))
        self.button_search_sure=tkinter.Button(
            self.Windows, text="确认", width=25, height=5, font=("Arial", 10, "underline"))
        self.button_search_sure_width=self.button_search_sure.winfo_width()
        self.button_search_sure_height=self.button_search_sure.winfo_height()
        self.x_3=int(self.Windows_width-self.button_search_sure_width)
        self.y_3=300
        self.button_search_sure_place=self.button_search_sure.place(x=self.x_3/2, y=self.y_3, anchor="center")










