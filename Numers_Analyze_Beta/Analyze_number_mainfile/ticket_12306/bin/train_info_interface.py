import json
import tkinter
class train_ticket_choose_UI:
    def __init__(self, train_info, main_window_height, main_window_width):
        with open(r".\temp\station_name_info.json", "r", encoding="utf-8") as station_name:
            self.station_name_info=station_name.read()
        self.train_ticket_UI=tkinter.Toplevel()
        self.interface_width=1000
        self.interface_height=800
        self.screen_choose_ticket_x = int((main_window_width - self.interface_width)/2)
        self.screen_choose_ticket_y = int((main_window_height - self.interface_height)/2)
        self.windows_choose_ticket_position_str = "{}x{}+{}+{}".format(
            self.interface_width, self.interface_height, self.screen_choose_ticket_x, self.screen_choose_ticket_y)
        self.train_ticket_UI.geometry(self.windows_choose_ticket_position_str)
        self.scrollbar=tkinter.Scrollbar(self.train_ticket_UI)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.train_info_dict=train_info
        self.train_ticket_list = tkinter.Listbox(self.train_ticket_UI, yscrollcommand=self.scrollbar.set,
                                                 width=self.interface_width, height=self.interface_height)
        for train_ticket_info in self.train_info_dict:
            self.period_start_name=None
            self.period_end_name=None
            self.train_start_name=None
            self.train_end_name=None
            for station_name, station_code in json.loads(self.station_name_info).items():
                if train_ticket_info[list(train_ticket_info.keys())[0]][0]==station_code:
                    self.train_start_name=station_name
                elif train_ticket_info[list(train_ticket_info.keys())[0]][1]==station_code:
                    self.train_end_name=station_name
                if train_ticket_info[list(train_ticket_info.keys())[0]][2]==station_code:
                    self.period_start_name=station_name
                elif train_ticket_info[list(train_ticket_info.keys())[0]][3]==station_code:
                    self.period_end_name=station_name
            self.train_info="{}  {}-{}  {}  {}-{}  {}-{} {}".format(
                list(train_ticket_info.keys())[0], self.train_start_name, self.train_end_name, train_ticket_info[list(train_ticket_info.keys())[0]][7], self.period_start_name,
                self.period_end_name, train_ticket_info[list(train_ticket_info.keys())[0]][4], train_ticket_info[list(train_ticket_info.keys())[0]][5],
                train_ticket_info[list(train_ticket_info.keys())[0]][6])
            self.train_ticket_list.insert(tkinter.END, self.train_info)
        self.train_ticket_list.pack(side=tkinter.LEFT)
        self.scrollbar.config(command=self.train_ticket_list.yview)













