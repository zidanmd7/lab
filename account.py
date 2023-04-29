class Account:



    def __init__(self, name: str) -> None:
        """Funtion to set up account object.
        :param name: Account name
        """
        self.__name = name
        self.__balance = 0



    def deposit(self, amount) -> bool:
        """
        Funtion to add money to the account.
        :param amount: Amount to add to balance
        """
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount) -> bool:
        """
        Funtion to withdraw/take out money from the account.
        :param amount: Amount to deduct from total balance
        """
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    def account_balance(self) -> float:
        """
        Funtion to show the total amount of the balance.
        :return: The total balance of the account
        """
        return self.__balance

    def account_name(self) -> str:
        """
        Funtion to show the name of the account holder
        :return: Account name
        """
        return self.__name
