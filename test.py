#   import library
from tkinter import *
import tkcalendar
from datetime import timedelta
import json
from requests.api import get
import locale
from tkinter import messagebox
from datetime import datetime
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

#   the values we need to send

token = '1943394345:AAGOULIQSLKuGSW6NKUyhIdExkYcLrQFpy8'
chat_id = -579353316
question = 'Ретро (Время МСК)'
telegram_poll_url = f'https://api.telegram.org/bot{token}/sendPoll?'

#   --------------------------

""" Get today date for tkinter  """

сurrent_date = datetime.now().date()
start = сurrent_date
stop = сurrent_date

""" Open calendar GUI in new window """

main = Tk()
main.geometry("750x450")

def getDateRange(start,stop):
    
    """ User selects dates  """

    datesDirt = []
    tkdate = (stop-start).days
    for i in range(tkdate+1):
        day = start + timedelta(days=i)
        datesDirt.append(day)
    lenDate = len(datesDirt)

    if datesDirt:

        """ Checking the date for correct   """

        datesDirt = [x.strftime('%A %d-%m') for x in datesDirt]

        a = len(datesDirt)
        count = - 1
        listdate = []

        """ Recording of all received dates with duplication """

        while count <= int(a) - 2:
            count = count + 1
            listdate.append(datesDirt[count] + ' 10:00 - 13:00')
            listdate.append(datesDirt[count] + ' 13:00 - 16:00')

        """ Forming a request to the API """

        quesUrl = f'{telegram_poll_url}chat_id={chat_id}&'\
        f'question={question}&options={json.dumps(listdate)}'\
        f'&is_anonymous=false'

        """ Check for the number of dates entered, should not exceed 5 """

        if int(lenDate) > 5:
            messagebox.showinfo("Error!","The maximum range of the pool is 5")
            pass
        else:
            
            get(quesUrl)
            messagebox.showinfo("Success!","Poll send to group!")
            pass

    else:
        messagebox.showinfo("Error","Date pool is incorrect")
        pass
firstDate = tkcalendar.DateEntry(main)
firstDate.pack(padx=10,pady=10)

secondDate = tkcalendar.DateEntry(main)
secondDate.pack(padx=10,pady=10)

Button(main,text='Send pool question to group',command=lambda: getDateRange(firstDate.get_date(),secondDate.get_date())).pack() 

main.mainloop()