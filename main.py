from flask import Flask, render_template
import db

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def Home():
    reviewData = db.GetAllReviews()
    return render_template("index.html", reviews=reviewData)

app.run(debug=True, port=5000)