from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('user-form.html')

@app.route('/', methods=['POST'])
def verify_form():

    user_name = request.form['user_name']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    nono = " "
    user_name_error=""
    password_error=""
    password_v_error=""
    email_error=""

    if len(user_name) == 0:
        user_name_error = "Please give a Username"

    elif len(user_name) < 3:
        user_name_error = "Sorry, that user name is too short!"

    elif len(user_name) > 20:                         #Verify Username
        user_name_error = "Sorry, that user name is too long!"

    elif nono in user_name:
        user_name_error = "Sorry, spaces are not allowed!"


    if len(password) == 0:
        password_error = "Please give a password"
        password = ""
    elif len(password) < 3:
        password_error = "Your password is too short!"
        password = ""                                    #Checks password validity
    elif len(password) > 20:
        password_error = "Your password is too long!"
        password = ""
    elif nono in password:
        password_error = "Sorry, spaces aren't allowed you dummy!"
        password =""

    if password != verify_password:                      #Verify password
        password_v_error = "Passwords do not match!"
        password = ""
        verify_password = ""

    goodie1 = "@"
    goodie2 = "."

    if not email:
        email_error = ""
    elif len(email) > 20:
        email_error = "I'm sorry, that email address is too long!"

    elif len(email) < 3:
        email_error = "I'm sorry that email is too short!"
                                                   # Email validation
    elif goodie1 not in email:
        email_error = "Not a valid email"

    elif goodie2 not in email:
        email_error = "Not a valid email"

    elif nono in email:
        email_error = "Please...no spaces in the email address"




    if not user_name_error and not password_error and not password_v_error and not email_error:
        return redirect('/valid-user?username={}'.format(user_name))
    else:                                              #Pass it on through
        return render_template('user-form.html', user_name_error=user_name_error, user_name=user_name,
        password_error=password_error, password=password, password_v_error=password_v_error,
        verify_password=verify_password, email_error=email_error, email = email
        )

@app.route('/valid-user')
def valid_user():
    user = request.args.get('username') #gettin the query string
                                    #somehow it was really impirtant to keep my q var in quotes

    return '<h1> Welcome, {0} ! </h1>'.format(user)
app.run()
