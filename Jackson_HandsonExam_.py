amount=float(input("Enter the amount of the purchase: \n"))
#Calculating state sales tax
state_tax = 0.4 * amount

#Calculating county sales tax
county_tax = 0.2 * amount

#Calculating total sales tax
total_tax = state_tax + county_tax

#Calculating total sale
total_sale = amount + total_tax

#Printing the results
print("Amount of the purchase:\t%.2f\nState sales tax:\t%.2f\nCounty sales tax:\t%.2f\nTotal sales tax:\t%.2f\nTotal sales:\t\t%.2f\n"
%(amount,state_tax,county_tax,total_tax,total_sale))
