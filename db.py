import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/review.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllReviews():

    # Connect, query all guesses and then return the data
    db = GetDB()
    reviews = db.execute("SELECT * FROM Reviews").fetchall()
    db.close()
    return reviews