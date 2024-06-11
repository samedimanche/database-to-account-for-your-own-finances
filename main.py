import sqlite3
import matplotlib
matplotlib.use('TkAgg')  # Set the backend to 'TkAgg' or 'Qt5Agg'
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('finances.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (date TEXT, category TEXT, amount REAL)''')

def add_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))

    c.execute("INSERT INTO transactions VALUES (?, ?, ?)", (date, category, amount))
    conn.commit()
    print("Transaction added successfully.")

def view_transactions():
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()

    if not transactions:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(f"{transaction[0]} | {transaction[1]} | {transaction[2]}")

def generate_report():
    c.execute("SELECT category, SUM(amount) AS total FROM transactions GROUP BY category")
    category_totals = c.fetchall()

    if not category_totals:
        print("No transactions found.")
    else:
        categories = []
        totals = []
        for category, total in category_totals:
            categories.append(category)
            totals.append(total)

        plt.figure(figsize=(8, 6))
        plt.bar(categories, totals)
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.title("Financial Report")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

while True:
    print("\nFinance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
