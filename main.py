import mysql.connector
from login import user, password # Import login details from git ignored file
from flask import	Flask, redirect, url_for, render_template, flash, request

app = Flask(__name__)

@app.route("/index", methods=["GET","POST"])
def get_form():

  error = None

  try:
    if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      subject = request.form['subject']
      message = request.form['message']
      email = request.form['email']

    else:
      print("get_form() failed")

  except Exception as e:
    print(e)
    return render_template("index.html", response = error)

fname, lname, subject, message, email = get_form()


print(f"\nName: {fname}\nSurname: {lname}\nSubject: {subject}\nMessage: {message}\nEmail: {email}\n")

db = mysql.connector.connect(
  host = "localhost",
  user = user,
  password = password,
  database = "site"
)

mycursor = db.cursor()

mycursor.execute(f"INSERT INTO contact (fname, lname, subject, msg, email, date) VALUES ('{fname}', '{lname}', '{subject}', '{message}', '{email}', CURRENT_DATE())") # Insert data from user input

db.commit()

print("\nTable updated successfully")

resp = "null"

@app.route("/")
def Response():

  return render_template("index.html", response = resp)