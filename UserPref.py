def getUserPref():
    userPrefDict={}
    with open("userPreferences.txt") as file:
        for line in file:
            (key,value) = line.rstrip('\n').split(':')
            userPrefDict[key] = value
    file.close()
    return userPrefDict

def setUserPref(userPrefDict):
    with open("userPreferences.txt", 'w') as file: 
        for key, value in userPrefDict.items(): 
            file.write('%s:%s\n' % (key, value))
    file.close()
