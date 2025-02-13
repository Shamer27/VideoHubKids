import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, flash
import db
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    reviewData = db.GetAllReviews()
    return render_template("index.html", reviews=reviewData)

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
            return redirect("/")

            # Success! Let's go to the homepage

       
    return render_template("register.html")


@app.route("/add", methods=["GET","POST"])
def Add():
    addError = None
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
        
        db.AddReview(user_id, reviewTitle, score, gameName, date, reviewText, username)
        return redirect("/")
        
    else:
        addError = "Please fill in all fields"

        # Send the data to add our new guess to the db
    return render_template("add.html")

@app.route("/<int:id>")
def singleReview(id):

 #matching the page route
    reviewData = db.getSingleReview(id)
    if reviewData is None:
        redirect("/")

    return render_template("review.html", review=reviewData)



@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    print(f"Editing review ID: {id}")  # Debugging step 1

    reviewData = db.getSingleReview(id)
    print(f"Review Data: {reviewData}")  # Debugging step 2

    # Check if review exists
    if reviewData is None:
        flash("Review not found.")
        return redirect("/")

    # Check if user is logged in
    if "username" not in session:
        print("Please log in to edit your review.")
        return redirect("/login")


    # Check if user is the owner of the review
    if session['id'] != reviewData["user_id"]:
        print("You can only edit your own reviews.")
        return redirect("/")

    if request.method == "POST":
        reviewTitle = request.form["title"]
        score = request.form["score"]
        gameName = request.form["game"]
        date = request.form["date"]
        reviewText = request.form.get("review")

        # Update the review in the database
        db.UpdateReview(id, reviewTitle, score, gameName, date, reviewText)
        flash("Review updated successfully!")
        return redirect("/userReviews")

    return render_template("edit.html", review=reviewData)


@app.route("/<int:id>/delete", methods=["POST"])
def delete(id):
    reviewData = db.getSingleReview(id)
    if reviewData is None:
        flash("Review not found.")
        return redirect("/")
    
    if "username" not in session:
        flash("Please log in to delete your review.")
        return redirect("/login")
    
    if session["id"] != reviewData["user_id"]:
        flash("You can only delete your own reviews.")
        return redirect("/")
    
    db.DeleteReview(id)
    flash("Review deleted successfully!")
    return redirect("/")

@app.route("/userReviews")
def userReviews():
    if "username" not in session:
        flash("Please log in to view your reviews.")
        return redirect("/login")
    
    userReviews = db.showUserrReviews(session["username"])
    return render_template("userReviews.html", userReviews=userReviews)
app.run(debug=True, port=5000)