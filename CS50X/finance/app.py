import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from datetime import datetime

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
    """Show portfolio of stocks"""

    # session.clear()

    # Get user id
    user_id = session["user_id"]
    # Get data from portfolio table
    portfolio = db.execute(
        "SELECT symbol, shares, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol",
        user_id,
    )
    # Get current cash
    current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    # current_cash = current_cash[0]["cash"]

    grand_total = current_cash

    # Calculate stock value
    for stock in portfolio:
        look_stock = lookup(stock["symbol"])
        stock["name"] = look_stock["name"]
        stock["price"] = look_stock["price"]
        stock["total_value"] = stock["total_shares"] * stock["price"]

        grand_total += stock["total_value"]

    return render_template(
        "index.html",
        portfolio=portfolio,
        current_cash=current_cash,
        grand_total=grand_total,
    )

    # return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # check the method
    if request.method == "POST":
        # for POST method

        # Assign to new variable for the transaction
        user_id = session["user_id"]
        # Check the shares via loolup and return
        symbol_buy = request.form.get("symbol")
        shares_buy = request.form.get("shares")
        look_stock = lookup(symbol_buy)

        time_buy = datetime.now()

        # if blank or symbol does not exists
        if not symbol_buy:
            return apology("Please input the symbol of stock", 400)

        # if the stock does not exists
        elif look_stock == None:
            return apology("There is no this Symbol in the stock", 400)
        # Check shares
        elif not shares_buy:
            return apology("Please input the number of shares", 400)
        elif not shares_buy.isdigit():
            return apology("Please input the number of shares", 400)
        # If shares < 1
        elif int(shares_buy) <= 0:
            return apology("Please input the number of shares", 400)

        price = look_stock["price"]
        total_price = int(shares_buy) * price
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = cash[0]["cash"]
        time = datetime.now()

        # Check enough cash
        if cash < total_price:
            return apology("Not enough cash to buy the stock", 403)
        else:
            # Update user's cash after transaction then add to table
            updated_cash = cash - total_price
            db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)

            # Add transaction data to the transaction table
            db.execute(
                "INSERT INTO transactions (user_id, symbol, shares, price, total_price, time) VALUES (?, ?, ?, ?, ?, ?)",
                user_id,
                symbol_buy,
                shares_buy,
                price,
                total_price,
                time,
            )

            return redirect("/")
            # return render_template("buy.html")

    else:
        return render_template("buy.html")

    # return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    history = db.execute(
        "SELECT symbol, shares, price, time FROM transactions WHERE user_id =?", user_id
    )
    return render_template("history.html", history=history)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    # User reached route via GET
    if request.method == "GET":
        # go to template quote.html
        return render_template("quote.html")

    # User reached route via POST
    else:
        symbol = request.form.get("symbol")
        look_stock = lookup(symbol)
        # if the stock does not exists
        if look_stock == None:
            return apology("There is no this Symbol in the stock")
        # Change format by usd function
        look_stock["price"] = usd(look_stock["price"])
        return render_template("quoted.html", look_stock=look_stock)
    # return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Submit the user's input via POST to /register
    if request.method == "POST":
        # Define Variable to use next
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # The user's input is already exists in database
        # Query database for search username
        check_user = db.execute(
            "SELECT COUNT(*) FROM users WHERE username = ?", username
        )
        check_user2 = check_user[0]["COUNT(*)"]

        # The user's input is blank
        if not username:
            return apology("must provide username", 400)

        # Ensure username is not exists
        elif check_user2 == 1:
            return apology("This username is already exists", 400)

        # Check password and Confirmation
        # The password's input is blanl
        elif not password:
            return apology("must provide password", 400)

        # Check confirmation
        elif not confirmation:
            return apology("must provide confirmation", 400)

        # Check password and comfirmation is the same
        elif password != confirmation:
            return apology("Your password and comfirmation should be the same", 400)

        # Hash the password and store it in to database
        pass_hash = generate_password_hash(password)
        new_user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)", username, pass_hash
        )

        # Query database for new username and login
        new_login = db.execute("SELECT * FROM users WHERE username = ?", username)

        session["user_id"] = new_login[0]["id"]

        # redirect to homepage
        return redirect("/")

    # Submit via other method not 'POST'
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    portfolio = db.execute(
        "SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol",
        user_id,
    )
    # For method GET
    if request.method == "GET":
        # Display form to sell
        return render_template("sell.html", portfolio=portfolio)
    # For method POST
    else:
        # Submit to sell via POST
        # Define variable to use next
        Symbol_sell = request.form.get("symbol")
        Shares_sell = request.form.get("shares")
        look_sell = lookup(Symbol_sell)
        # Check how much shares that user have in account
        SharesTotal = db.execute(
            "SELECT SUM(shares) FROM transactions WHERE user_id = ? AND symbol = ?",
            user_id,
            Symbol_sell,
        )

        # Check for error
        if not Symbol_sell:
            return apology("Choose symbol to sell")
        elif not Shares_sell:
            return apology("Choose how much to sell")
        elif not Shares_sell.isdigit():
            return apology("Choose how much to sell")
        elif int(Shares_sell) <= 0:
            return apology("Choose how much to sell")
        elif look_sell == None:
            return apology("There is no this symbol")
        elif int(Shares_sell) > SharesTotal[0]["SUM(shares)"]:
            return apology("Don't have shares enough to sell")

        # Sell opearation
        user_sell_id = db.execute("SELECT id FROM users WHERE id = ?", user_id)
        stock_sell_name = look_sell["name"]
        stock_sell_price = look_sell["price"]
        total_sell_price = stock_sell_price * int(Shares_sell)
        sell_time = datetime.now()
        Shares_sell = -abs(int(Shares_sell))
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        current_cash = int(user_cash[0]["cash"]) + total_sell_price
        total_sell_price = -abs(total_sell_price)
        # Update the transactions table after selling
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, total_price, time) VALUES(?, ?, ?, ?, ?, ?)",
            user_id,
            Symbol_sell,
            Shares_sell,
            stock_sell_price,
            total_sell_price,
            sell_time,
        )
        # Update the user's cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash, user_id)

        return redirect("/")


# Personal Touch
# Add Cash to user's account
@app.route("/addcash", methods=["GET", "POST"])
@login_required
def addcash():
    """Adding some cash to the user account"""
    user_id = session["user_id"]
    if request.method == "POST":
        # Define Variable
        addcash = request.form.get("addcash")
        # Check error
        if not addcash:
            return apology("How much to add")
        elif not addcash.isdigit():
            return apology("How much to add")
        elif int(addcash) <= 0:
            return apology("How much to add")
        # Get current cash in account
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0][
            "cash"
        ]
        new_cash = current_cash + float(addcash)
        # Update the added cash to user's account
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)
        return redirect("/")
    else:
        return render_template("addcash.html")
