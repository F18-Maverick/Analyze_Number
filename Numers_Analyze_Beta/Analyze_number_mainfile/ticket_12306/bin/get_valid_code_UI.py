import os
import time
import tkinter
import threading
class get_valid_code:
    def __init__(self, computer_info_width, computer_info_height, file_dir, phone_number):
        self.file_dir_name = file_dir
        self.temp_dir = os.path.join(self.file_dir_name, 'temp')
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.windows_get_valid_code = tkinter.Toplevel()
        # self.windows_choose_start_time_icon = self.windows_choose_start_time.iconbitmap(
        #     r"./ticket_12306_prog_addition/download_photo.ico")
        self.title_1 = self.windows_get_valid_code.title("填写登录信息")
        self.windows_get_valid_code_height = 300
        self.windows_get_valid_code_width = 500
        self.unresizeable = self.windows_get_valid_code.resizable(False, False)
        self.screen_get_valid_code_x = int((computer_info_width - self.windows_get_valid_code_width) / 2)
        self.screen_get_valid_code_y = int((computer_info_height - self.windows_get_valid_code_height) / 2)
        self.windows_get_valid_code_position_str = "{}x{}+{}+{}".format(
            self.windows_get_valid_code_width, self.windows_get_valid_code_height,
            self.screen_get_valid_code_x, self.screen_get_valid_code_y)
        self.New_choose_get_valid_code_Windows = self.windows_get_valid_code.geometry(
            self.windows_get_valid_code_position_str)
        self.valid_code_text = tkinter.Label(self.windows_get_valid_code, text="验证码")
        self.valid_code_text.place(x=self.x_entry, y=self.y_entry-20)
        self.valid_code_entry = tkinter.Entry(
            self.windows_get_valid_code, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.valid_code_entry.place(x=self.x_entry, y=self.y_entry)
        self.button=self.button_get_sign_in_info()
        self.loading_valid_code="已经验证码发送给:{}".format(phone_number)
        self.loading_valid_code_text=tkinter.Label(self.windows_get_valid_code, text=self.loading_valid_code)
        self.loading_valid_code_text.place(x=self.x_entry, y=self.y_entry+40)
        self.time_countdown_thread=threading.Thread(target=self.time_count_down)
        self.time_countdown_thread.start()
    def time_count_down(self):
        self.time_count_total=60
        while self.time_count_total!=0:
            self.time_count_total-=1
            time.sleep(1)
            self.time_text=tkinter.Label(self.windows_get_valid_code, text="重新发送({}秒)".format(self.time_count_total))
            self.time_text.place(x=self.x_entry, y=self.y_entry+60)
    def get_data(self):
        self.contact_info=self.valid_code_entry.get()
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        with open(os.path.join(self.temp_dir, "data_socket_user_valid_code_info.log"), "w", encoding="utf-8") as datalog_write:
            datalog_write.write(str(self.contact_info))
        self.windows_get_valid_code.destroy()
    def button_get_sign_in_info(self):
        self.button_sign_in_sure = tkinter.Button(
            self.windows_get_valid_code, text="确认", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_get_start_time_sure_pack = self.button_sign_in_sure.pack(side=tkinter.BOTTOM)
        self.bind_func_sure = self.button_sign_in_sure.bind("<Button-1>", lambda event: self.get_data())


















