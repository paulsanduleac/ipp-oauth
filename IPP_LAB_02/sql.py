import sqlite3
pw = '2578f6eb0f643a7f65a07571033062f8659e74d676d447cc9d0a878c16c19e31' #m3g@pwd


def create_users_db():
    with sqlite3.connect("users.db") as connection:
        c = connection.cursor()
        c.execute('''CREATE TABLE users(email TEXT PRIMARY KEY, password TEXT, appid TEXT, name_surname TEXT)''')
        c.execute('''INSERT INTO users(email, password, appid, name_surname) VALUES(?,?,?,?)''', ('grea8dude@gmail.com',pw,'ap001','grea8_dude'))


def create_login_db():
    with sqlite3.connect("login.db") as connection:
        c = connection.cursor()
        c.execute('''CREATE TABLE login(email TEXT PRIMARY KEY, password TEXT, appid TEXT, timestamp TEXT, token TEXT)''')


create_users_db()
create_login_db()