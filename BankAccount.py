class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance


    def get_account_number(self):
        return self.__account_number


    def set_account_number(self, account_number):
        self.__account_number = account_number


    def get_holder_name(self):
        return self.__holder_name


    def set_holder_name(self, holder_name):
        self.__holder_name = holder_name


    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative!")


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive!")


    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}")


    def display_account_info(self):
        print("\n--- Account Information ---")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__holder_name}")
        print(f"Balance: ₹{self.__balance:.2f}")
