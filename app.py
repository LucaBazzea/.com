from flask import Flask, render_template, request

from mysql.connector import *
from login import user, password # Import login details from git ignored file

app = Flask(__name__)

class Render_site:

   # Renders the websites homepage
   @app.route("/", methods=["GET", "POST"])
   def index():
      return render_template("index.html")
      
   # Fetches data from the contact form and sends user to result.html
   @app.route("/result", methods=["GET", "POST"])
   def contact_form():
      try:
         first_name = request.form.get("fname")
         last_name = request.form.get("lname")
         subject = request.form.get("subject")
         message = request.form.get("message")
         email = request.form.get("email")

         return render_template("result.html", result=f"Hello {first_name, last_name}. {email} Subject: {subject} Message: {message}")
      except Exception as error:
         return render_template("result.html", result=f"Error: {error}")

fname, lname, subject, message, email = Render_site.contact_form()

class Database:

   def update_table(fname, lname, subject, message, email):
      print(f"\nName: {fname}\nSurname: {lname}\nSubject: {subject}\nMessage: {message}\nEmail: {email}\n")

      try:
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

      except Exception as error:
         print(f"Error: {error}")
         

if __name__ == "__main__":
   app.run(debug=True, use_reloader=True)