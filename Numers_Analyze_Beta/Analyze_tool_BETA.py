import tkinter
from Number_Analyzing_First_Gen.Analyze_tool import Analyze_All_Function
# 定义Analyze_tool_Beta的继承类
class Analyze_all_function_Beta(Analyze_All_Function):
    # 定义12306的窗口
    def define_12306_windows(self):
        self.destory_main_windows=self.Windows.destroy()
        self.windows_12306=tkinter.Tk()
# 运行窗口
if __name__=="__main__":
    Analyze_Beta=Analyze_all_function_Beta()
    define_12306_windows=Analyze_Beta.define_12306_windows()
