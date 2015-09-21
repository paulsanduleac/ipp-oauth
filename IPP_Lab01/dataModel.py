urlRegister = "http://oauthservice/register"
urlLogin = "http://oauthservice/login"
urlGetLastUserLoginTime = "http://oauthservice/get_last_login"

registerData = \
    {'app_id': '001',
     'email': 'user@mail.com',
     'pass': 'password',
     'name': 'name',
     'surname': 'surname',
     'user': 'username'}

loginData = \
    {'app_id': '001',
     'email': 'user@mail.com',
     'user': 'username',
     'pass': 'password'}

getLastUserLoginTimeInput = \
    {'app_id': '001',
     'token': 'mumbojumbo',
     'email': 'user@mail.com'
     }

outputRegisterLogin = \
    {'code': '1',
     'token': 'mumboJumbo'}

getLastUserLoginTimeOutput = \
    {'code': 'time',
     'time': 'yyyy:mm:dd:hh:mm:ss'}

loggedIn = \
    {'time': 'time',
     'token': 'token',
     'app_id': 'app-id'}


userList = []
loginList = []
