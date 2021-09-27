class BankAccount:
    def __init__(self, account_number, account_name, balance=-0):
        self._account_number = account_number
        self._account_name = account_name
        self.set_balance(balance)

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance > 0:
            self._balance = new_balance
        else:
            print("Số tiền không hợp lệ")

    def display(self):
        print(self._account_number, self._account_name, self._balance, "₫")

    def get_withdraw(self, amount):
        return self._balance

    def set_withdraw(self, amount):
        # print(self._balance)
        # print(amount)
        if 0 < amount < self._balance:
            self._balance -= amount
        else:
            print("Số dư trong tài khoản không đủ để rút , vui lòng rút ít hơn") 

    def get_deposit(self, amount_deposit):
        return self._balance

    def set_deposit(self, amount_deposit):
        # print(self._balance)
        # print(amount)
        if 0 < amount_deposit:
            self._balance += amount_deposit
        else:
            print("Số tiền cần nạp phải > 0") 

my_account = BankAccount(1, "Truong Nguyen",50)
my_account.set_balance(100_000) #Số tiền có ban đầu
# Bỏ dấu # để thực thi từng function bên dưới
# my_account.set_withdraw(50_000) #Rút tiền
# my_account.set_deposit(500_000) #Nạp tiền
my_account.display()