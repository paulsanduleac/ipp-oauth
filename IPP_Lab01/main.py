# Gaiu Dorin IPP Lab 0, Prototyping
import random, string
import urllib2, json
import time
import dataModel # contains input/output data models and also the URLs

def getInputData(url): # get the json content from an URL
    response = urllib2.urlopen(url)
    code = response.getcode()
    if code == 200: # check if URL loaded correctly
        data = response.read()
        inputJSON = json.loads(data)
        return inputJSON

    else:
        print "error " + str(code)
        return None

def generateToken(length):
    return ''.join(random.choice(string.lowercase + string.digits + string.uppercase) for i in range(length))

def userRegisters(registerData):  #user registration event
    if registerData in dataModel.userList:  # check if user exists
        dataModel.outputRegisterLogin['code'] = 1
        dataModel.outputRegisterLogin['token'] = None
    else:
        # save a new user in userList and return a valid token
        dataModel.userList.append(registerData)
        dataModel.outputRegisterLogin['code'] = 0
        token = generateToken(10)
        dataModel.outputRegisterLogin['token'] = token

    return dataModel.outputRegisterLogin

def userLogins(loginData):  #login event
    for user in dataModel.userList:
        if compareDicts(loginData, user) == 4:
            dataModel.outputRegisterLogin['code'] = 0;
            token = generateToken(10)
            dataModel.outputRegisterLogin['token'] = token
            # now save the time and tokens in a list
            dataModel.loggedIn['time'] = time.time()
            dataModel.loggedIn['token'] = token
            dataModel.loggedIn['app_id'] = loginData['app_id']
            dataModel.loginList.append(dataModel.loggedIn)

        else:
            dataModel.outputRegisterLogin['code'] = 2
            dataModel.outputRegisterLogin['token'] = None

    return dataModel.outputRegisterLogin

def getLastUserLoginTime(inputData):
    for user in dataModel.loginList:
        if compareDicts(inputData, user) == 2:
            dataModel.getLastUserLoginTimeOutput['code'] = 0
            dataModel.getLastUserLoginTimeOutput['time'] = user['time']
            return dataModel.getLastUserLoginTimeOutput

    dataModel.getLastUserLoginTimeOutput['code'] = 3
    dataModel.getLastUserLoginTimeOutput['time'] = None
    return dataModel.getLastUserLoginTimeOutput


def compareDicts(dict1, dict2):
    count = 0
    for key in dict1.keys():
        if key in dict2.keys():
            count += 1  # match num
    return count


#test
userRegisters(dataModel.registerData)
userLogins(dataModel.loginData)
getLastUserLoginTime(dataModel.getLastUserLoginTimeInput)


