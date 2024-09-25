class file_name_entery:
    def __init__(self, computer_width_information, computer_height_information):
        self.computer_info_width=computer_width_information
        self.computer_info_height=computer_height_information
    # 用户输入下载文件的名字
    def filename_windows(self):
        self.windows_filename=tkinter.Toplevel()
        self.windows_filename_icon=self.windows_filename.iconbitmap(r"download_photo.ico")
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
        self.button_ensure_filename_and_wirtein_bind=self.ensure_filename.bind("<Button-1>", lambda event_2: self.write_in_file())
    def write_in_file(self):
        self.filename_entry_get = None
        self.filename_entry_get = self.file_name_entery.get()
        self.windows_filename_quite = self.windows_filename.destroy()
        if self.filename_entry_get != None:
            self.file_name = "{}{}".format(self.filename_entry_get, self.file_type)
            self.writing_type = "wb"
            with open(self.file_name, self.writing_type) as self.creat_file:
                self.creat_file.write(self.read_respond)
