class get_entery_text:
    def __init__(self, entery_text):
        self.entery=entery_text
        self.url_get()
    # 将要被点击Button事件触发的获取URL输入框中的函数
    def url_get(self):
        self.entery_get = self.entery.get()
        return self.entery_get
