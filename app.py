import pyodbc
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, MetaData, select, or_, and_, insert
from sqlalchemy.sql.operators import notendswith_op
from werkzeug.security import generate_password_hash, check_password_hash

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '24681012141618'
    return app
### three # means these statements were used with sql alchemy but I couldn't get it to work, so once sql server statements are workign you can remove all lines starting with ###

app = create_app()

server = '23.97.146.240' 
database = 'Student'
driver = 'ODBC Driver 17 for SQL Server'
username = 'sa' 


###app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'

###db = SQLAlchemy(app)

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor() 

#with open(".pw") as f:
 #   password = f.read()

###setting up a sql connection
###database_connection = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
###engine = create_engine(database_connection)
###connection = engine.connect()

###metadata = MetaData()


@app.route('/', methods=['GET','POST']) #this is the function to login a user
def login():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form:
            email = request.form['email'] 
            password = request.form['password']
            ###user = Table('UserDetails', metadata, autoload=True, autoload_with=engine)
            ###stmt = select([user])
            ###stmt = stmt.where(and_(user.columns.Email == email, user.columns.Password == password))
            ###result_proxy = connection.execute(stmt).fetchone()
            SQLCommand = ("SELECT * from UserDetails") 
            #SQLCommand = ("SELECT * from UserDetails WHERE Email = '" + email + "'") 
            #Processing Query  
            cursor.execute(SQLCommand)
            results = cursor.fetchall()
            if results != []:
                session['loginsuccess'] = True
                return redirect(url_for('profile'))
            else:
                flash("Email or Password is incorrect, Please try again", category='error')
                return redirect(url_for('login'))

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)



"""
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
                user = Table('UserDetails', metadata, autoload=True, autoload_with=engine)
                stmt = insert(user).values(Name = name, Email = email, Password = password)
                result_proxy = connection.execute(stmt)
            
            return redirect(url_for('login'))

    return render_template("register.html")

@app.route('/new/student', methods=['GET','POST']) #this is the function to create a new student
def new_student():
    if request.method=='POST':
        if "fname" in request.form and "lname" in request.form and "dob" in request.form and "country" in request.form and "mobile" in request.form and "email" in request.form and "course" in request.form:
            fname = request.form['fname']
            lname = request.form['lname']
            dob = request.form['dob']
            country = request.form['country']
            mobile = request.form['mobile']
            email = request.form['email']
            course = request.form['course']
            student = Table('StudentMaster', metadata, autoload=True, autoload_with=engine)
            stmt = insert(student).values(FirstName = fname, LastName = lname, DOB = dob, Country = country, Mobile = mobile, Email = email, Course = course)
            result_proxy = connection.execute(stmt)
            return redirect(url_for('login'))
           
    return render_template("students.html")

@app.route('/new/profile')
def profile():
    if session['loginsuccess']==True:
        return render_template("profile.html")


@app.route('/new/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('login'))

@app.route('/contact', methods=['GET','POST'])
def contactus():
    #session.pop('loginsuccess', None)
    return render_template("contact.html")
"""


    #, host='0.0.0.0', port='8080', ssl_context=("../cert.pem","../privkey.pem")



