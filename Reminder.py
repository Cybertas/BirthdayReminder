import sys
import os.path
import smtplib
import yagmail 
import datetime
from datetime import date
#from datetime import datetime

from email.message import EmailMessage

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
  
def enterDate():
    name = input('Enter a name: ')
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    inputDate = datetime.date(year, month, day)
    date = inputDate.isoformat()
    saveDateToFile(name, date)
    

def getNotificationState():
    currentState = "True"
    if os.path.isfile('userPref.txt'):
        file = open('userPref.txt','r')
        currentState = file.read()
        file.close()
    else:
        file = open('userPref.txt','w+')
        file.write(currentState)
        file.close()
    return currentState

def changeNotificationState(state):
    file = open('userPref.txt','w+')
    if state == True:
        file.write("True")
        print('Notification has been switched on ')
    else:
        file.write("False")
        print('Notification has been switched off ')
    file.close()

def notificationState():
    noticationState = getNotificationState()
    if noticationState == "True":
        print('Notification is Enabled')
    else:
        print('Notification is Disabled')

    state = input("To Enable[0], To Disable[1], Return[2]: ")
    if(state=='0'):
        changeNotificationState(True)
    if(state=='1'):
        changeNotificationState(False)
    if(state=='2'):
        return 0   

def getBirthday():
    count = 0
    with open('nameDate.txt') as file:
        lines = file.read().splitlines() 
    file.close()
    return lines

def getBirthdayMaxtrix():
    birthdayList = getBirthday()
    birthdayMaxtrix = list(birthday.split('&') for birthday in birthdayList)
    #print(birthdayMaxtrix)
    return birthdayMaxtrix



def getBirthdayPeople():
    birthdayPeople=[]
    today = getSystemDate()
    date = today[5:]
    matrix = getBirthdayMaxtrix()
    for array in matrix:
        monthDay = array[1]
        monthDay = monthDay[5:]
        if monthDay == date:
            birthdayPeople.append(array)

    print(birthdayPeople)

def showDate():
    #display date from file 
    #check if file exist first 
    #if not exist display error 
    count = 0
    birthdayList = getBirthday()
    for date in birthdayList:
        count += 1 
        nameDate = date.replace('&', ' on ')
        print(f'Record {count}: {nameDate}')
    print(birthdayList)

def setEmail(Email):
    if os.path.isfile('Email.txt'):
        file = open('Email.txt','w')
        file.write(Email)
        file.close()
    else:
        file = open('Email.txt','w+')
        file.write(Email)
        file.close()

def getSystemDate():
    today = date.today().isoformat()
    return today 
    

def getEmail():
    file = open('Email.txt','r')
    Email = file.read()
    file.close()
    return Email

def changeEmail():
    Email = input('Enter an Email: ')
    setEmail(Email)

def sendEmail():
    notificationState = getNotificationState()
    Email = getEmail()
    if(today == true and notificationState == "True"):#check notifcation state && check date with birthday 
        #yag=yagmail.SMTP()
        contents=["happy birthday"]
        #yag.send('chris20419@gmail.com','subject',contents)
        yagmail.SMTP(Email).send(Email,'subject',contents)

def exit():
    sys.exit()




#main 
if __name__ == '__main__':
    
    getNotificationState()
    isEmailSet=os.path.isfile('Email.txt')
    if isEmailSet == False:
        changeEmail()
    while True:
        inp = input('Enter a date[0], Show Dates[1], Set Email[2], Enable/Disable Notifcation[3], Set Reminder Days[4] , Exit[5]: ')
        if(inp=='0'):
            enterDate()
        if(inp=='1'):
            showDate()
        if(inp=='3'):
            notificationState()
        if(inp=='4'):
            setReminderDay()
        if(inp=='5'):
            exit()
        if(inp=='6'):#this is to test
            getBirthdayPeople()
        #sendEmail()

        

