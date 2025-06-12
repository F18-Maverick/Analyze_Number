import os
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class get_ticket:
    def __init__(self, train_code, choose_start_station, choose_end_station, train_go_date, condition, choose_index_train):
        self.button_xpath=None
        self.train_code_index=-1
        self.onclick_condition=0
        self.abs_dir=os.path.dirname(os.path.abspath(__file__))
        self.train_go_date=train_go_date
        self.train_code = train_code
        self.choose_start_station=choose_start_station
        self.choose_end_station=choose_end_station
        self.condition=condition
        print(self.choose_start_station, "...", self.choose_end_station)
        self.choose_index_train=choose_index_train
        self.options=Options()
        self.init_url="https://kyfw.12306.cn/otn/leftTicket/init"
        #self.options.add_argument('--headless')
        self.options.binary_location="{}/firefox_linux/firefox".format(self.abs_dir)
        self.firefox_web_driver=Service(executable_path="{}/geckodriver-v0.36.0-linux64/geckodriver".format(self.abs_dir))
        self.driver=webdriver.Firefox(service=self.firefox_web_driver, options=self.options)
        self.contant=self.driver.get(self.init_url)
        self.get_button()
        self.web_get_ticket()
    def get_button(self):
        if self.condition == "1":
            for index in range(self.train_code):
                self.train_code_index += 2
        elif self.condition == "2":
            for index in range(self.choose_index_train[0] + 1):
                self.train_code_index += 2
        try:
            self.button_xpath = (
                "/html/body/div[2]/div[7]/div[13]/table/tbody/tr[{}]/td[13]/a".format(self.train_code_index))
            self.onclick_condition+=1
        except:
            tkinter.messagebox.showerror(
                title="Get ticket error", message="Can not get ticket correctly, please try should these bug in our github issues")
    def web_get_ticket(self):
        self.from_station_input = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "fromStationText")))
        self.from_station_input.clear()
        self.from_station_input.click()
        self.from_station_input.send_keys(self.choose_start_station)
        self.from_station_input.send_keys(Keys.ENTER)
        self.end_station_input = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "toStationText")))
        self.end_station_input.clear()
        self.end_station_input.click()
        self.end_station_input.send_keys(self.choose_end_station)
        self.end_station_input.send_keys(Keys.ENTER)
        self.date_input = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "train_date")))
        self.date_input.clear()
        self.date_input.click()
        self.date_input.send_keys(self.train_go_date)
        self.date_input.send_keys(Keys.ENTER)
        self.button_get_left_ticket = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.ID, "query_ticket")))
        self.button_get_left_ticket.click()
        self.button_get_choose_ticket = WebDriverWait(self.driver, timeout=20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_xpath)))
        self.button_get_choose_ticket.click()























