import os.path
import datetime
from datetime import date

def enterDate():
    name = input('Enter a name: ')
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    inputDate = datetime.date(year, month, day)
    date = inputDate.isoformat()
    saveDateToFile(name, date)

def saveDateToFile(name,date):
    #open file 
    #write to file 
    #close file 
    if os.path.isfile('nameDate.txt'):
        file = open('nameDate.txt','a')
        file.write(name+'&'+date+"\n")
        file.close()
    else:
        file = open('nameDate.txt','w+')
        file.write(name+'&'+date+"\n")
        file.close()