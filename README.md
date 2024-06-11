# database-to-account-for-your-own-finances

A Python program that allows you to fill in a database to track your finances and generate reports with graphs. This program uses the SQLite database and the Matplotlib library for generating graphs.

Here's how the program works:

The program connects to an SQLite database named finances.db.
It creates a table named transactions with columns for date, category, and amount if the table doesn't already exist.
The add_transaction() function prompts the user to enter the date, category, and amount of a transaction, and then inserts the data into the transactions table.
The view_transactions() function retrieves all transactions from the database and displays them.
The generate_report() function calculates the total amount for each category by querying the database. It then uses the Matplotlib library to generate a bar chart displaying the total amount for each category.
The program displays a menu with options to add a transaction, view transactions, generate a report, or exit the program.
When the user selects an option, the corresponding function is called.
The program continues to run until the user chooses to exit.
Finally, the database connection is closed.
To run the program, you'll need to have Python 3 installed along with the Matplotlib library. You can install Matplotlib using pip:

```
pip install matplotlib
```

When you run the program, it will create a new database file named finances.db if it doesn't already exist. You can then add transactions, view them, and generate financial reports with graphs.

Note: This is a basic example, and you may want to add additional features like error handling, data validation, and more advanced reporting options based on your specific requirements.
