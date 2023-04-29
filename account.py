class Account:


    '''This sets the balance and name'''
    def __init__(self, name):
        self.__name = name
        self.__balance = 0



    '''This will check for the money added and check wether it is a correct amount or not'''
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    '''This checks the money taken out and if it is less than the balance or 0'''
    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    '''this shows the balance of the account'''
    def account_balance(self):
        return self.__balance

    '''this shows the name of the accound'''
    def account_name(self):
        return self.__name
