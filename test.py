#   import library
from tkinter import *
import tkcalendar
from datetime import timedelta
import json
from requests.api import get
import locale
from tkinter import messagebox

token = '1943394345:AAGOULIQSLKuGSW6NKUyhIdExkYcLrQFpy8'
chat_id = -599179418
question = 'Ретро (Время МСК)'
telegram_poll_url = f'https://api.telegram.org/bot{token}/sendPoll?'
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

main = Tk()
main.geometry("750x450")

def getDateRange(start,stop):
    
    datesDirt = []
    tkdate = (stop-start).days
    for i in range(tkdate+1):
        day = start + timedelta(days=i)
        datesDirt.append(day)
    lenDate = len(datesDirt)
    if datesDirt:
        
        datesDirt = [x.strftime('%A %d-%m') for x in datesDirt]
        a = len(datesDirt)
        count = - 1
        listdate = []
        while count <= int(a) - 2:
            count = count + 1
            listdate.append(datesDirt[count] + ' 10:00 - 13:00')
            listdate.append(datesDirt[count] + ' 13:00 - 16:00')
        quesUrl = f'{telegram_poll_url}chat_id={chat_id}&'\
        f'question={question}&options={json.dumps(listdate)}'\
        f'&is_anonymous=false'

        if int(lenDate) > 5:
            messagebox.showinfo("Error!","The maximum range of the pool is 5")
            pass
        else:
            
            get(quesUrl)
            messagebox.showinfo("Success!","Poll send to group!")
            pass

    else:
        # print('Date pool is incorrect')
        messagebox.showinfo("Error","Date pool is incorrect")
        pass
    # sys.exit()
firstDate = tkcalendar.DateEntry(main)
firstDate.pack(padx=10,pady=10)

secondDate = tkcalendar.DateEntry(main)
secondDate.pack(padx=10,pady=10)

Button(main,text='Send question',command=lambda: getDateRange(firstDate.get_date(),secondDate.get_date())).pack() 

main.mainloop()
