import threading
from bin import get_ticket_info
from choose_start_time_UI import choose_start_time
from choose_end_station_UI import choose_end_station
from choose_start_station_UI import choose_start_station
class thread_all:
    def choose_start_station_UI_thread(self, computer_width, computer_height):
        self.thread_choose_UI=threading.Thread(target=choose_start_station, args=(computer_width, computer_height),
                                               name="thread1", daemon=True)
        self.thread_choose_UI_start=self.thread_choose_UI.start()
    def choose_end_station_UI_thread(self, computer_width, computer_height):
        self.thread_choose_UI=threading.Thread(target=choose_end_station, args=(computer_width, computer_height),
                                               name="thread2", daemon=True)
        self.thread_choose_UI_end=self.thread_choose_UI.start()
    def choose_start_time_UI_thread(self, computer_width, computer_height):
        self.thread_choose_UI=threading.Thread(target=choose_start_time, args=(computer_width, computer_height),
                                               name="thread3", daemon=True)
        self.thread_choose_UI_date=self.thread_choose_UI.start()
    def download_ticket_station_info_thread(self):
        self.thread_station_info=threading.Thread(
            target=get_ticket_info.get_ticket_station_info, name="thread4", daemon=True)
        self.thread_station_name=self.thread_station_info.start()












