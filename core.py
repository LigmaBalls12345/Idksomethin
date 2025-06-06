import requests
import tkinter as tk
from tkinter import scrolledtext
import json
from config import TIMEOUT, PROXY

def tkinter_window(data_dict):
    window = tk.Tk()
    window.title("Данные уроков")
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20)
    text_area.pack(padx=10, pady=10)
    formatted_data = json.dumps(data_dict, ensure_ascii=False, indent=4)
    text_area.insert(tk.END, formatted_data)
    window.mainloop()

class MyStat:
    def __init__(self,login,password):
        self.login = login
        self.password = password
    
    def get_auth(self):
        url = "https://mapi.itstep.org/v1/mystat/auth/login"
        headers = {"accept": "application/json"}
        data = {"login": self.login, "password": self.password}
         
        response = requests.post(url, headers=headers, data = data)
        if(response.status_code == 200):
            return True,response.text
        else:
            return False,None
        
    def get_marks(self):
        time.sleep(TIMEOUT)
        result = self.get_auth()
        if(result[0] == False):
            return False
        else:
            url = "https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks"
            headers = {"authorization":f"Bearer {result[1]}"}
            response = requests.get(url,headers=headers)
            if(response.status_code == 200):
                return response.text
            else:
                return False

    def get_dates(self,date):
        result = self.get_auth()
        if(result[0] == False):
            return False
        else:
            url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=month&date_filter={date}"
            headers = {"authorization":f"Bearer {result[1]}"}
            response = requests.get(url,headers=headers)
            if(response.status_code == 200):
                tkinter_window(response.json())
            else:
                return False

    def get_average_mark(self):
        result = self.get_auth()
        if(result[0] == False):
            return False
        else:
            url = "https://mapi.itstep.org/v1/mystat/aqtobe/statistic/progress?period=year"
            headers = {"authorization":f"Bearer {result[1]}"}
            response = requests.get(url,headers=headers)
            if(response.status_code == 200):
                data = response.json()
                total_average_point = data.get("total_average_point")
                print(total_average_point)
            else:
                return False
