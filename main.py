from exceptions import TransactionNotFoundError,InvalidAmountError,InvalidTransactionTypeError
from manager import FinanceManager
manager = FinanceManager()


while True:
  try:  
    
    choice = int(input("Choose what you want to do: \n 1. Add Transaction \n 2. View Transactions \n 3. Delete Transactions \n 4. Search Transactions \n 5. Get Total Income \n 6. Get Total Expenses \n 7. Get Balance \n 8. Get Category Totals \n 9.Save Transactions \n10.Exit \n::"))
    
    if choice == 1:
     try:
        user_choice = input("Choose which type of Transaction you would like to Enter(Income/Expense): ").lower()
        Amount = float(input("Enter the Amount: \n"))
        category = input("Enter the category: \n").lower()
        Description = input("Enter the Description: \n").lower()
        manager.add_transaction(user_choice, Amount, category, Description)
        print("Transaction Successfully added")
        
     except InvalidTransactionTypeError as it:
        print(f"Error: {it}")
     except InvalidAmountError as ia:
        print(f"Error: {ia}")
     except ValueError as e:
        print(f"Error: {e}")
        
        
        
    elif choice == 2:    
        manager.view_transactions()
        
        
        
    elif choice == 3:
      try:
        manager.delete_transaction()
        
      except TransactionNotFoundError as T:
        print(f"Error: {T}")
      except ValueError:
        print("Please enter a valid number.")  
      
      
            
        
    elif choice == 4:
        manager.search_transactions()
        
        
         
    elif choice == 5:
        print(manager.get_total_income())
        
           
        
    elif choice == 6:
        print(manager.get_total_expenses())
        
        
        
    elif choice == 7:
        print(manager.get_balance())
        
        
        
    elif choice == 8:
        print(manager.get_category_totals())
        
        
        
    elif choice == 9:
        manager.save_transactions() 
        print("Transactions saved Successfully") 
        
               
    
    elif choice == 10:
        break   
    
    
    elif choice not in range(1, 11):
     print("Enter a valid choice between 1 and 10")
    
  except ValueError:
      print("Enter a valid input between 1 and 10 for choice")                 
        
        
        
        
            














