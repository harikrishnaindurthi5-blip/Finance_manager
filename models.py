class Transaction:

    def __init__(self, id, type, amount, category, description):
        self.id = id
        self.type = type
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, Amount: {self.amount}, Category: {self.category}, Description: {self.description}"

    def display(self):
        print(self)
        
    
   




 
    