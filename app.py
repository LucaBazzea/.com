from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
   return render_template("index.html")
   

@app.route("/result", methods=["GET", "POST"])
def result():
   try:
      first_name = request.form.get("fname")
      last_name = request.form.get("lname")
      subject = request.form.get("subject")
      message = request.form.get("message")
      email = request.form.get("email")

      return render_template("result.html", result=f"Hello {first_name, last_name}. {email} Subject: {subject} Message: {message}")
   except Exception as error:
      return render_template("result.html", result=f"Error: {error}")


if __name__ == "__main__":
   app.run(debug=True, use_reloader=True)