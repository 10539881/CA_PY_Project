import pyodbc
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, json
from werkzeug.security import generate_password_hash, check_password_hash #used to generate the has keyword using SHA256


#setting up the server details.
server = '23.97.146.240' 
database = 'Student'
driver = 'ODBC Driver 17 for SQL Server'
username = 'sa'

#dynamically pulling in the password.
with open(".pw") as f:
    password = f.read()

#creating the Flask app to allow the application to run
def create_app():
    app = Flask(__name__)
    app.secret_key = "1234567890"
    return app

app = create_app()

#creating the connection string to the SQL Server Database
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = connection.cursor() 

# function to login user.
@app.route('/', methods=['GET','POST']) 
def login():
    if request.method == 'POST': # checking if the form method = post, when page first loads this will be false.
        email = request.form['email'] # assigning values from the individual ...
        password = request.form['password'] # elements on the HTML to the variables email & password.
        SQLCommand = ("SELECT * from UserDetails WHERE Email = '" + email + "'") # creating the SQL Statment to return any record that match the email entered by the user.
        cursor.execute(SQLCommand) # execute the above statement.
        results = cursor.fetchall() # assign the returned records (if any) to the results variable.
        if results != []: #checking if there are any records
            for r in results: # looping through the results set.
                if check_password_hash(r.Password, password): #checking if the correct password was supplied, as the password was converted to a SHA256 hash password it must run a...
                    flash("Logged in successfully", category="success") # hash password check to see if it matches.
                    return render_template("profile.html") # if the password is correct, the user is directed to the profile page.
                else:
                    flash("Password is incorrect", category="error") # otherwise a message is displayed indicating an error
                    return redirect(url_for('login')) # and the page is refreshed to allow for a subsequent entry.
        else:
            flash("Email is incorrect, Please try again", category='error') # if the email supplied does not exist in the database a message is displyed to indicate this.
            return redirect(url_for('login'))

    return render_template("login.html")# if the page is being displayed without the form being submitted nothing happens.

#function to register a new user
@app.route('/new_user', methods=['GET','POST']) 
def new_user():
    if request.method=='POST':# checking if the form method = post, when page first loads this will be false.
        name = request.form['name'] # assigning values from the individual ...
        email = request.form['email'] # elements on the HTML to the variables email & password.
        password1 = request.form['password1']
        password2 = request.form['password2']
        if len(name) < 2: # adding some validation, the HTML forces the user to entry some data; however this provides further validation.
            flash("Name must be great than 4 characters", category='error')
        elif len(email) < 4:
            flash("Email must be great than 3 characters", category='error')
        elif password1 != password2: # the user must enter a second password as confirmation, these passwords are compared and if they don't match...
            flash("Passwords don't match", category='error') # a message is displayed to the user.
        elif len(password1) < 8: # password must be at least 8 characters long.
            flash("Password is too short, must contain at least 8 characters", category='error')
        else:
            flash("Account Created!", category='success')
            password=generate_password_hash(password1, method='sha256') # password is converted to a unique string of characters to ensure security. in this function SHA256 is used. 
            SQLCommand = ("INSERT INTO UserDetails (Name, Email, Password) VALUES (?,?,?)") # once all the data has been gathered, a SQL Statment is constructed to add a new record to the database.
            cursor.execute(SQLCommand, name, email, password)# above statement is executed...                cursor.commit()# and committed..
            return redirect(url_for('login'))     
        return redirect(url_for('new_user')) 

    return render_template("register.html")

# function to create a new student
@app.route('/new_student', methods=['GET','POST']) 
def new_student():
    if request.method=='POST': # checking if the form method = post, when page first loads this will be false.
        fname = request.form['fname'] # gathering the data from the HTML form
        lname = request.form['lname']
        dob = request.form['dob']
        country = request.form['country']
        mobile = request.form['mobile']
        email = request.form['email']
        course = request.form['course']
        # check if student already exists
        SQLCommand = ("SELECT * from StudentMaster WHERE Email = '" + email +"'") # SQL Statment is search the database for any records which matches the email address supplied by the user.
        cursor.execute(SQLCommand)
        results = cursor.fetchone()
        if results == None:     # if the email address doesn't already exist the new student can be added.
            SQLCommand = ("INSERT INTO StudentMaster (FirstName, LastName, DOB, Country, Mobile, Email, Course) VALUES (?,?,?,?,?,?,?)") # SQL Statment to create a new record on the StudentMaster table.
            cursor.execute(SQLCommand, fname, lname, dob, country, mobile, email, course)
            cursor.commit()
            flash("Student: " + fname + " " + lname + " has been created", category='success') # message to confirm new record.
        else:
            flash("Student already exists, Please renter details", category='error') # is the email addres already exists on the database, the student cannot be created.
            return redirect(url_for('new_student'))
           
    return render_template("students.html")

# function to find student details in order to update or delete student.
@app.route('/find_student', methods=['GET','POST'])
def find():
    if request.method =='POST':# checking if the form method = post, when page first loads this will be false.
        global globalfindemail # in order to update or delete a record the relevant student's details must be displayed, this global variable will allow the value to be used in multiple functions.
        globalfindemail = request.form['email'] # assigning email from HTML Form.
        action = request.form['action'] # checking if the user pressed the Update or Delete button.
        SQLCommand = ("SELECT * from StudentMaster WHERE Email = '" + globalfindemail + "'") # Running a SQL Statment is pull back any records which equal the email address supplied by the user.
        cursor.execute(SQLCommand)
        results = cursor.fetchall()
        print(action + "this is the button that was pressed")
        if results != []: # if data is returned...
            for r in results: # loop through the records
                content = {'FirstName':r.FirstName, 'LastName':r.LastName, 'DOB':r.DOB, 'Country':r.Country, 'Mobile':r.Mobile, 'Email':r.Email, 'Course':r.Course} # assigning values from the fields to the variables.
                student = json.dumps(content) # converting the list to a string in order to be stored in a JSON file.
                obj = open("static/students.json", "w") # opening the JSON file.
                obj.write(student) # writing out the data.
                obj.close() # closing the file.
            if action == 'Update Student': # if the user wants to update the student...
                return redirect(url_for('updateStudent')) # this function is called
            else:
                return redirect(url_for('deleteStudent')) # otherwise the user wants to delete the student and this function is called.
        else:
            flash("Student doesn't exist, please renter email address", category='error')# lastly the email entered was incorrect and student doesn't exist.
    return render_template('find.html')

# function to update student details
@app.route('/update-Student', methods=['GET','POST'])
def updateStudent():
    if request.method =='POST': # checking if the form method = post, when page first loads this will be false.
        fname = request.form['fname'] # gathering the data from the HTML form
        lname = request.form['lname']
        dob = request.form['dob']
        country = request.form['country']
        mobile = request.form['mobile']
        email = request.form['email']
        course = request.form['course']
        SQLCommand = ("UPDATE StudentMaster SET FirstName=?, LastName=?, DOB=?, Country=?, Mobile=?, Email=?, Course=? WHERE Email = ?") # sql statment to update the student record.
        cursor.execute(SQLCommand, fname,lname,dob,country,mobile,email,course,globalfindemail)  # pulling back any records where the email address matches the global variable captured in the Find() function.
        cursor.commit()
        flash("Student: " + fname + " " + lname + " has been updated", category='success')
        return redirect(url_for('find'))
    return render_template("update.html") 

# function to delete student details.
@app.route('/delete-Student', methods=['GET','POST'])
def deleteStudent():
    if request.method=='POST':
        action = request.form['action'] # checking if the user has clicked the Delete Student button or the Cancel button
        if action == "Delete Student":
            SQLCommand = ("DELETE FROM StudentMaster WHERE Email = ?") # sql statment to delete the student record.
            cursor.execute(SQLCommand, globalfindemail)  
            cursor.commit()
            flash("Student has been deleted", category='success')
            return redirect(url_for('find'))
        else:
            return redirect(url_for('find')) # if the user clicked the Cancel button they are redirected back to the Find screen.
    return render_template("delete.html") 

@app.route('/contact', methods=['GET','POST'])#function to contact us
def contactus():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='443', ssl_context=("../cert.pem","../privkey.pem"))
    
     
    #debug=True - only required in testing environment.


