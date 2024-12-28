from account_factory import AccountFactory

def main():
    print("Welcome to the Bank Account Creation System!")

    account_type = input("Enter account type (Savings, Current, Business): ").strip()
    account_holder = input("Enter account holder's name: ").strip()

    try:
        account = AccountFactory.create_account(account_type, account_holder)
        
        print(account.account_details())
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
