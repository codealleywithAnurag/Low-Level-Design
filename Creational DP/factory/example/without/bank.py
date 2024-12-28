class SavingsAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.account_type = "Savings"

    def account_details(self):
        return f"Savings Account for {self.account_holder}"


class CurrentAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.account_type = "Current"

    def account_details(self):
        return f"Current Account for {self.account_holder}"


class BusinessAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.account_type = "Business"

    def account_details(self):
        return f"Business Account for {self.account_holder}"
