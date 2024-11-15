import tkinter
class choose_start_time:
    def __init__(self, computer_info_width, computer_info_height):
        self.windows_choose_start_time = tkinter.Toplevel()
        self.windows_choose_start_time_icon = self.windows_choose_start_time.iconbitmap(
            r"./ticket_12306_prog_addition/download_photo.ico")
        self.start_time_entery = tkinter.Entry(
            self.windows_choose_start_time, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.start_time_entery.place(x=self.x_entry, y=self.y_entry)
        self.title_1 = self.windows_choose_start_time.title("请选择到达车站")
        self.windows_choose_start_time_height = 300
        self.windows_choose_start_time_width = 500
        self.unresizeable = self.windows_choose_start_time.resizable(False, False)
        self.screen_choose_start_time_x = int((computer_info_width - self.windows_choose_start_time_width) / 2)
        self.screen_choose_start_time_y = int((computer_info_height - self.windows_choose_start_time_height) / 2)
        self.windows_choose_start_time_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_start_time_width, self.windows_choose_start_time_height,
            self.screen_choose_start_time_x, self.screen_choose_start_time_y)
        self.New_choose_start_time_Windows = self.windows_choose_start_time.geometry(
            self.windows_choose_start_time_position_str)








