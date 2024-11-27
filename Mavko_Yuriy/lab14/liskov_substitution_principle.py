class Transaction:
    def execute(self, amount):
        raise NotImplementedError()

    def get_transaction_type(self):
        raise NotImplementedError()

class Deposit(Transaction):
    def execute(self, amount):
        print(f"The deposit in the amount of {amount} UAH has been successfully completed.")

    def get_transaction_type(self):
        return "Deposit"

class Withdraw(Transaction):
    def execute(self, amount):
        print(f"Withdrawal in the amount of {amount} UAH has been successfully completed.")

    def get_transaction_type(self):
        return "Withdrawal"

def process_transaction(transaction, amount):
    print(f"In progress {transaction.get_transaction_type()}...")
    transaction.execute(amount)

deposit = Deposit()
withdraw = Withdraw()

process_transaction(deposit, 500)

process_transaction(withdraw, 200)
