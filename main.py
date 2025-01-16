from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "uReview"  # Set a secret key for session management

@app.route("/")
def Home():
    reviewData = db.GetAllReviews()
    return render_template("index.html", Games=reviewData)


@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Try and add them to the DB
        if db.RegisterUser(username, password):
            # Success! Set the session ID to the new user
            session['user_id'] = username  # Assuming username is unique
            # Let's go to the homepage
            return redirect("/")
        
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def Login():

    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username and id then
            session['id'] = user['id']
            session['username'] = user['username']

            # Send them back to the homepage
            return redirect("/")
        else:
            error = "Invalid username or password"
        
    return render_template("login.html", error=error)

@app.route("/createReview", methods=["GET","POST"])
def createReview():

    # Did they click submit?
    if request.method == "POST":
        user_id = session['id']
        title = request.form['title']
        review = request.form['review']
        date = request.form['date']
        game = request.form['game']
        score = request.form['score']

        # Send the data to add our new guess to the db
        db.AddReview(user_id, date, game, score)

    return render_template("createReview.html")

@app.route("/review", methods=["GET"])
def viewReview():
    return render_template("review.html")

app.run(debug=True, port=5000)