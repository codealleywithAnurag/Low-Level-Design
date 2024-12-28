from bank import SavingsAccount, CurrentAccount, BusinessAccount

class AccountFactory:
    @staticmethod
    def create_account(account_type, account_holder):
        if account_type == "Savings":
            return SavingsAccount(account_holder)
        elif account_type == "Current":
            return CurrentAccount(account_holder)
        elif account_type == "Business":
            return BusinessAccount(account_holder)
        else:
            raise ValueError("Invalid account type")
