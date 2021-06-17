from datetime import datetime

class Account:
    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        self.balance=0
        self.transaction_fee=300
        self.loan_limit=10000
        self.loan=0
        self.loan_fees=0.05
        self.transactions=[]
    
    def deposit(self,amount):
        try:
            amount+10
        except:
            return f'Please enter amount in figures'
        
        if amount<=0:
            return f'Please deposit a valid amount'
        else:
            self.balance +=amount
            transact={"amount":amount,"balance":self.balance,"narration":"You deposited","time":datetime.now()}
            self.transactions.append(transact)
            return f'Hello {self.name} you have deposited {amount} your new balance is {self.balance}'

    def withdraw(self,amount):
        try:
            amount+10
        except:
            return f'Please enter amount in figures'
        transaction=amount+amount*0.05
        if amount<=0:
            return f'Invalid input'

        elif self.balance<=transaction:
            return f'Insufficient balance'

        else:
             self.balance-=transaction
             transact={"amount":amount,"balance":self.balance,"narration":"You withdrew","time":datetime.now()}
             self.transactions.append(transact)
             return f'Transaction successful you have withdrawn {amount} your balance is {self.balance}'

    def borrow(self,amount):
        try:
            amount+10
        except:
            return f'Please enter amount in figures'
        
        total_loan=amount+amount*self.loan_fees
        if amount<=0:
            return f'Invalid input'
        elif total_loan >self.loan_limit:
            return f'{amount} is greater than limit, try a lower amount'
        elif self.loan>0:
            return f'Repay your outstanding loan of {self.loan}'
        else:
            loan=self.balance+amount
            self.loan+=total_loan
            transact={"amount":amount,"balance":self.balance,"narration":"You borrowed","time":datetime.now()}
            self.transactions.append(transact)
            return f'You new balance is {loan}. Repay {total_loan} in 30 days'
    def repay(self,amount):
        try:
            amount+10
        except:
            return f'Please enter amount in figures'
        
        if amount<=0:
            return f'Invalid input'

        elif amount<self.loan:
            diff=self.loan-amount
            self.loan-=amount
            return f'{amount} has been deducted to repay your loan outstanding debt is {diff}'

        else:
            diff=amount-self.loan
            self.balance+=diff
            self.loan=0
            transact={"amount":amount,"balance":self.balance,"narration":"You repayed","time":datetime.now()}
            self.transactions.append(transact)
            return f'Loan has been fully payed. Your new account balance is {self.balance}'
            
    def statement(self):
        for transaction in self.transactions:
            amount=transaction["amount"]
            narration=transaction["narration"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            specific=time.strftime("%-I:%M%p")
            print(f'On {date} at {specific}..{narration}..{amount}..your account balance is {balance}')

    def transfer(self,amount,account): 
        try:
            amount+10
        except:
            return f'Please enter amount in figures'

        fee=amount*0.05
        total=amount+fee

        if amount<=0:
            return f'Invalid input'
            
        elif total>self.balance:
            return f'{self.balance} is not enough to complete the transaction you need {total} in order to transfer {amount}'

        else:
            self.balance-=total
            account.deposit(amount)
            return f'{account.name} will recieve {amount} your new balance is {self.balance}'


class MobileMoneyAccount(Account):
    def __init__(self, name, phoneNumber,service_provider):
        Account.__init__(self,name,phoneNumber)
        self.service_provider=service_provider

    def buy_airtime(self,amount):
        try:
            amount+10
        except:
            return f'Enter number in figures'
        if amount<=0:
            return f'Invalid input'

        elif amount>=self.balance:
            fee=amount*0.001
            total=amount+fee
            return f'Cannot complete the transaction you have insufficient balance'
        else:
            self.balance-=amount
            return f'You have succesfully bought {amount} of airtime your new account balance is {self.balance}'
        