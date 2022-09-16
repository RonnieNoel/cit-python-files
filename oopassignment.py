# Using classes, Create a basic banking application with the following features:

# Create a class called BankAccount with the following attributes:

# account_number - a string
# balance - a float
# owner - a string
# type - a string
# Create a class called Bank with the following attributes:

# name - a string
# accounts - a list of BankAccount objects
# Create a class called Customer with the following attributes:

# name - a string
# accounts - a list of BankAccount objects
# Create a class called Transactions with the following attributes:

#  1. `account` - a `BankAccount` object
#  2. `amount` - a float
#  3. `type` - a string
# The application should have the following functionality:

# Create a new Bank object
# Create a new Customer object
# Create a new BankAccount object
# Add the BankAccount object to the Bank object
# Add the BankAccount object to the Customer object
# Print the Bank object
# Print the Customer object
# Print the BankAccount object
# Create a new Transaction object
# Add the Transaction object to the BankAccount object

class BankAccount:
    def __init__(self,account_number,balance,owner,type ):
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type
    
    def __repr__(self):
        return f"ACCOUNT NO:{self.account_number}, BAL:{ self.balance},OWNER:{self.owner} TYPE:{self.type}"

bnk=BankAccount(1000000,10000,"ronnie","current")
print(bnk)        
class Bank:
    accounts=[]
    def __init__(self,name,accounts):
        self.name=name
        self.accounts=accounts
        
    def __repr__(self):
        return f"ACCOUNT NAME:{self.name}, ACCOUNTS:{ self.accounts}"
        
bank1=Bank("equity",10030492034920)
print(bank1)

class Customer:
    accounts=[]
    def __init__(self,name,accounts):
        self.name=name
        self.accounts=accounts
    
    def __repr__(self):
        return f"NAME:{self.name}, ACCOUNTS:{ self.accounts}"
     
customer1=Customer("ronnie",12324223132)
print(customer1) 
      
class Transactions:
    def __init__(self,account,amount,type):
        self.account=account
        self.amount=amount
        self.type=type
    
    def __repr__(self):
        return f"ACCOUNT:{self.account}, AMOUNT:{ self.amount}, TYPE:{self.type}"
    
tr=Transactions("ronnie",12324223132,"dep")
print(tr) 

