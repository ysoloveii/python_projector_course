import math


class Circle:
    """Constructed by a circle radius."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Compute the area of the circle."""
        return math.pi * self.radius**2

    def perimeter(self):
        """Compute the perimeter of the circle."""
        return 2 * math.pi * self.radius


user_circle = Circle(5)
print("Area of the circle:", user_circle.area())
print("Perimeter of the circle:", user_circle.perimeter())


# define empty class Student
class Student:
    pass


# define empty class Marks
class Marks:
    pass


# create some instances of the Student and Marks classes
user_student = Student()
user_marks = Marks()

# check whether the instances are instances of the classes
print(isinstance(user_student, Student))
print(isinstance(user_marks, Marks))

# check whether the said classes are subclasses
# of the built-in object class or not
print(issubclass(Student, object))
print(issubclass(Marks, object))


class Account:
    def __init__(self, balance, account_number):
        """Initializes a new instance of the class with a starting
        balance and an account number."""
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        """Method can be used to create a new account with a zero balance."""
        return cls(0.0, account_number)

    def deposit(self, amount):
        """Allow funds to be added to the account."""
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        """Allow funds to be removed from the account."""
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        """Return the current balance of the account."""
        return self._balance

    def get_account_number(self):
        """Returns the account number."""
        return self._account_number

    def __str__(self):
        """Provides a string representation of the account object,
        including the account number and current balance."""
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        """Adds an interest_rate attribute, which is used
        to calculate the interest on the account balance."""
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        """Calculates the interest and adds it to the account balance
        using the deposit method inherited from the Account class."""
        interest = self._balance * self._interest_rate
        self.deposit(interest)

    def __str__(self):
        return f'Savings account number: {self._account_number}, balance: {self._balance}, interest rate: {self._interest_rate}'


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        """Adds an overdraft_limit attribute, which specifies
        the maximum negative balance that the account can have."""
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Overrides the withdraw method from the Account class to enforce
        the overdraft limit by checking if the requested
        withdrawal would exceed the limit."""
        if self._balance - amount < -self._overdraft_limit:
            raise ValueError('Withdrawal amount exceeds overdraft limit')
        super().withdraw(amount)

    def __str__(self):
        return f'Current account number: {self._account_number}, balance: {self._balance}, overdraft limit: {self._overdraft_limit}'


class Bank:
    def __init__(self):
        # array to store the account objects
        self._accounts = []

    def add_account(self, account):
        # adds a new account to the array
        self._accounts.append(account)

    def remove_account(self, account):
        # removes an account from the array
        self._accounts.remove(account)

    def get_total_balance(self):
        # returns the sum of the balances of all the accounts in the array
        return sum(account.get_balance() for account in self._accounts)

    def update(self):
        """Iterates through each account, updating it in the following ways:
        Savings accounts get interest added;
        CurrentAccounts get a letter sent if they are in overdraft."""
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.get_balance() < 0:
                print(f'Sending overdraft letter for account {account.get_account_number()}')

    def open_account(self, account_type, balance, account_number, *args):
        """Creates a new account object of the specified type
        (Account, SavingsAccount or CurrentAccount) and
        adds it to the accounts array."""
        if account_type == 'Account':
            account = Account(balance, account_number)
        elif account_type == 'SavingsAccount':
            interest_rate = args[0]
            account = SavingsAccount(balance, account_number, interest_rate)
        elif account_type == 'CurrentAccount':
            overdraft_limit = args[0]
            account = CurrentAccount(balance, account_number, overdraft_limit)
        else:
            raise ValueError('Invalid account type')

        self.add_account(account)
        return account

    def close_account(self, account):
        # removes an account from the array
        self.remove_account(account)

    def pay_dividend(self, amount):
        """Calculates the dividend for each account based on its balance
        and the total balance of all accounts,
        and deposits the dividend into the account."""
        total_balance = self.get_total_balance()
        for account in self._accounts:
            dividend = amount * account.get_balance() / total_balance
            account.deposit(dividend)

    def __str__(self):
        return f'Bank with {len(self._accounts)} accounts'


# create a Bank object
bank = Bank()

# create some Account objects and add them to the bank
account1 = Account.create_account('A001')
account1.deposit(1000)
bank.add_account(account1)

account3 = CurrentAccount(2000, 'C001', 1000)
account3.withdraw(1500)
bank.add_account(account3)

# open a new SavingsAccount
savings_account = bank.open_account('SavingsAccount', 1000, 'S001', 0.01)

# pay a dividend into all accounts
bank.pay_dividend(1000)

# print the balances of the account
print(savings_account.get_balance())

# print the total balance of all accounts in the bank
print(f'Total balance: {bank.get_total_balance()}')

# print the number of accounts in the bank
print(f'Number of accounts: {len(bank._accounts)}')
