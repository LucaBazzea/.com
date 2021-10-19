import mysql.connector
from login import user, password # Import login details from git ignored file

db = mysql.connector.connect(
  host = "localhost",
  user = user,
  password = password,
  database = "site"
)

mycursor = db.cursor()

mycursor.execute("INSERT INTO contact (fname, lname, subject, msg, email, date) VALUES ('Luca', 'Bazzea', 'Test', 'text', 'luca@email.com', CURRENT_DATE())") # Insert data from user input

db.commit()
print("\nTable updated successfully")