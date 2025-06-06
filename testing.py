from core import *
import time

accounts = {"Abdur_up82":"277353*Is","SomeShit91":"WrongPassword","vedal987":"BananaRum"}
timeout = 5

right = 0
wrong = 0

right_l = []
wrong_l = []

def test_auth(accounts):
    global right
    global wrong
    global right_l
    global wrong_l
    acc_={}
    for i,j in accounts.items():
        acc_[i] = MyStat(i,j)
        if acc_[i].get_auth()[0] == True:
            right+=1
            right_l.append(i)
        else:
            wrong+=1
            wrong_l.append(i)
        print("В прогрессе...")
        time.sleep(timeout)

test_auth(accounts)
if(right>0 and wrong>0):
    print(f"Из данного списка {right} аккаунтов подходят ({right_l})\nА также {wrong} аккаунтов не подходят ({wrong_l})")
elif(right>0 and wrong==0):
    print(f"Из данного списка все аккаунты верны ({right_l})")
else:
    print(f"Из данного списка все аккаунты неверны ({wrong_l})")
