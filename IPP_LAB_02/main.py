from flask import Flask, render_template, request, flash
import time, sqlite3, random, string
app = Flask(__name__)

def hash_data(buf):  # used for hashing passwords and tokens
    import hashlib
    h = hashlib.sha256()
    h.update(buf)
    return h.hexdigest()

def gen_token(length): # used for generating a random token
    token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    return hash_data(token)

def timestamp_to_readable(timestamp): # converting a UNIX timestamp into readable format
    import datetime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

@app.route("/")
def homepage():
    try:
        title = "Menu"
        return render_template("Homepage.html", title=title)
    except Exception, e:
        return str(e)


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    try:
        title = "Registration"
        if request.method == 'POST':
            appID = request.form['appID']
            name_surname = request.form['name_surname']
            mail = request.form['email']
            password = request.form['password']
            with sqlite3.connect("data_users.db") as connection:
                c = connection.cursor()
                c.execute('SELECT email FROM users WHERE email=?', (mail,))
                row = c.fetchone()
                if row is None:
                    c.execute('''INSERT INTO users(email, password, appid, name_surname) VALUES(?,?,?,?)''', (mail, hash_data(password), appID, name_surname))
                    c.close()
                    return "User succesfully registered." + "<br> <a href='/'>Return to menu</a>"
                else:
                    c.close()
                    return "A user with this email already exists. Please try using a different email address." + "<br> <a href='/'>Return to menu</a>"

        return render_template("Registration.html", title=title)
    except Exception, e:
        return str(e)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    try:
        title = "Login"
        if request.method == 'POST':
            current_time = time.time()
            login_id = gen_token(150)
            appID = request.form['appID']
            mail = request.form['email']
            password = request.form['password']
            with sqlite3.connect("data_users.db") as connection:
                c = connection.cursor()
                c.execute('SELECT email,password FROM users WHERE email=? AND password=? AND appid=?', (mail,hash_data(password),appID,))
                response = c.fetchone()
                c.close()
                if response is None:
                    return "Error" + "<br> <a href='/'>Return to menu</a>"
                else:
                    with sqlite3.connect("data_logins.db") as conn:
                        c_login = conn.cursor()
                        token = gen_token(150)
                        c_login.execute('''INSERT INTO login(login_id, email, password, appid, timestamp, token) VALUES(?,?,?,?,?,?)''', (login_id, mail, hash_data(password), appID, current_time, token))
                        c_login.close()
                    return "Successflly logged in. Your token is:" + token + "<br> <a href='/'>Return to menu</a>"

        return render_template("Login.html", title=title)

    except Exception, e:
        return str(e)


@app.route('/stats/', methods=['POST', 'GET'])
def stats():
    try:
        title = "stats"
        if request.method == 'POST':
            appID = request.form['appID']
            email = request.form['email']
            token = request.form['token']
            with sqlite3.connect("data_logins.db") as connection:
                c = connection.cursor()
                c.execute('SELECT * FROM login WHERE appid=? AND token=? and email=?', (appID,token,email,))
                response = c.fetchone()
                c.close()
                if response is None:
                    return "Invalid Data" + "<br> <a href='/'>Return to menu</a>"
                else:
                    return "Login date: " + timestamp_to_readable(float(response[4])) + "<br> <a href='/'>Return to menu</a>"
        return render_template("Stats.html", title=title)

    except Exception, e:
        return str(e)

if __name__ == '__main__':
    app.run()


