import os
import sys
import tkinter.messagebox
from selenium import webdriver
from . import browsers_searcher
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class get_ticket:
    def __init__(self, train_code, choose_start_station, choose_end_station, train_go_date, condition, choose_index_train):
        self.init_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.button_xpath = None
        self.train_code_index = -1
        self.onclick_condition = 0
        self.train_go_date = train_go_date
        self.train_code = train_code
        self.choose_start_station = choose_start_station
        self.choose_end_station = choose_end_station
        self.condition = condition
        self.choose_index_train = choose_index_train
        self.open_browsers()
        self.get_button()
    def open_browsers(self):
        self.count=0
        self.abs_dir = os.path.dirname(os.path.abspath(__file__))
        self.inborn_driver_list=["firefox", "waterfox", "firefox-developer", "firefox-nightly", "msedge", "msedge-dev", "msedge-beta",
                                 "msedge-canary", "chromium", "chrome", "chrome-canary", "chrome-dev", "ungoogled-chromium"]
        self.browsers_list=browsers_searcher.get()
        self.choosed_driver_type_list=[]
        self.choosed_driver_name_list=[]
        self.choosed_browsers_dir_list=[]
        self.browsers_dir_list=[]
        self.system_type=sys.platform
        self.choosed_driver=None
        self.choosed_driver_name=None
        self.browser_dir=None
        for inborn_driver in self.inborn_driver_list:
            for host_browser in self.browsers_list:
                if inborn_driver==host_browser["browser_type"]:
                    self.choosed_driver=inborn_driver
                    self.browser_dir=host_browser["path"]
                    self.browsers_dir_list.append(self.browser_dir)
                    if (self.system_type=="win32" or self.system_type=="cygwin" or self.system_type=="win64"
                        or self.system_type=="windows" or self.system_type=="Windows"):
                        if (self.choosed_driver=="firefox" or self.choosed_driver=="waterfox" or self.choosed_driver=="firefox-developer"
                            or self.choosed_driver=="firefox-nightly"):
                            self.choosed_driver_name="geckodriver.exe"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver=="msedge" or self.choosed_driver=="msedge-dev" or self.choosed_driver=="msedge-beta"
                              or self.choosed_driver=="msedge-canary"):
                            self.choosed_driver_name="msedgedriver.exe"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif self.choosed_driver=="chromium" or self.choosed_driver=="chrome" or self.choosed_driver=="chrome-canary":
                            self.choosed_driver_name="chromedriver.exe"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        else:
                            tkinter.messagebox.showerror(
                                title="不兼容",
                                message="本项目未自带本机中浏览器的驱动程序。请阅读readme文件，并指定驱动和下载地址。如问题仍未解决，请发布issue")
                    elif self.system_type=="linux" or self.system_type=="Linux":
                        if self.choosed_driver=="firefox" or self.choosed_driver=="waterfox":
                            self.choosed_driver_name="geckodriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif self.choosed_driver=="msedge" or self.choosed_driver=="msedge-dev":
                            self.choosed_driver_name="msedgedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver=="chrome" or self.choosed_driver=="chrome-dev" or self.choosed_driver=="chromium"
                              or self.choosed_driver=="ungoogled-chromium"):
                            self.choosed_driver_name="chromedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        else:
                            tkinter.messagebox.showerror(
                                title="不兼容",
                                message="本项目未自带本机中浏览器的驱动程序。请阅读readme文件，并指定驱动和下载地址。如问题仍未解决，请发布issue")
                    elif self.system_type=="darwin":
                        if (self.choosed_driver_name=="firefox" or self.choosed_driver_name=="firefox-developer" or
                            self.choosed_driver_name=="firefox-nightly"):
                            self.choosed_driver_name = "geckodriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver_name=="msedge" or self.choosed_driver_name=="msedge-beta" or
                              self.choosed_driver_name=="msedge-dev" or self.choosed_driver_name=="msedge-canary"):
                            self.choosed_driver_name = "msedgedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        elif (self.choosed_driver=="chrome" or self.choosed_driver=="chrome-beta" or self.choosed_driver=="chrome-canary"
                              or self.choosed_driver=="chrome-dev" or self.choosed_driver_name=="chrome-test" or
                              self.choosed_driver_name=="chromium"):
                            self.choosed_driver_name="chromedriver"
                            self.choosed_driver_name_list.append(self.choosed_driver_name)
                            self.choosed_driver_type_list.append(self.choosed_driver)
                            self.choosed_browsers_dir_list.append(self.browser_dir)
                        else:
                            tkinter.messagebox.showerror(
                                title="不兼容",
                                message="本项目未自带本机中浏览器的驱动程序。请阅读readme文件，并指定驱动和下载地址。如问题仍未解决，请发布issue")
                    else:
                        tkinter.messagebox.showerror(
                            title="不兼容",
                            message="如果您正在使用源码运行该项目，说明该源码暂时不兼容您的操作系统，请阅读readme文件并安装本项目以更好的兼容。如问题仍未解决，请发布issue")
        print(self.choosed_driver_type_list, "...", self.choosed_driver_name_list, "...", self.choosed_browsers_dir_list, "...", self.browsers_dir_list)
        for index in range(len(self.choosed_driver_name_list)):
            self.driver_dir = os.path.join(self.abs_dir, "driver", self.choosed_driver_name_list[index])
            self.options = Options()
            # self.options.add_argument('--headless')
            self.options.binary_location=self.browsers_dir_list[index]
            try:
                if (self.choosed_driver_type_list[index]=="firefox" or self.choosed_driver_type_list[index]=="waterfox"
                    or self.choosed_driver_type_list[index]=="firefox-developer"):
                    self.web_driver=Service(executable_path=self.driver_dir)
                    self.driver = webdriver.Firefox(service=self.web_driver, options=self.options)
                    self.contant=self.driver.get(self.init_url)
                    self.web_get_ticket()
                elif (self.choosed_driver_type_list[index]=="msedge" or self.choosed_driver_type_list[index]=="msedge-dev"
                      or self.choosed_driver_type_list[index]=="msedge-beta" or self.choosed_driver_type_list[index]=="msedge-canary"):
                    self.web_driver = Service(executable_path=self.driver_dir)
                    self.driver=webdriver.Edge(service=self.web_driver, options=self.options)
                    self.contant=self.driver.get(self.init_url)
                    self.web_get_ticket()
                elif (self.choosed_driver_type_list[index]=="chrome" or self.choosed_driver_type_list[index]=="chrome-dev"
                      or self.choosed_driver_type_list[index]=="chromium" or self.choosed_driver_type_list[index]=="chrome-canary"
                      or self.choosed_driver_type_list[index]=="ungoogled-chromium"):
                    self.web_driver = Service(executable_path=self.driver_dir)
                    self.driver=webdriver.Chrome(service=self.web_driver, options=self.options)
                    self.contant=self.driver.get(self.init_url)
                    self.web_get_ticket()
                else:
                    tkinter.messagebox.showerror(title="Error", message="Error")
            except:
                pass
            self.count+=1
        if self.count==len(self.choosed_driver_name_list):
            tkinter.messagebox.showerror(title="Error", message="无法使用任何浏览器，请提交issues至该项目的GitHub仓库")
        else:
            pass
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
                title="Get ticket error", message="Can not get ticket correctly, please try share these bug in our github issues")
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























