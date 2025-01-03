from flask import Flask, render_template, request, redirect

import api,api2
app = Flask(__name__)
dbo = Database()



@app.route("/")
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform', methods=['post'])
def perform():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.save(name, email, password)
    if response == 1:
        return render_template('register.html',message="Email already exist")

    else :
        return render_template('login.html',message="Registration Successful, Kindly Login to proceed")


@app.route('/perform_login', methods=['post'])
def logged():
    email= request.form.get("user_entered_email")
    password= request.form.get("user_entered_pass")
    response= dbo.check(email,password)
    if response:
        return redirect("/profile")

    else:
        return render_template('login.html', message="Invalid Email or password")

@app.route("/profile")
def profile():
  return render_template("profile.html")

@app.route("/ner")
def ner():
    return render_template("ner.html")

@app.route("/perform_ner", methods=['post'])
def nert():
    text= request.form.get("ner_text")
    response=api.ner(text)
    print(response)
    return render_template("ner.html",response=response)






@app.route("/sent")
def sent():
    return render_template("sent.html")

@app.route("/perform_sent", methods=['post'])
def senting():
    text= request.form.get("sent_text")
    response=api2.sent(text)
    print(response)

    return render_template("sent.html", response=response)


app.run(debug=True)
