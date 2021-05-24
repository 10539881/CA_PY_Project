import pyodbc
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, MetaData, select, or_, and_, insert
from sqlalchemy.sql.operators import notendswith_op
from werkzeug.security import generate_password_hash, check_password_hash

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '24681012141618'
    return app

app = create_app()

server = '23.97.146.240' 
database = 'Student'
driver = 'ODBC Driver 17 for SQL Server'
username = 'sa' 
password='Password888£'


#with open(".pw") as f:
 #   password = f.read()

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor() 

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email'] 
            password = request.form['password']
            SQLCommand = ("SELECT * from UserDetails WHERE Email = '" + email + "' AND Password = '" + password + "'" )
            cursor.execute(SQLCommand)
            results = cursor.fetchall()
            if results != []:
                session['loginsuccess'] = True
                return redirect(url_for('profile'))
            else:
                flash("Email or Password is incorrect, Please try again", category='error')
                return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/new/profile')
def profile():
    if session['loginsuccess']==True:
        return render_template("profile.html")

@app.route('/new_user', methods=['GET','POST']) #this is the function to register a new user
def new_user():
    if request.method=='POST':
            name = request.form['name']
            email = request.form['email']
            password1 = request.form['password1']
            password2 = request.form['password2']

            if len(name) < 2:
                flash("Name must be great than 4 characters", category='error')
            elif len(email) < 4:
                flash("Email must be great than 3 characters", category='error')
            elif password1 != password2:
                flash("Passwords don't match", category='error')            
            elif len(password1) < 8:
                flash("Password is too short, must contain at least 8 characters", category='error')
            else:
                flash("Account Created!", category='success')
                password=generate_password_hash(password1, method='sha256')
                SQLCommand = ("INSERT INTO UserDetails (Name, Email, Password) VALUES (?,?,?)")
                cursor.execute(SQLCommand, name, email, password)
                cursor.commit()

            return redirect(url_for('new_user'))

    return render_template("register.html")

@app.route('/new/student', methods=['GET','POST']) #this is the function to create a new student
def new_student():
    if request.method=='POST':
        if "fname" in request.form and "lname" in request.form and "dob" in request.form and "country" in request.form and "mobile" in request.form and "email" in request.form and "course" in request.form:
            fname = request.form['fname']
            lname = request.form['lname']
            dob = request.form['dob']
            currentdate = datetime.today()
            result = currentdate - dob
            country = request.form['country']
            mobile = request.form['mobile']
            email = request.form['email']
            course = request.form['course']
            # check if student already exists
            SQLCommand = ("SELECT * from StudentMaster WHERE Email = '" + email +"'")
            print(SQLCommand)
            cursor.execute(SQLCommand)
            results = cursor.fetchone()
            print(result)
            if results == None:

                if len(fname) < 2:
                    flash("First Name must be great than 2 characters", category='error')
                elif len(lname) < 2:
                    flash("Last Name must be great than 2 characters", category='error')
                elif dob is None:
                    flash("Date of Birth must be added", category='error')
                elif len(email) < 4:
                    flash("Email must be great than 3 characters", category='error')
               # elif password1 != password2:
                    flash("Passwords don't match", category='error')            
                #elif len(password1) < 8:
                    flash("Password is too short, must contain at least 8 characters", category='error')
                else:
                    flash("Account Created!", category='success')
                   # password=generate_password_hash(password1, method='sha256')
                    SQLCommand = ("INSERT INTO UserDetails (Name, Email, Password) VALUES (?,?,?)")
                   # cursor.execute(SQLCommand, name, email, password)
                    cursor.commit()
                    flash("Student: " + fname + " " + lname + " has been created", category='success')
                    SQLCommand = ("INSERT INTO StudentMaster (FirstName, LastName, DOB, Country, Mobile, Email, Course) VALUES (?,?,?,?,?,?,?)")
                    cursor.execute(SQLCommand, fname, lname, dob, country, mobile, email, course)
                    cursor.commit()
            else:
                flash("Student already exists, Please renter details", category='error')
            return redirect(url_for('new_student'))
           
    return render_template("students.html")


@app.route('/new/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('login'))

@app.route('/contact', methods=['GET','POST'])
def contactus():
    #session.pop('loginsuccess', None)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
 #, host='0.0.0.0', port='8080', ssl_context=("../cert.pem","../privkey.pem")



