class User:
    def __init__(self, name, email):  #The class constructor
        self.name = name
        self.email = email
        self.account_balance = 0  # Set to 0 as the default value and NOT included in the parameter list, to prevent an opening balance being passed in as an argument when the class is instantiated
    #Defining a deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    #Defining a withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    #Defining a withdrawal method
    def display_balance(self):
        print("Account balance for " + self.name + "is" + str(self.account_balance))
        return self

    #Defining a transfer money method
    def transfer(self, name, amount):
        print(self.name+" transfers "+str(amount)+"to "+name.name)
        self.make_withdrawal(amount)
        name.make_deposit(amount)
        self.display_balance()
        name.display_balance()
        return self





    

amy = User('Amy', 'a@b.com')
ben = User('Ben', 'a@b.com')
carl = User('Carl', 'a@b.com')


amy.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_balance()

ben.make_deposit(300).make_deposit(400).make_withdrawal(100).make_withdrawal(100).display_balance()

carl.make_deposit(300).make_withdrawal(400).make_withdrawal(100).make_withdrawal(100).display_balance()

amy.transfer(carl,100)

print(amy) # Prints the memory location of the object
