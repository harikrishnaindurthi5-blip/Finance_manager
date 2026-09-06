# Personal Finance Manager

A command-line personal finance management application built with Python.

This project was created to practice and demonstrate core Python concepts including **Object-Oriented Programming (OOP), file handling, exception handling, custom exceptions, lists, dictionaries, loops, functions, and basic data persistence**.

## Features

* Add income and expense transactions
* Automatically generate transaction IDs
* View all saved transactions
* Delete transactions by ID
* Search transactions by:

  * Transaction type
  * Category
  * Description
* Calculate total income
* Calculate total expenses
* Calculate current balance
* Calculate totals by category
* Save transactions to a text file
* Load previously saved transactions when the application starts
* Validate transaction types and amounts
* Handle invalid user input
* Handle missing transaction IDs with custom exceptions
* Preserve transaction data between program runs

## Technologies Used

* Python 3
* Object-Oriented Programming
* Lists
* Dictionaries
* Functions
* File Handling
* Exception Handling
* Custom Exceptions

## Project Structure

```text
personal_finance_manager/
│
├── main.py
├── models.py
├── manager.py
├── file_handler.py
├── exceptions.py
├── README.md
├── .gitignore
│
└── data/
    └── transactions.txt
```

## File Responsibilities

### `main.py`

Contains the command-line interface and main program loop.

It is responsible for:

* Displaying the menu
* Getting input from the user
* Calling the appropriate `FinanceManager` methods
* Handling user input errors
* Displaying success and error messages

### `models.py`

Contains the application's data model.

The `Transaction` class represents an individual financial transaction.

Each transaction contains:

* ID
* Type
* Amount
* Category
* Description

### `manager.py`

Contains the main business logic of the application.

The `FinanceManager` class handles:

* Adding transactions
* Viewing transactions
* Deleting transactions
* Searching transactions
* Calculating income
* Calculating expenses
* Calculating balance
* Calculating category totals
* Saving and loading transactions

### `file_handler.py`

Responsible only for reading and writing transaction data.

Transactions are stored in:

```text
data/transactions.txt
```

The file uses the following format:

```text
ID | Type | Amount | Category | Description
```

Example:

```text
1 | expense | 25.5 | Food | Lunch
2 | income | 100000.0 | Salary | Monthly salary
```

### `exceptions.py`

Contains custom exceptions used by the application:

* `InvalidAmountError`
* `InvalidTransactionTypeError`
* `TransactionNotFoundError`

These exceptions allow the application to handle specific application errors separately from Python's built-in exceptions.

## How It Works

When the application starts, the `FinanceManager` loads previously saved transactions from the data file.

When a new transaction is added:

1. The user selects `income` or `expense`.
2. The user enters the amount.
3. The user enters a category.
4. The user enters a description.
5. The manager validates the transaction.
6. A unique transaction ID is generated.
7. A `Transaction` object is created.
8. The transaction is added to the list.

When the user saves:

1. The current transaction list is passed to `FileHandler`.
2. The existing file is opened in write mode.
3. The current transactions are written back to the file.
4. The latest application state is therefore persisted.

## Transaction IDs

Transaction IDs start at `1`.

New IDs are generated using the highest existing ID plus `1`.

For example:

```text
1
2
3
```

If transaction `2` is deleted, the next transaction will receive:

```text
4
```

The application does not reuse deleted IDs.

This keeps transaction IDs unique across program restarts.

## Error Handling

The application handles both built-in and custom exceptions.

### Invalid transaction type

Only these transaction types are accepted:

```text
income
expense
```

Anything else raises:

```python
InvalidTransactionTypeError
```

### Invalid amount

Amounts must be greater than zero.

For example:

```text
0
-50
```

raise:

```python
InvalidAmountError
```

### Invalid numeric input

If the user enters text where a number is expected, Python's built-in:

```python
ValueError
```

is handled by the application.

### Transaction not found

If the user attempts to delete a transaction ID that does not exist, the application raises:

```python
TransactionNotFoundError
```

## Running the Application

Make sure Python is installed.

From the project directory, run:

```bash
python main.py
```

The application will display a menu:

```text
1. Add Transaction
2. View Transactions
3. Delete Transactions
4. Search Transactions
5. Get Total Income
6. Get Total Expenses
7. Get Balance
8. Get Category Totals
9. Save Transactions
10. Exit
```

## Example

Adding an expense:

```text
Choose what you want to do:
1. Add Transaction
2. View Transactions
...

::1

Choose which type of Transaction you would like to Enter(Income/Expense):
expense

Enter the Amount:
25.50

Enter the category:
Food

Enter the Description:
Lunch

Transaction Successfully added
```

The transaction is stored in memory and can then be saved to:

```text
data/transactions.txt
```

## Testing

The application was manually tested for:

* Adding income
* Adding expenses
* Invalid transaction types
* Zero amounts
* Negative amounts
* Non-numeric amounts
* Empty categories
* Empty descriptions
* Searching existing transactions
* Searching for nonexistent transactions
* Calculating income
* Calculating expenses
* Calculating balance
* Calculating category totals
* Deleting existing transactions
* Deleting nonexistent transactions
* Invalid transaction IDs
* Saving transactions
* Saving multiple times without creating duplicates
* Restarting the application and loading saved transactions
* Deleting a transaction, saving, restarting, and verifying that the deletion persisted
* Generating new transaction IDs after restarting the application

## What I Practiced

This project helped me apply several Python concepts together instead of practicing them individually.

### Python fundamentals

* Variables
* Strings
* Numbers
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions

### Object-Oriented Programming

* Classes
* Objects
* `__init__`
* `self`
* Methods
* Object composition

### File Handling

* `open()`
* Reading files
* Writing files
* `with open(...)`
* File modes
* Saving and loading application data

### Error Handling

* `try`
* `except`
* `ValueError`
* `FileNotFoundError`
* Custom exceptions
* `raise`

### Application Structure

The project also introduced separating responsibilities between different modules:

```text
User Interface
      ↓
Finance Manager
      ↓
Transaction Model
      ↓
File Handler
      ↓
transactions.txt
```

## Future Improvements

This is Version 1 of the project.

Possible future improvements include:

* Replace text-file storage with JSON
* Add stronger data validation
* Add Pydantic models
* Add a database
* Build an API with FastAPI
* Add authentication
* Add monthly and yearly reports
* Add budgeting features
* Add a web or mobile interface
* Add automated tests

These features are intentionally outside the scope of Version 1.

## Author ---- Harikrishna Indurthi

Built as a Python learning and portfolio project while progressing toward backend development, APIs, and AI/GenAI application development.
