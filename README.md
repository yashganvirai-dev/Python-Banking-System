# Python Banking System

A simple console-based Banking System developed using Python and Object-Oriented Programming (OOP) concepts.

## Features

- Create bank accounts
- Savings Account and Current Account
- Deposit money
- Withdraw money
- Check current balance
- View transaction history
- Manage multiple accounts
- Input validation
- Clean object-oriented architecture

## OOP Concepts Demonstrated

### 1. Classes and Objects
The project uses classes such as `BankAccount`, `SavingsAccount`, `CurrentAccount`, and `BankingSystem`.

### 2. Constructors
The `__init__()` method initializes account and banking system objects.

### 3. Encapsulation
Sensitive account data such as balance and transaction history is kept in `_balance` and `_transactions`.

### 4. Inheritance
`SavingsAccount` and `CurrentAccount` inherit common functionality from `BankAccount`.

### 5. Polymorphism
Both account classes implement the `account_type()` method differently.

### 6. Abstraction
`BankAccount` is an abstract class using Python's `ABC` and `abstractmethod`.

## Project Structure

```text
Python-Banking-System/
│
├── banking_system.py
├── README.md
└── class_diagram.png
```

## Requirements

- Python 3.x
- No external libraries are required to run the banking application.

## How to Run

Open the project folder in VS Code and run:

```bash
python banking_system.py
```

## Sample Operations

The program demonstrates:

1. Creating Savings and Current accounts
2. Depositing money
3. Withdrawing money
4. Checking balance
5. Viewing transaction history
6. Displaying all accounts

## Class Diagram

See `class_diagram.png` for the architecture of the application.

## Author

Yash Ganvir

## Project Purpose

This project was created to practice Python Object-Oriented Programming concepts and demonstrate how OOP can be applied to a real-world banking use case.
