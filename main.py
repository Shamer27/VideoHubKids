from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    guessData = db.GetAllReviews()
    return render_template("index.html", guesses=guessData)

@app.route("/login", methods=["GET", "POST"])
def Login():
    
    # They sent us data, get the username and password
    # then check if their details are correct.
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username then
            session['username'] = user['username']
            session['id'] = user['id']
            return redirect("/");
            # Send them back to the homepage
        else:
            error = "Invalid username or password"


    return render_template("login.html", error=error)

@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Try and add them to the DB
        if db.RegisterUser(username, password):
            user = db.CheckLogin(username, password)
            session['username'] = user['username']
            session['id'] = user['id']
            return redirect("/");

            # Success! Let's go to the homepage

       
    return render_template("register.html")


@app.route("/add", methods=["GET","POST"])
def Add():

    if session.get('username') == None:
        return redirect("/")
    # Did they click submit?
    if request.method == "POST":
        user_id = session['id']
        username = session['username']
        date = request.form['date']
        gameName = request.form['game']
        score = request.form['score']
        reviewText = request.form.get('review')
        reviewTitle = request.form['title']
        

        # Send the data to add our new guess to the db
        db.AddReview(user_id, reviewTitle, score, gameName, date, reviewText, username)
        return redirect("/");

    return render_template("add.html")


app.run(debug=True, port=5000)
