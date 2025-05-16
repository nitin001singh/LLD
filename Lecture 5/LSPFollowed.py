from abc import ABC, abstractmethod
from typing import List

# 1. DepositOnlyAccount interface
class DepositOnlyAccount(ABC):
    @abstractmethod
    def deposit(self, amount: float):
        pass

# 2. WithdrawableAccount interface extends DepositOnlyAccount
class WithdrawableAccount(DepositOnlyAccount):
    @abstractmethod
    def withdraw(self, amount: float):
        pass


class SavingAccount(WithdrawableAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited: {amount} in Savings Account. New Balance: {self.balance}")

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} from Savings Account. New Balance: {self.balance}")
        else:
            print("Insufficient funds in Savings Account!")


class CurrentAccount(WithdrawableAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited: {amount} in Current Account. New Balance: {self.balance}")

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} from Current Account. New Balance: {self.balance}")
        else:
            print("Insufficient funds in Current Account!")


class FixedTermAccount(DepositOnlyAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited: {amount} in Fixed Term Account. New Balance: {self.balance}")


class BankClient:
    def __init__(self,
                 withdrawable_accounts: List[WithdrawableAccount],
                 deposit_only_accounts: List[DepositOnlyAccount]):
        self.withdrawable_accounts = withdrawable_accounts
        self.deposit_only_accounts = deposit_only_accounts

    def process_transactions(self):
        for acc in self.withdrawable_accounts:
            acc.deposit(1000)
            acc.withdraw(500)

        for acc in self.deposit_only_accounts:
            acc.deposit(5000)


if __name__ == "__main__":
    withdrawable_accounts = [SavingAccount(), CurrentAccount()]
    deposit_only_accounts = [FixedTermAccount()]

    client = BankClient(withdrawable_accounts, deposit_only_accounts)
    client.process_transactions()
