import tkinter
# 定义12306抢票的所有功能
class Function_12306_All:
    # 定义12306的窗口
    def define_12306_windows(self):
        self.windows_12306=tkinter.Toplevel()
    # 主循环
    def tkinter_mainloop(self):
        self.mainloop=tkinter.mainloop()
# 运行Function_12306_All
class Run_Function_12306_All(Function_12306_All):
    function_12306_windows=Function_12306_All.define_12306_windows
    mainloop=Function_12306_All.tkinter_mainloop
"""
# 运行窗口
if __name__=="__main__":
    Analyze_Beta=Analyze_all_function_Beta()
    define_12306_windows=Analyze_Beta.define_12306_windows()
"""
