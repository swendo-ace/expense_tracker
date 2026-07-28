#!/usr/bin/env python3
"""Command-line Expense Tracker with persistent CSV storage."""


def load_expenses():
    """Read saved expenses from the CSV file. (Coming in Step 4)"""
    return []


def save_expenses(expenses):
    """Write expenses to the CSV file. (Coming in Step 4)"""
    pass


def get_total(expenses):
    """Add up the total of all expenses."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def add_expense(expenses):
    """Ask the user for an expense and store it in the list."""
    name = input("What did you spend on? ").strip()
    if not name:
        print("Expense name can't be empty.\n")
        return
    try:
        amount = float(input("How much? "))
    except ValueError:
        print("That's not a valid number. Expense not added.\n")
        return
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print(f"Added: {name} - {amount:.2f}\n")


def view_expenses(expenses):
    """Display all expenses plus the total."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n--- Your Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']:<20} {expense['amount']:>10.2f}")
    print("-" * 33)
    print(f"{'TOTAL':<21} {get_total(expenses):>10.2f}\n")


def edit_expense(expenses):
    """Edit an existing expense. (Coming in Step 5)"""
    print("Not built yet.\n")


def delete_expense(expenses):
    """Delete an expense. (Coming in Step 5)"""
    print("Not built yet.\n")


def main():
    expenses = load_expenses()
    print("=== Expense Tracker ===\n")
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Edit expense")
        print("4. Delete expense")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
