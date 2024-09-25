import tkinter
class window:
    # 初始化程序
    def __init__(self):
        self.Windows=tkinter.Tk()
        self.title=self.Windows.title("Numbers Analyze tool")
        self.Windows_height=600
        self.Windows_width=1000
        self.unsizeale=self.Windows.resizable(False, False)
        self.computer_info_height=self.Windows.winfo_screenheight()
        self.computer_info_width=self.Windows.winfo_screenwidth()
        self.screen_x=int((self.computer_info_width-1000)/2)
        self.screen_y=int((self.computer_info_height-600)/2)
        self.size_position_str="{}x{}+{}+{}".format(self.Windows_width, self.Windows_height, self.screen_x, self.screen_y)
        self.New_Windows=self.Windows.geometry(self.size_position_str)
        self.windows_icon=self.Windows.iconbitmap(r"download_photo.ico")
