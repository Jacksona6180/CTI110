#Travel Expense
# 9/21/22
# CTI-110 P1HW2 - Travel Expense
#Jackson Ashley
print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget:"))
destination = input("Enter your travel destination:")
gas= int(input("How much do you think you will spend on gas?"))
accomodation = int(input("Approximately, how much will you need for accomodations?"))
food = int(input("Last, how much do you need for food?"))
total = gas + accomodation + food
balance = budget - total

print("---------Travel Expenses-------")
print("Location:", destination)
print("Initial Budget:",budget)
print("Fuel:",gas)
print("Accomodation:", accomodation)
print("Food:",food)
print("Remaining Balance:",balance) 

