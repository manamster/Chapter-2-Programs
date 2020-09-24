#Hyder Rizvi and Calvin Comstock-Fisher
#9/24/20
#People We Helped: Nobody
#People that Helped us: Nobody
#Mileage Calculator

#Step 1. Ask what car the the user has?

Car = input("What type of car do you own? ")

#Step 2. Ask how many gallons it can hold

Gallons = float(input("How many gallons of gas can it hold? "))

#Step 3: Ask how far it can travel per mile

Mileage = float(input("How many miles per gallon can it travel? "))

#Step 4: Ask price per gallon

Cost = float(input("What is the cost of a gallon of gas? ")) 

#Step 5: Find price of full tank

Tank = Gallons*Cost

#Step 6: Find distance that it can travel on a full tank

Distance = Mileage*Gallons

#Step 7: Tell user the programs findings

print("The",Car,"can travel",Distance,"miles.")
print("{:}${:,.2f}{:}".format("A full tank would cost ",Tank,"."))