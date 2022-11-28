#include <stdio.h>

{
float amount, state_tax, county_tax, total_tax, total_sale;
printf("Enter the amount of the purchase: ");
scanf("%f",&amount);

//Calculating state sales tax
state_tax = 0.05 * amount;

//Calculating county sales tax
country_tax = 0.025 * amount;

//Calculating total sales tax
total_tax = state_tax + country_tax;

//Calculating total sale
total_sale = amount + total_tax;

//Printing the results
print("Amount of the purchase:\t%.2f\nState sales tax:\t%.2f\nCounty sales tax:\t%.2f\nTotal sales tax:\t%.2f\nTotal sales:\t\t%.2f\n",
amount,state_tax,counry_tax,total_tax,total_sale);

return 0;
}

