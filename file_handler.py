
from models import Transaction

class FileHandler:
    
    def __init__(self,filename):
        self.filename = filename
        
    def save_transactions(self,transactions):
        with open(self.filename, "w") as file:
            for transaction in transactions:
             transaction_line = f"{transaction.id} | {transaction.type} | {transaction.amount} | {transaction.category} | {transaction.description} \n"
             file.write(transaction_line)
            
        
    
    def load_transactions(self):
                try:
                 
                  with open(self.filename, "r") as file:
            
                   transactions = []
                   for transaction_line in file:
                    transaction_line = transaction_line.split("|")
                    id = int(transaction_line[0].strip())
                    amount = float(transaction_line[2].strip())
                    type = transaction_line[1].strip()
                    category = transaction_line[3].strip()
                    description = transaction_line[4].strip()
                    new_transaction = Transaction(id, type, amount, category, description)
                    transactions.append(new_transaction)
                   return transactions
                    
                except FileNotFoundError:
                 print("Error : File doest Exist")
                 return []
                
    
        