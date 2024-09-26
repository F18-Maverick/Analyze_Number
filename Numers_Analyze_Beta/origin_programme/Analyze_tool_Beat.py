import tkinter
from Analyze_tool import Analyze_All_Function
# 定义12306抢票的所有功能
class Analyze_tool_Beta_All_Functions(Analyze_All_Function):
    # 定义12306的窗口
    def Function_12306_windows(self):
        self.windows_12306=tkinter.Toplevel()
    # 为12306抢票功能创建按钮侦测
    def windows_12306_bind(self):
        self.windows_12306_run = self.button_12306_windows.bind("<Button-1>", lambda event_3: self.Function_12306_windows())
    # 主循环

# 运行窗口
if __name__=="__main__":
    Analyze_Beta=Analyze_tool_Beta_All_Functions()







