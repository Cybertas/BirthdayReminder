from datetime import date
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
    print('today is: '+today)
    matrix = getBirthdayMaxtrix()
    for array in matrix:
        monthDay = array[1]
        monthDay = monthDay[5:]
        print('birthday is: '+monthDay)
        if monthDay == today:
            birthdayPeople.append(array)

    #print(birthdayPeople)
    return birthdayPeople

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

def getSystemDate():
    today = date.today().isoformat()
    today = today[5:]
    return today 
    