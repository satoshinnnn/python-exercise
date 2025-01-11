class BankAccount:
    def __init__(self, account_num, account_holder, balance):
        self.account_num = account_num
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,deposit_amount):
        if deposit_amount > 0:
            self.balance = self.balance + deposit_amount
            print(f"Account number '{self.account_num}' deposited {deposit_amount}; current balance is {self.balance}")
        else:
            print(f"Withdraw transaction of account number '{self.account_num}' FAILED ")
    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.balance:
            print( f"Withdraw transaction of account number '{self.account_num}' FAILED ")
        elif withdraw_amount <= 0:
            print( f"Withdraw transaction of account number '{self.account_num}' FAILED ")
        else:
            self.balance = self.balance - withdraw_amount
            print(f"Account number '{self.account_num}' withdrawn {withdraw_amount}; current balance is {self.balance}")

    def get_balance(self):
        return self.balance
    def display_info(self):
        return f"Account Number: {self.account_num}, Holder: {self.account_holder}, Balance: {self.balance:.2f}"

class SavingAccount(BankAccount):
    def __init__(self, account_num, account_holder, balance,interest_rate, time):
        super().__init__(account_num, account_holder, balance)
        self.interest_rate = interest_rate
        self.time = time
    def apply_interest(self):
        self.balance = self.balance * pow(1 + self.interest_rate/100, self.time)
        print(f"Balance of saving account number '{self.account_num}' was staked after {self.time} year is {self.balance}$ ")
        #principle*pow( 1 + rate/100, time)


class Bank:
    def __init__(self):
        self.normal_accounts = []
        self.sav_accounts = []
# Normal Account
    def add_normal_account(self,normal_account):
        self.normal_accounts.append(normal_account)
    def show_infor_of_normal_accounts(self):
        for normal_account in self.normal_accounts:
            print( normal_account.display_info())
# Saving Account
    def add_sav_account(self, sav_account):
        self.sav_accounts.append(sav_account)

    def show_infor_of_sav_accounts(self):
        for sav_account in  self.sav_accounts:
            print(sav_account.display_info())

# Place to create objects for normal account
account1 = BankAccount(101, "Alice", 1000)
account2 = BankAccount(102, "Bob", 900 )
# Place to create objects for saving account
saving1 = SavingAccount(274, "Anni", 500, 5, 3)
saving2 = SavingAccount(333, "Anki", 800, 7, 3)


bank = Bank()
# add các account vào danh sách accounts
bank.add_normal_account(account1)
bank.add_normal_account(account2)

# add các saving account vào danh sách sav_accounts
bank.add_sav_account(saving1)
bank.add_sav_account(saving2)

print("---------------- Normal Accounts Information ----------------")
# Hiển thị thông tin tài khoản normal
bank.show_infor_of_normal_accounts()
print("-------------------------------------------------------------")

print("---------------- Saving Accounts Information ----------------")
# Hiển thị thông tin tài khoản saving
bank.show_infor_of_sav_accounts()
print("-------------------------------------------------------------")

print("---------- Transaction History Of Normal Accounts -----------")
# Lịch sử Nạp/Rút tiền của các tài khoản normal
account1.withdraw(200)
account2.withdraw(10000)  # Số dư không đủ --> print to the console is Transaction FAILED
account2.withdraw(100)
account1.deposit(500)
account1.deposit(500)

print("------------ Balance History Of Saving Accounts ------------")
saving1.apply_interest()
saving2.apply_interest()
