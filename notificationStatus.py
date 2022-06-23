from UserPref import *

def getNotificationState():
    userPrefDict = {}
    userPrefDict=getUserPref()
    notificationState = userPrefDict["notificationStatus"]
    #print(notificationState)
    return notificationState

def setNotificationState(state):
    userPrefDict = {}
    userPrefDict=getUserPref()
    if(state=='0'):
        userPrefDict["notificationStatus"] = "0"
        setUserPref(userPrefDict)
        return 0 
    if(state=='1'):
        userPrefDict["notificationStatus"] = "1"
        setUserPref(userPrefDict)
        return 0 
    if(state=='2'):
        return 0   
   
def notificationState():
    noticationState = getNotificationState()
    if noticationState == "0":
        print('Notification is Enabled')
    else:
        print('Notification is Disabled')

    state = input("To Enable[0], To Disable[1], Return[2]: ")
    setNotificationState(state)

