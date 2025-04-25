class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        if not hasattr(account, 'get_balance') or not callable(account.get_balance):
            raise TypeError("Invalid account object provided")
        self.accounts.append(account)

    def get_total_balance(self): 
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return True
        return False

    def is_valid_email(self, email):
        if not isinstance(email, str):
            return False
        return '@' in email and '.' in email

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: Rs. {self.get_total_balance()}"
