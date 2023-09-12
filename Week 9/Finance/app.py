import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

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
    """Show portfolio of stocks"""

    # Create the transactions table if it doesn't exist
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS "transactions" (
            "id" INTEGER NOT NULL,
            "user_id" INTEGER NOT NULL,
            "symbol" TEXT NOT NULL,
            "shares" INTEGER NOT NULL,
            "price" NUMERIC NOT NULL,
            "transacted" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY("user_id") REFERENCES "users"("id"),
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    """
    )

    rows = db.execute(
        """
        SELECT symbol, SUM(shares) as totalShares
        FROM transactions
        WHERE user_ID =:user_id
        GROUP BY symbol
        HAVING SUM(shares) > 0;
        """,
        user_id=session["user_id"],
    )
    holdings = []
    grand_total = 0
    for row in rows:
        stock = lookup(row["symbol"])
        holdings.append(
            {
                "symbol": stock["symbol"],
                "name": stock["name"],
                "shares": row["totalShares"],
                "price": usd(stock["price"]),
                "total": usd(stock["price"] * row["totalShares"]),
            }
        )
        grand_total += stock["price"] * row["totalShares"]
    rows = db.execute(
        "SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"]
    )
    cash = rows[0]["cash"]
    grand_total += cash

    return render_template(
        "index.html", holdings=holdings, cash=usd(cash), grand_total=usd(grand_total)
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("Ent er a symbol and shares")
        elif not request.form.get("shares").isdigit():
            return apology("invalid number of shares")
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))
        stock = lookup(symbol)
        if not stock:
            return apology("symbol invalid")
        rows = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        cash = rows[0]["cash"]

        updated_cash = cash - shares * stock["price"]
        if updated_cash < 0:
            return apology("Cannot afford this purchase")
        db.execute(
            "UPDATE users SET cash=:updated_cash WHERE id =:id",
            updated_cash=updated_cash,
            id=session["user_id"],
        )
        db.execute(
            """
            INSERT INTO transactions
                (user_id, symbol, shares, price)
            VALUES (:user_id, :symbol, :shares, :price)
            """,
            user_id=session["user_id"],
            symbol=stock["symbol"],
            shares=shares,
            price=stock["price"],
        )
        flash("Bought!")
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute(
        """
        SELECT symbol, shares, price, transacted
        FROM transactions
        WHERE user_id=:user_id
        """,
        user_id=session["user_id"],
    )
    for i in range(len(rows)):
        rows[i]["price"] = usd(rows[i]["price"])
    return render_template("history.html", rows=rows)


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

    # if user reached route via POST
    if request.method == "POST":
        # make sure symbol entered
        if not request.form.get("symbol"):
            return apology("You must enter a symbol")

        # get quote
        stock = lookup(request.form.get("symbol"))
        # check is valid stock name provided
        if stock == None:
            return apology("Stock symbol not valid, please try again")

        # show user quoted
        return render_template("quoted.html", stock=stock)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = :username",
            username=request.form.get("username"),
        )

        # Check if a user with that username already exists
        if len(rows) != 0:
            return apology("username already exists.", 400)

        # Ensure password was submitted and matches the confirmation
        if not request.form.get("password"):
            return apology("must provide password", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("confirmation must match password", 400)

        db.execute(
            "INSERT INTO users (username, hash) VALUES (:username, :hash)",
            username=request.form.get("username"),
            hash=generate_password_hash(request.form.get("password")),
        )
        return render_template("login.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("Enter a symbol and shares")
        elif not request.form.get("shares").isdigit():
            return apology("invalid number of shares")
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        rows = db.execute(
            """
            SELECT symbol, SUM(shares) as totalShares
            FROM transactions
            WHERE user_id=:user_id
            GROUP BY symbol
            HAVING totalShares > 0;
            """,
            user_id=session["user_id"],
        )
        for row in rows:
            if row["symbol"] == symbol:
                if shares > row["totalShares"]:
                    return apology("too many shares")

        rows = db.execute("SELECT cash FROM users WHERE id =:id", id=session["user_id"])
        cash = rows[0]["cash"]

        updated_cash = cash + shares * stock["price"]
        db.execute(
            "UPDATE users SET cash=:updated_cash WHERE id =:id",
            updated_cash=updated_cash,
            id=session["user_id"],
        )
        db.execute(
            """
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (:user_id,:symbol, :shares, :price)""",
            user_id=session["user_id"],
            symbol=stock["symbol"],
            shares=-1 * shares,
            price=stock["price"],
        )
        flash("Sold!")
        return redirect("/")

    else:
        rows = db.execute(
            """
            SELECT symbol
            FROM transactions
            WHERE user_id=:user_id
            GROUP BY symbol
            HAVING SUM(shares) > 0;
        """,
            user_id=session["user_id"],
        )
        return render_template("sell.html", symbols=[row["symbol"] for row in rows])


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def account():
    """Change account settings."""
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # ensure all fields are completed
        if (
            not request.form.get("old_password")
            or not request.form.get("password")
            or not request.form.get("confirm_password")
        ):
            return render_template("account.html")

        # assign to variable for easy handling
        old_password = request.form.get("old_password")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # retrieve user data
        user = db.execute(
            "SELECT * FROM users WHERE id = :user_id", user_id=session["user_id"]
        )

        # ensure new passwords match
        if password != confirm_password:
            return apology("new passwords do not match")

        # commit new password to db
        hash = generate_password_hash(confirm_password)
        db.execute(
            "UPDATE users SET hash = :hash WHERE id = :user_id",
            hash=hash,
            user_id=session["user_id"],
        )
        return render_template("changepasswordsuccess.html", success=1)

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("changepassword.html")
