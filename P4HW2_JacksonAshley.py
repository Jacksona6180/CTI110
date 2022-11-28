# CTI-110
# P4HW2 - Salary Calculator
# Ashley Jackson
#11.16.2022

numOfEmp = 0               
totalOverTimePay = 0       
totalRegPay = 0            
totalGrossPay = 0         


while True:
    

    name = input("Enter employee's name or \"None\" to terminate: ")
    
   
    if name == "None":
        break
    else:
        
      
        numOfEmp += 1
    
    hours = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What did " + name + "\' pay rate? "))
    
    overtime = 0
    overtimePay = 0
    regularPay = 0
    grossPay = 0
    
    if hours > 40:
        
     
        overtime = hours - 40
        
  
        overtimePay = overtime * rate * 1.5
        
      
        regularPay = 40*rate
        
        grossPay = regularPay + overtimePay
    else:
        
       
        regularPay = hours*rate
        grossPay = regularPay
    

    totalOverTimePay += overtimePay
    
    
    totalRegPay += regularPay
    

    totalGrossPay += grossPay
    

    print("\nEmployee name: " + name + "\n")
    

    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours, rate, overtime, overtimePay, regularPay, grossPay))
    print()

print()
print("Total number of employees entered:", numOfEmp)
print("Total amount payed for over time: $" + '{:.2f}'.format(totalOverTimePay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(totalRegPay))
print("Total amount payed in gross: $" + '{:.2f}'.format(totalGrossPay))
