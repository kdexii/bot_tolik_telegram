#   import library
from tkinter import *
import tkcalendar
from datetime import timedelta
import json, requests
from requests.api import get
import telebot
import sys
token = '1943394345:AAGOULIQSLKuGSW6NKUyhIdExkYcLrQFpy8'
chat_id = -579353316
question = 'Ретро (Время МСК)'
telegram_poll_url = f'https://api.telegram.org/bot{token}/sendPoll?'

main = Tk()

def getDateRange(start,stop):
    global datesDirt
    datesDirt = []
    tkdate = (stop-start).days
    for i in range(tkdate+1):
        day = start + timedelta(days=i)
        datesDirt.append(day)
        
    if datesDirt:
        
        datesDirt = [x.strftime('%Y-%m-%d') for x in datesDirt]
        a = len(datesDirt)
        count = - 1
        listdate = []
        while count <= int(a) - 2:
            count = count + 1
            # print(dates[count] + ' 10:00 - 13:00') # if u want see this trash = uncomment
            listdate.append(datesDirt[count] + ' 10:00 - 13:00')
            # print(dates[count] + ' 13:00 - 16:00')
            listdate.append(datesDirt[count] + ' 13:00 - 16:00')
        quesUrl = f'{telegram_poll_url}chat_id={chat_id}&'\
        f'question={question}&options={json.dumps(listdate)}'\
        f'&is_anonymous=false'
        get(quesUrl)
        # print(quesUrl)
        

    else:
        print('Date pool is incorrect')
    sys.exit()
firstDate = tkcalendar.DateEntry(main)
firstDate.pack(padx=10,pady=10)

secondDate = tkcalendar.DateEntry(main)
secondDate.pack(padx=10,pady=10)

Button(main,text='Send question',command=lambda: getDateRange(firstDate.get_date(),secondDate.get_date())).pack() 

main.mainloop()
