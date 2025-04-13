import json
import tkinter
from tkinter import font
class train_ticket_choose_UI:
    def __init__(self, train_info, main_window_height, main_window_width):
        self.text_font=font.Font(family="微软雅黑", size=10)
        self.sapce_length=self.text_font.measure(" ")
        self.text_info = self.text_font.metrics()
        self.text_height = self.text_info["ascent"] + self.text_info["descent"]
        with open(r".\temp\station_name_info.json", "r", encoding="utf-8") as station_name:
            self.station_name_info=station_name.read()
        self.train_ticket_UI=tkinter.Toplevel()
        self.interface_width=1000
        self.interface_height=800
        self.ListBox_width=self.interface_width
        self.ListBox_height=int(self.interface_height/self.text_height+1)
        self.every_lettice_length=self.ListBox_width/6
        self.screen_choose_ticket_x = int((main_window_width - self.interface_width)/2)
        self.screen_choose_ticket_y = int((main_window_height - self.interface_height)/2)
        self.windows_choose_ticket_position_str = "{}x{}+{}+{}".format(
            self.interface_width, self.interface_height, self.screen_choose_ticket_x, self.screen_choose_ticket_y)
        self.train_ticket_UI.geometry(self.windows_choose_ticket_position_str)
        self.train_info_dict=train_info
        self.scrollbar=tkinter.Scrollbar(self.train_ticket_UI)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.train_ticket_list = tkinter.Listbox(
            self.train_ticket_UI, yscrollcommand=self.scrollbar.set, width=self.ListBox_width, height=self.ListBox_height)
        for train_ticket_info in self.train_info_dict:
            self.period_start_name=None
            self.period_end_name=None
            self.train_start_name=None
            self.train_end_name=None
            self.train_number=list(train_ticket_info.keys())[0]
            self.left_ticket_info=train_ticket_info[self.train_number][7]
            self.period_start_time=train_ticket_info[self.train_number][4]
            self.period_end_time=train_ticket_info[self.train_number][5]
            self.need_time=train_ticket_info[self.train_number][6]
            for station_name, station_code in json.loads(self.station_name_info).items():
                if train_ticket_info[list(train_ticket_info.keys())[0]][0]==station_code:
                    self.train_start_name=station_name
                elif train_ticket_info[list(train_ticket_info.keys())[0]][1]==station_code:
                    self.train_end_name=station_name
                if train_ticket_info[list(train_ticket_info.keys())[0]][2]==station_code:
                    self.period_start_name=station_name
                elif train_ticket_info[list(train_ticket_info.keys())[0]][3]==station_code:
                    self.period_end_name=station_name
            self.complete_peorid_station="{}-{}".format(self.train_start_name, self.train_end_name)
            self.choose_peorid_station="{}-{}".format(self.period_start_name, self.period_end_name)
            self.choose_time_peorid="{}-{}".format(self.period_start_time, self.period_end_time)
            self.space_length_1=int((self.every_lettice_length-self.text_font.measure(self.train_number))/self.sapce_length)
            self.space_length_2=int((self.every_lettice_length-self.text_font.measure(self.complete_peorid_station))/self.sapce_length)
            self.space_length_3=int((self.every_lettice_length-self.text_font.measure(self.left_ticket_info))/self.sapce_length)
            self.space_length_4=int((self.every_lettice_length-self.text_font.measure(self.choose_peorid_station))/self.sapce_length)
            self.space_length_5=int((self.every_lettice_length-self.text_font.measure(self.choose_time_peorid))/self.sapce_length)
            self.train_info="{}{}{}{}{}{}{}{}{}{}{}".format(
                self.train_number, " "*self.space_length_1, self.complete_peorid_station, " "*self.space_length_2, self.left_ticket_info,
                " "*self.space_length_3, self.choose_peorid_station, " "*self.space_length_4, self.choose_time_peorid, " "*self.space_length_5, self.need_time)
            self.train_ticket_list.insert(tkinter.END, self.train_info)
        self.train_ticket_list.pack(side=tkinter.BOTTOM)
        self.scrollbar.config(command=self.train_ticket_list.yview)
        self.title_list=["车次", "列车始发/终点站", "余票情况", "选择的始发/终点站", "列车始发/终到时间", "中途耗时"]
        self.space_num_list=[]
        self.title_each_length=self.interface_width/6
        for titles in self.title_list:
            self.space_length=int((self.title_each_length-self.text_font.measure(titles))/self.sapce_length)
            self.space_num_list.append(self.space_length)
        self.title_complete="{}{}{}{}{}{}{}{}{}{}{}{}".format(
            self.title_list[0], self.space_num_list[0]*" ", self.title_list[1], self.space_num_list[1]*" ", self.title_list[2], self.space_num_list[2]*" ",
            self.title_list[3], self.space_num_list[3]*" ", self.title_list[4], self.space_num_list[4]*" ", self.title_list[5], self.space_num_list[5]*" ")
        self.title_label=tkinter.Label(self.train_ticket_UI, text=self.title_complete, font=self.text_font)
        self.title_label.pack(side=tkinter.TOP)
    def button_each_ticket(self):
        pass












