import os
from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = int(request.form.get("day"))

        # Insert the new birthday into the database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return redirect("/")

    else:
        # Fetch all birthdays from the database
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)

@app.route("/delete/<int:birthday_id>", methods=["POST"])
def delete(birthday_id):
    # Delete the birthday entry with the given ID
    db.execute("DELETE FROM birthdays WHERE id = ?", birthday_id)
    return redirect("/")

if __name__ == "__main__":
    app.run()
