#Calvin Comstock-Fisher and Hyder Rizvi
#9/24/20
#People We Helped: Nobody
#People that Helped us: Nobody
#Book Project 3

#Step 1: Find cost of food

bill = float(input("What is the cost for the food you ordered? "))

#Step 2: Find cost of 15% and 20% tips

tip15 = float(bill*.15)
tip20 = float(bill*.20)

#Step 3: Find total cost for 15% and 20% tips

total15 = tip15 + bill
total20 = tip20 + bill

#Step 4: Tell user the programs findings

print("{:}${:,.2f}".format("The cost of the food with a %15 percent tip is ",total15, "."))
print("{:}${:,.2f}".format("The cost of the food with a %20 percent tip is ",total20, "."))