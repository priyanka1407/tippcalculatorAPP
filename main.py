#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill?  $"))
tips = int(input("How much tips would you like to give ? 10, 12, or 15? "))
people_spliting_bill= int(input("How many people to split the bill? "))
tips= tips/100
percent_with_bill=total_bill*tips
bill_with_tips=total_bill+percent_with_bill
total_bill= bill_with_tips/people_spliting_bill
final_amount="{:.2f}".format(total_bill)
print(f"Each person should pay: ${final_amount}")

