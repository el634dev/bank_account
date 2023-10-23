# Perform common banking activities and display user info
class BankAccount:
    def __init__(self, full_name, account_number, balance):
        """
        :param full_name: full name of the bank account owner
        :param account_number: randomly generated 8-digit number, unique per account
        :param balance: the balance of money in the account, should start at 0
        """
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit_amount(self, amount):
        """
        :param amount: Number that is deposited
        :return: a string with the amount deposited and the new amount
        """
        new_amount = amount + self.balance
        return f"Amount deposited: ${float(amount)}, new balance: ${float(new_amount)}"

    def withdraw_amount(self, amount):
        """
        :param amount: Number that is deposited
        :return: A string or a string with an overdraft fee of $10
        """
        new_balance = self.balance - amount
        if amount > self.balance:
            amount -= 10
            return "Insufficient funds."
        else:
            return f"Amount withdrawn: ${float(amount)}, your new balance is: ${float(new_balance)}"

    def get_balance(self):
        """
        :return: Print a user-friendly message with the current account balance
        """
        print(f"Balance: ${self.balance}")
        return self.balance

    def add_interest(self, interest):
        """
        :param interest: annual interest rate
        :return: add interest to the users balance
        """
        interest = self.balance * 0.00083
        return f"Your new balance is ${self.balance + interest} after interest"

    def print_statement(self):
        """
        :return: Prints a message with the bank account owner's info
        """
        return f"{self.full_name}\nAccount No.: *****{str(self.account_number)[3:]}\nBalance: ${round(self.balance)}"


# Print Bank Statement
jane_account = BankAccount(full_name="Jane Webster", account_number=3141592, balance=300000)
print(jane_account.print_statement())
print("--------------------------")

# Adding Interest Example
ray_account = BankAccount(full_name="Ray Thompson", account_number=4921736, balance=200000)
print(ray_account.print_statement())
print(ray_account.add_interest(10))
print("--------------------------")

# Withdraw Example
kent_account = BankAccount(full_name="Clark Kent", account_number=9365841, balance=400000)
print(kent_account.print_statement())
print(kent_account.withdraw_amount(150))
