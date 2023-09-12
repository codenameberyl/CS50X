# Finance

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 9 - Finance Problem Set](https://cs50.harvard.edu/x/2023/psets/9/finance/). The C$50 Finance app allows users to manage portfolios of stocks, check real stock prices, buy and sell stocks, and view transaction history.

## Getting Started

1. Log into cs50.dev and open the terminal.
2. Navigate to the appropriate directory using the `cd` command.

## Implementation Details

### Register

1. Implement the registration functionality in the `register` route.
2. Require the user to input a username and password.
3. Check if the username is blank or already exists in the database.
4. Check if the password is blank or the confirmation password doesn't match.
5. Hash the user's password using `generate_password_hash` and insert the user into the `users` table.
6. Create a new template (e.g., `register.html`) similar to `login.html` for the registration form.

### Quote

1. Implement the quote functionality in the `quote` route.
2. Require the user to input a stock symbol.
3. Use the `lookup` function to get the stock's current price.
4. Create a new template (e.g., `quote.html`) for the quote form and another template (e.g., `quoted.html`) to display the quoted price.

### Buy

1. Implement the buying functionality in the `buy` route.
2. Require the user to input a stock symbol and the number of shares to buy.
3. Check if the symbol is valid and the input is a positive integer.
4. Use the `lookup` function to get the stock's current price.
5. Check if the user has enough cash to buy the specified number of shares.
6. Insert a new row into a table to track the purchase.
7. Update the user's cash balance and create a template (e.g., `buy.html`) to display the purchase details.

### Index

1. Implement the `index` route to display the user's portfolio.
2. Use multiple `SELECT` queries to get the user's stock holdings, prices, and cash balance.
3. Calculate the total value of each holding and the overall portfolio value.
4. Create a template (e.g., `index.html`) to display the portfolio table.

### Sell

1. Implement the selling functionality in the `sell` route.
2. Require the user to select a stock symbol and input the number of shares to sell.
3. Check if the symbol is valid and the input is a positive integer.
4. Check if the user owns enough shares to sell.
5. Update the user's cash balance and create a template (e.g., `sell.html`) to display the sale details.

### History

1. Implement the `history` route to display the user's transaction history.
2. Fetch all buy and sell transactions for the user from the database.
3. Create a template (e.g., `history.html`) to display the transaction history table.

## Testing

1. Run the Flask application in the terminal:

   ```bash
   flask run
   ```

2. Open your web browser and navigate to the URL shown in the terminal.

3. Test the registration, quote, buy, index, sell, and history functionalities as described in the problem specifications.

## Personal Touch

Implement at least one personal touch of your choice. This could include features like allowing users to change passwords, adding additional cash to their account, buying/selling shares via the index page, requiring strong passwords, or implementing any other feature you find interesting.