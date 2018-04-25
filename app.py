from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, RadioField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

#config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'cklogin'
app.config['MYSQL_CUSORCLASS'] = 'DictCursor'
#initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        cur = mysql.connection.cursor()
        #get user by Username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            data = cur.fetchone()
            password = data[2]
            if sha256_crypt.verify(password_candidate, password):
                #password matched
                session['logged in'] = True
                session['username'] = username
                type = data[10]
                if type == 'Donator':
                    return redirect(url_for('donator'))
                else:
                    return redirect(url_for('donatee'))

            else:
                return render_template('passwordnotfound.html')
        else:
            return render_template('usernamenotfound.html')
    return render_template('login.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    password = sha256_crypt.encrypt(str(request.form['password']))
    name = request.form['name']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip = request.form['zip']
    email = request.form['email']
    phone = request.form['phone']
    radio = request.form['radio']

    print(username, password)

        #create cursor
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(username, password, name, street, city, state, zip, email, phone, type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (username, password, name, street, city, state, zip, email, phone, radio))

        #commit to DB
    mysql.connection.commit()
        #close connection
    cur.close()

    return redirect(url_for('success'))
    #return render_template('register.html', form=form)

@app.route('/donator')
def donator():
    return render_template('restaurant.html')

@app.route('/donatee')
def donatee():
    return render_template('shelter.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
