from datetime import datetime
from os import name


class Customer:
    def __init__(self, name, dob, email, phone):
        self.name = name
        self.dob = datetime.strptime(dob, "%d/%m/%Y").date()
        self.email = email
        self.phone = phone

    def get_info(self):
        print("Customer name:", self.name)
        print("Date of birth:", self.dob)
        print("Email:", self.email)
        print("Phone:", self.phone)


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = Customer()
        self.balance = balance                      # gọi @balance.setter

    @property
    def account_number(self):
        return self._account_number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print("Account info")
        print("Account number:", self.account_number)
        self.owner.get_info()
        print("Balance:", self.balance, "₫")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(
                "Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005

    def calculate_interest(self):
        return self.balance * self.monthly_interest_rate


acc = Customer("Trường Nguyễn", "07/09/1991", "truongn.nguyen1@onemount.com", "0938338332")

my_account = SavingAccount("1", acc, 1_000_000_000)
my_account.display()
print(my_account.calculate_interest())
