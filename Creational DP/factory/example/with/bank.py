class Account:
    def account_details(self):
        raise NotImplementedError("Subclasses should implement this method.")

class SavingsAccount(Account):
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def account_details(self):
        return f"Savings Account for {self.account_holder}"


class CurrentAccount(Account):
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def account_details(self):
        return f"Current Account for {self.account_holder}"


class BusinessAccount(Account):
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def account_details(self):
        return f"Business Account for {self.account_holder}"
