class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. New balance is Rs.{self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew Rs.{amount}. New balance is Rs.{self.__balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return self.__balance

account = Account(100) 

account.deposit(50)
account.withdraw(30)
account.withdraw(150)
account.deposit(-20)   
account.withdraw(-10)  

print(f"Current balance: Rs.{account.get_balance()}")
