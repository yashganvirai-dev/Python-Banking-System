from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract base class for bank accounts."""

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
        self._transactions = []

    @abstractmethod
    def account_type(self):
        """Return the type of account."""
        pass

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self._balance += amount
        self._transactions.append(f"Deposited: Rs.{amount}")
        print(f"Rs.{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self._balance:
            print("Insufficient balance.")
            return

        self._balance -= amount
        self._transactions.append(f"Withdrawn: Rs.{amount}")
        print(f"Rs.{amount} withdrawn successfully.")

    def show_balance(self):
        print(f"Current Balance: Rs.{self._balance}")

    def show_transactions(self):
        print("\nTransaction History:")
        if not self._transactions:
            print("No transactions yet.")
        else:
            for index, transaction in enumerate(self._transactions, start=1):
                print(f"{index}. {transaction}")


class SavingsAccount(BankAccount):
    """Savings account implementation."""

    def account_type(self):
        return "Savings Account"


class CurrentAccount(BankAccount):
    """Current account implementation."""

    def account_type(self):
        return "Current Account"


class BankingSystem:
    """Manages multiple bank accounts."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, account):
        if account.account_number in self.accounts:
            print("Account number already exists.")
            return

        self.accounts[account.account_number] = account
        print(
            f"{account.account_type()} created successfully "
            f"for {account.account_holder}."
        )

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def show_all_accounts(self):
        print("\nAll Accounts:")
        if not self.accounts:
            print("No accounts available.")
            return

        for account in self.accounts.values():
            print(
                f"Account No: {account.account_number} | "
                f"Holder: {account.account_holder} | "
                f"Type: {account.account_type()}"
            )


def main():
    bank = BankingSystem()

    # Account creation
    account1 = SavingsAccount("1001", "Yash", 5000)
    account2 = CurrentAccount("1002", "Rahul", 10000)

    bank.create_account(account1)
    bank.create_account(account2)

    # Transactions
    print("\n--- Yash's Account ---")
    account1.deposit(2000)
    account1.withdraw(1000)
    account1.show_balance()
    account1.show_transactions()

    print("\n--- Rahul's Account ---")
    account2.deposit(3000)
    account2.withdraw(2500)
    account2.show_balance()
    account2.show_transactions()

    bank.show_all_accounts()


if __name__ == "__main__":
    main()
