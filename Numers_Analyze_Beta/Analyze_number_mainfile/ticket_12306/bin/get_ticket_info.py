def get_ticket_info(self):
    self.start_station = None
    self.end_station = None
    self.ticket_date = None
    self.url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={},SZQ&ts={},GZQ&date={}&flag=N,N,Y".format(
        self.start_station, self.end_station, self.ticket_date)
    self.header = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Cookie":
            True}
    self.respond = None
    if self.Url_Get == None or self.Url_Get == '':
        self.error_messagebox_download = tkinter.messagebox.showerror(
            title="enter error", message="You MUST enter a url which you want to download!")
    else:
        self.add_url_headers = urllib.request.Request(url=self.Url_Get, headers=self.header)
        self.respond = urllib.request.urlopen(self.add_url_headers)
        self.read_respond = self.respond.read()