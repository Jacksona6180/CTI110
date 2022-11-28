## Ashley Jackson
## M5HW1
## 11/1/2022
## Calculates if user is within budget


amount=int(input("Enter the budget of the month($): "))

choice='Y'

total = 0.0

while (choice=='Y'or choice=='y'):
   
    expenses = float(input('Enter the expenses($): '))
 
    total=total+ expenses
  
    choice = input("Want to add any expenses? enter y for yes or for no: ")
   
print("Monthly income: "+str(amount))

print("Total monthly expenses: "+str(total))

print("Left over amount after expenses: "+str(amount-total))

if total > amount:
   
    print("User is over the budget.")
    
elif total == amount:
    
    print("User budget is enough for expenses.")
    
else:
    print("User is under the budget.")
    
