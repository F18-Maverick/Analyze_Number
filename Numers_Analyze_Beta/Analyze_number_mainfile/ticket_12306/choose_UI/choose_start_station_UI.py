import tkinter
from ..analyze_json.analyze_city_json import all_city
from ..analyze_json.analyze_city_station_json import all_city_station
class choose_start_station:
    def __init__(self, computer_info_width, computer_info_height):
        self.all_city_name=all_city().get_city_name()
        self.all_city_adCode=all_city().get_city_adCode()
        self.all_city_code=all_city().get_city_code()
        self.all_city_station_name=all_city_station().get_station_name()
        self.all_city_station_first_code=all_city_station().get_station_first_code()
        self.all_city_station_generateId=all_city_station().get_station_generatedId()
        self.all_city_station_ID=all_city_station().get_station_Id()
        self.all_city_station_pycode=all_city_station().get_station_py_code()
        self.windows_choose_start_station = tkinter.Toplevel()
        self.windows_choose_start_station_icon = self.windows_choose_start_station.iconbitmap(
            r"./ticket_12306_prog_addition/download_photo.ico")
        self.start_station_entery = tkinter.Entry(
            self.windows_choose_start_station, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=40, relief="solid", insertwidth=1)
        self.x_entry = 50
        self.y_entry = 80 / 3
        self.start_station_entery.place(x=self.x_entry, y=self.y_entry)
        self.title_1 = self.windows_choose_start_station.title("请选择出发车站")
        self.windows_choose_start_station_height = 300
        self.windows_choose_start_station_width = 500
        self.unresizeable = self.windows_choose_start_station.resizable(False, False)
        self.screen_choose_start_station_x = int((computer_info_width - self.windows_choose_start_station_width) / 2)
        self.screen_choose_start_station_y = int((computer_info_height - self.windows_choose_start_station_height) / 2)
        self.windows_choose_start_station_position_str = "{}x{}+{}+{}".format(
            self.windows_choose_start_station_width, self.windows_choose_start_station_height,
            self.screen_choose_start_station_x, self.screen_choose_start_station_y)
        self.New_choose_start_station_Windows = self.windows_choose_start_station.geometry(
            self.windows_choose_start_station_position_str)





