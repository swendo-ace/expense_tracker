# Expense Tracker

A command-line expense tracker built in Python — add, view, edit and delete
expenses, with everything saved to a CSV file that survives between runs.

## Features
- Interactive menu loop (add / view / edit / delete / quit)
- Running total of all spending
- Persistent storage in `expenses.csv` — open it in Excel or edit it by hand
- Input validation throughout: bad numbers and broken CSV rows are handled
  gracefully instead of crashing

## Getting started
Requires Python 3. No external libraries needed.

    git clone https://github.com/swendo-ace/expense_tracker.git
    cd expense_tracker
    python3 expense_tracker.py

## How it works
Expenses are held as a list of dictionaries with a name and an amount,
written to CSV after every change so nothing is lost even if the program
is interrupted. On startup the file is read back in; malformed rows are
skipped rather than crashing the load.

## Project structure
    expense_tracker.py   # the whole program
    expenses.csv         # your data (created on first run, not tracked by git)

## Author
Ace — Software Engineering @ African Leadership University
