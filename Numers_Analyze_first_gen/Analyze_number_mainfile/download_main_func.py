import json
import tkinter
import urllib.request
from tkinter import messagebox
class download_function:
    def __init__(self, Enter_space):
        self.entery_text=Enter_space
        self.read_respond=None
        self.header={
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Cookie":
                True}
        self.Url_Get=get_entery_text(self.entery_text)
        self.respond=None
        if self.Url_Get==None or self.Url_Get=='':
            self.error_messagebox_download=tkinter.messagebox.showerror(title="enter error", message="You MUST enter a url which you want to download!")
        else:
            self.add_url_headers=urllib.request.Request(url=self.Url_Get, headers=self.header)
            self.respond=urllib.request.urlopen(self.add_url_headers)
            self.read_respond=self.respond.read()
            self.url_type = self.respond.getheader("Content-Type")
            self.text_list_url_type = []
            for a in self.url_type:
                self.text_list_url_type.append(a)
            self.text_list_url_type.append(";")
            self.find_element = "/"
            self.element_position = self.text_list_url_type.index(self.find_element)
            self.semicolon = ";"
            self.judge_type_url = ""
            self.count_limit=None
            self.count_limit=self.text_list_url_type.index(self.semicolon)
            for b in range(self.element_position + 1, self.count_limit):
                self.judge_type_url += self.text_list_url_type[b]
            with open("url_type.json", "r", encoding="utf-8") as self.url_type_file:
                self.file_data = json.load(self.url_type_file)
            self.content = self.file_data[0]
            self.file_type_in_dic = []
            self.content_type_in_dic = []
            for d in self.content:
                self.file_type_in_dic.append(d)
            for e in self.file_type_in_dic:
                self.get_content_type = self.content[e]
                self.content_type_in_dic.append(self.get_content_type)
            self.file_type_position = self.content_type_in_dic.index(self.judge_type_url)
            self.file_type=self.file_type_in_dic[self.file_type_position]
            self.filename=self.filename_windows()
