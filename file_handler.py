import json
from models import Transaction

class FileHandler:
    
    def __init__(self,filename):
        self.filename = filename
        
    
    def save_transactions(self,transactions):
        with open(self.filename, "w") as file:
            json.dump([transaction.__dict__ for transaction in transactions],file, indent = 4)
                    
                    
            
        
    
    def load_transactions(self):
         try:
            with open(self.filename, "r") as f:
                transactions = []
                data = json.load(f)
                for transaction in data:
                    new_transaction = Transaction(transaction["id"], transaction["type"], transaction["amount"], transaction["category"], transaction["description"])
                    
                    transactions.append(new_transaction)
            return transactions
         except FileNotFoundError:
                  print("Error : File doest Exist")
                  return []        
                
                 
                  
                    
                 
             
             
                
    
        