# Personal Finance Manager

A command-line personal finance management application built with Python.

This project was created to practice and demonstrate core Python concepts including **Object-Oriented Programming (OOP), file handling, exception handling, custom exceptions, lists, dictionaries, loops, functions, and JSON data persistence**.

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
* Automatically save transactions to a JSON file
* Automatically load previously saved transactions when the application starts
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
* JSON
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
    └── transactions.json
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
* Saving transactions
* Loading transactions

### `file_handler.py`

Responsible only for reading and writing transaction data.

Transactions are stored in:

```text
data/transactions.json
```

The transaction data is stored as JSON.

Example:

```json
[
    {
        "id": 1,
        "type": "expense",
        "amount": 25.5,
        "category": "food",
        "description": "lunch"
    },
    {
        "id": 2,
        "type": "income",
        "amount": 100000.0,
        "category": "salary",
        "description": "monthly salary"
    }
]
```

### `exceptions.py`

Contains custom exceptions used by the application:

* `InvalidAmountError`
* `InvalidTransactionTypeError`
* `TransactionNotFoundError`

These exceptions allow the application to handle specific application errors separately from Python's built-in exceptions.

## How It Works

When the application starts, the `FinanceManager` loads previously saved transactions from the JSON file.

When a new transaction is added:

1. The user selects `income` or `expense`.
2. The user enters the amount.
3. The user enters a category.
4. The user enters a description.
5. The manager validates the transaction.
6. A unique transaction ID is generated.
7. A `Transaction` object is created.
8. The transaction is added to the list.
9. The updated transaction list is automatically saved to the JSON file.

When a transaction is deleted:

1. The user enters the transaction ID.
2. The manager finds the transaction.
3. The transaction is removed from the list.
4. The updated transaction list is automatically saved to the JSON file.

The user does not need to manually save the application.

## JSON Persistence

The application uses JSON to preserve transaction data between program runs.

When saving:

```text
Transaction objects
        ↓
__dict__
        ↓
Python dictionaries
        ↓
json.dump()
        ↓
transactions.json
```

When loading:

```text
transactions.json
        ↓
json.load()
        ↓
Python dictionaries
        ↓
Transaction objects
        ↓
transactions list
```

This allows the application to close and restart without losing previously saved transactions.

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
9. Exit
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

The transaction is automatically saved to:

```text
data/transactions.json
```

No manual save is required.

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
* Automatically saving newly added transactions
* Automatically saving deleted transactions
* Restarting the application and loading saved transactions
* Generating new transaction IDs after restarting
* Confirming transactions are preserved after restarting
* Confirming deleted transactions remain deleted after restarting

## What I Practiced

This project helped me apply several Python concepts together instead of practicing them individually.

### Python Fundamentals

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

### JSON

* `json.dump()`
* `json.load()`
* Converting objects to dictionaries
* Converting dictionaries back into objects
* JSON data persistence

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
transactions.json
```

## Future Improvements

This is Version 1 of the project.

Possible future improvements include:

* Add stronger data validation
* Add Pydantic models
* Add a database
* Build an API with FastAPI
* Add authentication
* Add monthly and yearly reports
* Add budgeting features
* Add a web or mobile interface
* Add automated tests
* Add AI-powered financial insights

These features are intentionally outside the current scope of Version 1.

## Author

**Harikrishna Indurthi**

Built as a Python learning and portfolio project while progressing toward backend development, APIs, and AI/GenAI application development.
