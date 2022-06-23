import os
import smtplib
import sys
import threading 
from email.message import EmailMessage

from fetchDates import *
from insertDates import enterDate, saveDateToFile
from notificationStatus import *
from sendEmail import *
from sendEmailPrep import *
from UserPref import * 

def checkDatesBackgroundProcess():
    backGroundCheckBirthday = threading.Timer(3600.0, sendEmail())
    backGroundCheckBirthday.start()


#main 
if __name__ == '__main__':
    userPreferences = os.path.isfile('userPreferences.txt')
    if userPreferences == False:
        Email=input('Set Up - Enter Email: ')
        daysBeforeBD=input('Set Up - Enter number of days before birthday: ')
        notificationStat = input('Set Up - Enter 0 to endable email notifcation, 1 to disable: ')
        initalPreference = {
            "Email":Email,
            "ReminderDay":daysBeforeBD,
            "notificationStatus":notificationStat,
        }
        with open("userPreferences.txt", 'w') as file: 
            for key, value in initalPreference.items(): 
                file.write('%s:%s\n' % (key, value))
        file.close()
    while True:
        inp = input('Enter a date[0], Show Dates[1], Set Email[2], Enable/Disable Notifcation[3], Set Reminder Days[4] , Exit[5]: ')
        if(inp=='0'):
            enterDate()
        if(inp=='1'):
            showDate()
        if(inp=='2'):
            changeEmail()
        if(inp=='3'):
            notificationState()
        if(inp=='4'):
            setReminderDay()
        if(inp=='5'):
            sys.exit()
        if(inp=='6'):
            sendEmail()

        

