#!/usr/bin/env python3
"""Command-line Expense Tracker with persistent CSV storage."""


def load_expenses():
    """Read saved expenses from the CSV file. (Coming in Step 4)"""
    return []


def save_expenses(expenses):
    """Write expenses to the CSV file. (Coming in Step 4)"""
    pass


def get_total(expenses):
    """Add up the total of all expenses. (Coming in Step 3)"""
    return 0


def add_expense(expenses):
    """Ask the user for an expense and store it. (Coming in Step 3)"""
    print("Not built yet.\n")


def view_expenses(expenses):
    """Display all expenses plus the total. (Coming in Step 3)"""
    print("Not built yet.\n")


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
