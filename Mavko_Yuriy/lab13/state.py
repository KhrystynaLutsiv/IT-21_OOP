from abc import ABC, abstractmethod
class AccountState(ABC):
    @abstractmethod
    def deposit(self, amount, account):
        pass
    @abstractmethod
    def withdraw(self, amount, account):
        pass

class ActiveState(AccountState):
    def deposit(self, amount, account):
        account.balance += amount
        print(f"Deposited: ${amount}. New balance: ${account.balance}.")
    def withdraw(self, amount, account):
        if amount > account.balance:
            print("Insufficient funds!")
        else:
            account.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${account.balance}.")

class BlockedState(AccountState):
    def deposit(self, amount, account):
        print("Account is blocked. Cannot deposit.")
    def withdraw(self, amount, account):
        print("Account is blocked. Cannot withdraw.")

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.state = ActiveState()
    def deposit(self, amount):
        self.state.deposit(amount, self)
    def withdraw(self, amount):
        self.state.withdraw(amount, self)
    def block_account(self):
        self.state = BlockedState()
        print("Account is now blocked.")
    def activate_account(self):
        self.state = ActiveState()
        print("Account is now active.")


account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.block_account()
account.deposit(50)
account.withdraw(20)
account.activate_account()
account.deposit(30)
account.withdraw(90)
