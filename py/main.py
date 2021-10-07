import mysql.connector
from login import user, password # Import login details from .gitignore file
from datetime import date

today = date.today()

db = mysql.connector.connect(
  host = "localhost",
  user = user,
  password = password,
  database = "site"
)

mycursor = db.cursor()

mycursor.execute(f"INSERT INTO contact (fname, lname, subject, msg, email, date) VALUES ({fname}, {lname}, {subject}, {msg}, {email}, {today})") # Insert data from user input
db.commit()