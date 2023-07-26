import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    holdings = db.execute("""
        SELECT symbol, SUM(shares) AS total_shares, price
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
        """, session["user_id"])
    for holding in holdings:
        symbol = holding["symbol"]
        current_price = lookup(symbol)["price"]
        holding["current_price"] = usd(current_price)  # Format current_price
        holding["total_value"] = usd(holding["total_shares"] * current_price)  # Format total_value
    grand_total = cash + sum(holding["total_shares"] * lookup(holding["symbol"])["price"] for holding in holdings)
    return render_template("index.html", cash=usd(cash), holdings=holdings, grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        # Retrieve user input
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate symbol and shares inputs
        if not symbol or not shares:
            return apology("Symbol and shares cannot be blank.")

        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Shares must be a positive integer.")
        except ValueError:
            return apology("Shares must be a positive integer.")

        # Lookup stock information
        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid symbol.")

        # Calculate total purchase cost
        total_cost = stock["price"] * shares

        # Get user's available cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if not cash:
            return apology("User not found.")

        # Check if user can afford the purchase
        if cash[0]["cash"] < total_cost:
            return apology("Insufficient funds.")

        # Update user's cash balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?",
                   total_cost, session["user_id"])

        # Get the current timestamp
        buy_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert the purchase record into the transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, buy_time, sell_time) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, shares, stock["price"], buy_time, None)

        # Redirect to the home page
        return redirect("/")

    elif request.method == "GET":
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    # Retrieve the transaction history from the database for the current user
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])

    # Render the history.html template and pass the transaction history data
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        quote_info = lookup(symbol)

        if quote_info is None:
            return apology("Invalid symbol", 400)

        return render_template("quoted.html", symbol=symbol, name=quote_info["name"], price=quote_info["price"])


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # Retrieve the form data
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # Perform validation and sign-up logic here
        if password != confirmation:
            return apology("Passwords Do Not Match.", 400)
        if username == '':
            return apology("Invalid Username.", 400)
        if password == '':
            return apology("Invalid Password.", 400)
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Check if any rows are returned
        if len(rows) > 0:
            # Username already exists
            # Handle the case accordingly
            return apology("Username already exists.", 400)

        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                    username, hash)

        # Process successful sign-up
        return "Sign-up successful!"
    if request.method == 'GET':
        return render_template('register.html', error_message=None)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        # Get the symbols of stocks that the user owns
        symbols = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        return render_template("sell.html", symbols=symbols)

    elif request.method == "POST":
        # Retrieve the form data
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Validate the inputs
        if not symbol:
            return apology("Please select a stock", 400)
        if shares <= 0:
            return apology("Please enter a valid number of shares", 400)

        # Check if the user owns the selected stock
        stock_info = db.execute(
            "SELECT SUM(shares) AS total_shares FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        total_shares = stock_info[0]["total_shares"]
        if not total_shares or shares > total_shares:
            return apology("You don't own that many shares of the stock", 400)

        # Get the current price of the stock
        stock = lookup(symbol)
        if not stock:
            return apology("Invalid symbol", 400)
        price = stock["price"]

        # Calculate the transaction value
        value = shares * price

        # Get the original buy_time
        buy_time_row = db.execute(
            "SELECT buy_time FROM transactions WHERE user_id = ? AND symbol = ? AND shares > 0", session["user_id"], symbol)
        buy_time = buy_time_row[0]["buy_time"]

        # Get the current timestamp for the sell_time
        sell_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", value, session["user_id"])

        # Record the transaction with the original buy_time and sell_time
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, buy_time, sell_time) VALUES (?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, -shares, price, buy_time, sell_time)

        # Redirect to the home page
        flash("Shares sold successfully!")
        return redirect("/")