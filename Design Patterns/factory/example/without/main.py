from bank import SavingsAccount, CurrentAccount, BusinessAccount

def create_account(account_type, account_holder):
    if account_type == "Savings":
        return SavingsAccount(account_holder)
    elif account_type == "Current":
        return CurrentAccount(account_holder)
    elif account_type == "Business":
        return BusinessAccount(account_holder)
    else:
        raise ValueError("Invalid account type")


def main():
    print("Welcome to the Bank Account Creation System!")

    account_type = input("Enter account type (Savings, Current, Business): ").strip()
    account_holder = input("Enter account holder's name: ").strip()

    try:
        account = create_account(account_type, account_holder)
        
        print(account.account_details())
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
