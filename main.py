

def main():

    account = BankAccount("1234567890", "Eluri Hima Bindu", 1000.0)


    account.display_account_info()


    account.deposit(500)


    account.deposit(-100)


    account.withdraw(300)


    account.withdraw(2000)

    account.withdraw(-50)


    account.display_account_info()

if __name__ == "__main__":
    main()
