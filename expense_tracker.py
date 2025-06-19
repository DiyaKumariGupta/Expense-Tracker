import datetime

# Store all expenses in a list
expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.date.today().isoformat()

    category = input("Enter category (e.g., food, rent, travel): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: $"))
    except ValueError:
        print("Invalid amount! Please try again.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("✅ Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return

    total = 0
    print("\nYour Expenses:")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | {exp['description']} | ${exp['amount']:.2f}")
        total += exp['amount']
    print("-" * 50)
    print(f"Total Spent: ${total:.2f}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
