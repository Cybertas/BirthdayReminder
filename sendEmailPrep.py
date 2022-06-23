from UserPref import * 


def changeEmail():
    Email = input('Enter an Email: ')
    setEmail(Email)

def setEmail(Email):
    userPrefDict = {}
    userPrefDict=getUserPref()
    userPrefDict['Email'] = Email
    setUserPref(userPrefDict)
    print('Email has been set to: '+Email)
    return 0 

def getEmail():
    userPrefDict = {}
    userPrefDict=getUserPref()
    Email = userPrefDict['Email']
    return Email
