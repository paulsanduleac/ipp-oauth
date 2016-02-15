# Run this to create the two SQL databases (users and login)

import sqlite3

def create_users_db(): 
    with sqlite3.connect("data_users.db") as connection:
        c = connection.cursor()
        c.execute('''CREATE TABLE users(email TEXT PRIMARY KEY, password TEXT, appid TEXT, name_surname TEXT)''')

def create_login_db():
    with sqlite3.connect("data_logins.db") as connection:
        c = connection.cursor()
        c.execute('''CREATE TABLE login(login_id TEXT PRIMARY KEY, email TEXT, password TEXT, appid TEXT, timestamp TEXT, token TEXT)''')

create_users_db()
create_login_db()