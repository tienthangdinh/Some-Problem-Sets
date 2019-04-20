import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = db.execute("SELECT cash FROM users WHERE id =:user", user = session["user_id"])
    stocks = db.execute("SELECT Symbol, SUM(Shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY Symbol", user_id=session["user_id"])
    quotes = {}
    total = 0
    for stock in stocks:
        quotes[stock["Symbol"]] = lookup(stock["Symbol"])
        total = total + quotes[stock["Symbol"]]["price"] * stock["total_shares"]

    cash_remaining = user[0]["cash"]
    total = total + cash_remaining



    return render_template("index.html", quotes=quotes, stocks=stocks, total= total, cash_remaining=cash_remaining)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            apology("fehlt noch Symbol", 400)
        if not request.form.get("shares"):
            apology("please insert number of share u want to buy")

        try:
            number = int(request.form.get("shares"))
        except:
            return apology("must be a number")

        if number < 0:
            return apology("input positive number")

        try:
            share = lookup(request.form.get("symbol"))
        except:
            return apology("company doesnt exist")

        if share == None:
            return apology("company doesnt exist")

        rows = db.execute("SELECT cash FROM users WHERE id = :user", user=session["user_id"])

        vor = rows[0]["cash"]
        pps = -(share["price"])
        verlust = pps * number

        if vor < verlust:
            apology("oh nooooo nicht genug Geld", 400)

        db.execute("UPDATE users SET cash = cash + :verlust WHERE id = :user", verlust = verlust, user = session["user_id"])
        db.execute("INSERT INTO transactions (user_id, Symbol, Company, Shares, pps, Total) VALUES (:user_id, :symbol, :company, :shares, :pricepershare, :total)",
                    symbol = share["symbol"],
                    company = share["name"],
                    shares = number,
                    pricepershare = pps,
                    total = verlust,
                    user_id = session["user_id"]
                    )

        flash("Successfully bought")
        return redirect(url_for("index"))

    if request.method =="GET":
        return render_template("buy.html")



@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT Symbol, Shares, pps, timestamp FROM transactions WHERE user_id = :user_id ORDER BY timestamp ASC", user_id=session["user_id"])

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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

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
    """Get stock quote."""
    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("quote = none =))))", 400)

        return render_template("quoted.html", quote = quote)

    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("fehlt noch unsername", 400)
        elif not request.form.get("password"):
            return apology("fehlt noch password", 400)
        elif not request.form.get("confirmation") == request.form.get("password"):
            return apology("does not match", 400)

        passwort = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        new_user = db.execute("INSERT INTO users (username, hash) VALUES (:username, :passwort)", username=request.form.get("username"), passwort=passwort)

        if not new_user:
            return apology("something wrong happened", 400)

        session["user_id"] = new_user
        flash("Registered")
        return redirect(url_for("index"))

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        stocks = db.execute("SELECT Symbol, SUM(Shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY Symbol", user_id = session["user_id"])
        return render_template("sell.html", stocks = stocks)

    elif request.method =="POST":
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            apology("there is no such symbol value")

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("not integer")

        if shares < 0:
            return apology("need to be lon hon 0")

        stock = db.execute("SELECT SUM(Shares) as total_shares FROM transactions WHERE user_id = :user_id AND Symbol = :symbol GROUP BY Symbol", user_id = session["user_id"], symbol = request.form.get("symbol"))

        if stock[0]["total_shares"] < shares:
            return apology("Cant sell more than you have")

        addmoney = shares * quote["price"]

        db.execute("UPDATE users SET cash = cash + :addmoney WHERE id = :user_id", addmoney = addmoney, user_id = session["user_id"])
        db.execute("INSERT INTO transactions (user_id, Symbol, Shares, Company, pps, Total) VALUES (:user_id, :Symbol, :Shares, :Company, :pps, :Total)",
                    user_id = session["user_id"],
                    Symbol = quote["symbol"],
                    Shares = -shares,
                    Company = quote["name"],
                    pps = quote["price"],
                    Total = addmoney)

        flash("Sold!")

        return redirect(url_for("index"))










def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
