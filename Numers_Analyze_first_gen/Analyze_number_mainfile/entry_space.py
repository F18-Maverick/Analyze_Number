import tkinter
class enter_space:
    def __init__(self, Window):
        self.Windows=Window
        self.entery=tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体",15,"underline"),
            width=88, relief="solid", insertwidth=1)
        self.x_entry=50
        self.y_entry=80/3
        self.entery.place(x=self.x_entry, y=self.y_entry)
