class BankAccount:

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.customer_name=customer_name

    def deposit(self, amount):
        new_balance=self.balance + amount
        return ("The new balance is:",new_balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.balance - amount
            print("\n You have withdrawn" + str(amount) + "\n Your current balance" + str(amount))

    def check_balance(self):
        new_balance=self.balance
        return ("The Current Balance is:", new_balance)
    
    def customer_details(self):
        print("Customer Name:",self.customer_name)
        print("\n Account Number:", self.account_number)
        print("\n Balance:", self.balance)
        print("\n Date of Opening:", self.date_of_opening)

Customer=BankAccount(234354354, 15000, '10/7/2023', "JEREMY")

Customer.customer_details()

print(Customer.deposit(3000))

Customer.withdraw(9000)

print(Customer.check_balance())