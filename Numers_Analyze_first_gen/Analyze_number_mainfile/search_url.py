import tkinter
import webbrowser
class search_url:
    def __init__(self, Enter_space):
        self.entery_text = Enter_space
    # 搜索打开浏览器
    def search_open_chrome(self):
        self.url_open=get_entery_text(self.entery_text)
        if self.url_open==None or self.url_open==' ':
            self.error_messagebox_search = tkinter.messagebox.showerror(title="enter error", message="You MUST enter a url which you want to download!")
        else:
            self.webbrowser_open_url=webbrowser.open(self.url_open)
