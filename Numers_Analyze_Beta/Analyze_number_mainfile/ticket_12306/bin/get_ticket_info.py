import os
import json
import tkinter
import http.cookiejar
import urllib.request
import tkinter.messagebox
class get_ticket_station_info:
    def __init__(self):

        self.station_start_symbol=None
        self.station_end_symbol=None
        self.station_name_dict={}
        self.start_city=None
        self.end_city=None
        self.date_start=None
        self.temp_dir =os.path.abspath('./temp')
        if os.path.exists(self.temp_dir):
            self.temp_dir_start=os.path.abspath("./temp/data_socket_start_station.log")
            self.temp_dir_end=os.path.abspath("./temp/data_socket_end_station.log")
            self.temp_dir_date=os.path.abspath("./temp/data_socket_start_date.log")
            with open(self.temp_dir_start, "r", encoding="utf-8") as read_start:
                self.read_condition_start=read_start.read()
            with open(self.temp_dir_end, "r", encoding="utf-8") as read_end:
                self.read_condition_end=read_end.read()
            with open(self.temp_dir_end, "r", encoding="utf-8") as read_date:
                self.read_condition_date=read_date.read()
        self.condition=(
                not os.path.exists(self.temp_dir) or self.read_condition_start==""
                or self.read_condition_end=="" or self.read_condition_date=="")
        if self.condition:
            self.error_box=tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写购票信息(出发时间, 出发车站, 到达车站)")
        else:
            self.Download_get_station_info()
    def Download_get_station_info(self):
        self.header = {
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            "User-Agent":
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            "Cookie":
                True
        }
        self.cookie_jar = http.cookiejar.CookieJar()
        self.cookie_handler = urllib.request.HTTPCookieProcessor(self.cookie_jar)
        self.opener = urllib.request.build_opener(self.cookie_handler)
        self.station_name_url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9330"
        self.train_info_url=\
            "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes={}"
        self.add_url_headers = urllib.request.Request(url=self.station_name_url, headers=self.header)
        self.response_url=urllib.request.urlopen(self.add_url_headers)
        self.station_name_info=self.response_url.read().decode("utf-8")
        self.count=0
        self.count_1 = []
        self.count_4=[]
        self.station_info_section_list_index=[]
        self.station_info_section_list=[]
        self.station_symbol_list=[]
        self.station_name_list=[]
        self.station_info_dict={}
        for every_letter in self.station_name_info:
            self.count+=1
            if every_letter=="@":
                self.station_info_section_list_index.append(self.count-1)
        for index in range(len(self.station_info_section_list_index)-1):
            self.station_info_section = ""
            for section_index in range(
                    self.station_info_section_list_index[index], self.station_info_section_list_index[index+1]):
                self.station_info_section+=self.station_name_info[section_index]
            self.station_info_section_list.append(self.station_info_section)
        for all_station in self.station_info_section_list:
            self.count_2=0
            self.count_3=0
            for symbol_index in range(len(all_station)):
                if all_station[symbol_index]=="|":
                    self.count_1.append(symbol_index)
                    self.count_2+=1
                    if self.count_2==2:
                        break
            for all_station_name_index in range(len(self.count_1)-1):
                self.station_name=""
                for station_name_index in range(self.count_1[all_station_name_index]+1, self.count_1[all_station_name_index+1]):
                    self.station_name+=all_station[station_name_index]
            self.station_name_list.append(self.station_name)
            for symbol_index_1 in range(len(all_station)):
                if all_station[symbol_index_1]=="|":
                    self.count_3+=1
                    if self.count_3==2:
                        self.count_4.append(symbol_index_1)
                    elif self.count_3==3:
                        self.count_4.append(symbol_index_1)
                        break
            for all_station_symbol_index in range(len(self.count_4)-1):
                self.station_symbol=""
                for station_symbol_index in range(self.count_4[all_station_symbol_index]+1, self.count_4[all_station_symbol_index+1]):
                    self.station_symbol+=all_station[station_symbol_index]
            self.station_symbol_list.append(self.station_symbol)
        for all_station_info_index in range(len(self.station_name_list)):
            self.station_info_dict[self.station_name_list[all_station_info_index]]=self.station_symbol_list[all_station_info_index]
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        with open(os.path.join(self.temp_dir, "station_name_info.json"), "w", encoding="utf-8") as datalog_write:
            json.dump(self.station_info_dict, datalog_write, indent=4, ensure_ascii=False)
        with open(r"./temp/data_socket_start_station.log", "r", encoding="utf-8") as datalog_city_start_read:
            self.start_city=datalog_city_start_read.read()
        with open(r"./temp/data_socket_end_station.log", "r", encoding="utf-8") as datalog_city_end_read:
            self.end_city=datalog_city_end_read.read()
        with open(r"./temp/data_socket_start_date.log", "r", encoding="utf-8") as datalog_city_start_date_read:
            self.date_start = datalog_city_start_date_read.read()
        if self.start_city not in self.station_info_dict:
            self.error_box = tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写正确的购票信息(出发时间, 出发车站, 到达车站)")
        else:
            self.station_start_symbol=self.station_info_dict[self.start_city].upper()
        if self.end_city not in self.station_info_dict:
            self.error_box = tkinter.messagebox.showerror(
                title="未找到文件",
                message="请填写正确的购票信息(出发时间, 出发车站, 到达车站)")
        else:
            self.station_end_symbol=self.station_info_dict[self.end_city].upper()
        self.train_info_url_compleat=self.train_info_url.format(self.date_start, self.station_start_symbol, self.station_end_symbol, "ADULT")
        self.add_url_headers_train_info = urllib.request.Request(url=self.train_info_url_compleat, headers=self.header)
        self.response_url_train = urllib.request.urlopen(self.add_url_headers_train_info)
        self.statude_code=self.response_url_train.getcode()
        self.train_info = self.response_url_train.read().decode("utf-8")
        print(self.train_info, self.train_info_url_compleat, self.statude_code)


















