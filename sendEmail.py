import yagmail

from fetchDates import *
from notificationStatus import *
from sendEmailPrep import *


def sendEmail():
    notificationState = getNotificationState()
    Email = getEmail()
    today = getSystemDate()
    birthdayPeopleList = []
    birthdayPeopleList = getBirthdayPeople()
    
    if(len(birthdayPeopleList)>0 and notificationState == "0"):#check notifcation state && check date with birthday 
        #yag=yagmail.SMTP()
        bDayList = []
        text = 'Happy birthday to '
        for item in birthdayPeopleList:
            item=' '.join(item)
            bDayList.append(item)
        bDayList.insert(0,text)
        yagmail.SMTP(Email).send(Email,'Birthday Reminder',bDayList)
