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

    return render_template('success.html')
    #return render_template('register.html', form=form)

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
