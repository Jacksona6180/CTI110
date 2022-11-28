# A brief description of the project
# Date
# CTI-110 P2HW1 - Travel
#Jackson Ashley

print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget:"))
destination = input("Enter your travel destination:")
gas= int(input("How much do you think you will spend on gas?"))
accomodation = int(input("Approximately, how much will you need for accomodations?"))
food = int(input("Last, how much do you need for food?"))
total = gas + accomodation + food
balance = budget - total
print("---------------Travel Expense---------------")
print(f"{'destination:' : <20}", f"{ destination : <20}")
print(f"{'budget:' : <20}", f"{ '$'+str(float(budget)) : <20}")
print(f"{'gas:' : <20}", f"{'$'+str(float(gas)) : <20}")
print(f"{'accommodation:' : <20}", f"{'$'+str(float(accomodation)) : <20}")
print(f"{'food:' : <20}", f"{'$'+str(float(food)) : <20}")
print("--------------------------------------------")
print(f"{'balance:' : <20}", f"{'$'+str(float(balance)) : <20}")

