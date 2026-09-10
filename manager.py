from models import Transaction
from file_handler import FileHandler
from exceptions import (InvalidAmountError,
                        InvalidTransactionTypeError,
                        TransactionNotFoundError)

    

class FinanceManager:
    
    def __init__(self):
        self.transactions = []
        self.file_handler = FileHandler("data/transactions.json")
        self.load_transactions()
                
    def add_transaction(self, user_choice, Amount, category, Description):
        
            if user_choice not in ["income","expense"]:
                raise InvalidTransactionTypeError ("Enter a valid transaction type")
            if Amount <= 0:
                raise InvalidAmountError ("Enter Amount between 1 or more")
            if not category.strip():
                raise ValueError ("Enter The valid category")
            if not Description.strip():
                raise ValueError ("Enter valid Description for the transaction")
            
                  
            if self.transactions:
             id = max(transaction.id for transaction in self.transactions)+1
            else:
             id = 1
            transaction = Transaction(id, user_choice, Amount, category, Description)
            self.transactions.append(transaction)
            self.save_transactions()
         
                
    def view_transactions(self):
       if not self.transactions:
           print("No transactions found")
           return
       
       else:
            print("Here are the Current Transactions")    
            for transaction in self.transactions:
             print(f" Id = {transaction.id} \n Type = {transaction.type} \n Amount = {transaction.amount} \n Category = {transaction.category} \n Description = {transaction.description} \n")
     
    def delete_transaction(self):
        
            found = False
            delete_input = int(input("Enter your tranaction iD to delete the transaction: \n"))
            for transaction in self.transactions:
                if delete_input == transaction.id:
                 found = True
                 self.transactions.remove(transaction)
                 self.save_transactions()
                 print("Transaction deleted successfully!")
                 break
            if not found:
                raise TransactionNotFoundError ("No transactions found for this ID")
                     
            
            
    def search_transactions(self):
        search = input("Enter the keyword to search for the specific transactions: \n").lower()
        found = False
        for transaction in self.transactions:
            if search in transaction.type.lower() or search in  transaction.description.lower() or search in transaction.category.lower():
             found = True
             print(transaction)
        if not found:
             print("No transactions Found") 
    
    def get_total_income(self):
        total = 0 
        for transaction in self.transactions:
            if transaction.type == "income":
             total += transaction.amount
        return total
         
        
    def get_total_expenses(self):
        total = 0   
        for transaction in self.transactions:
         if transaction.type == "expense":
            total += transaction.amount
        return total
        
        
    def get_balance(self):
        balance = self.get_total_income() - self.get_total_expenses() 
        return balance


    def get_category_totals(self):
        category_wise_total = {}
        for transaction in self.transactions:
            if transaction.category in category_wise_total:
                category_wise_total[transaction.category] += transaction.amount 
            else :
                 category_wise_total[transaction.category] = transaction.amount   
        return category_wise_total
    
    def save_transactions(self):
        return self.file_handler.save_transactions(self.transactions)
    
    
    def load_transactions(self):
        self.transactions =  self.file_handler.load_transactions()
        return self.transactions
        
    
                  
                 
              


      
    
    
    
    