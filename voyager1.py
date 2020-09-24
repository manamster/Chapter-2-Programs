#Calvin Comstock-Fisher and Hyder Rivzi
#September 23rd, 2020
#People I Helped: Dr. Miller
#People that helped me: Nobody
#Voyager1 Distance Project

#Step 1. ask for the user to tell you how many days it has been since September 25th 2009
#Step 2. Calculate the time since then
#Step 3. Calculate distance based on time
#Step 4. Calculate Round Trip Time for Radio communication
#Step 5. Print all the data

totalDays = int(input("How many days has it been since Spetember 25th, 2009? "))
beginningDistance = 16637000000
totalHours = totalDays * 24
milesTotal = (totalHours * 38241) + beginningDistance
kmTotal = milesTotal * 1.609344
auTotal = milesTotal / 92955887.6
metersTotal = kmTotal * 1000
roundTripDistance = metersTotal * 2
roundTripTimeSeconds = roundTripDistance / 299792458
roundTripTimeHours = (roundTripTimeSeconds / 60) / 60
print("Voyager 1 is currently", end=" ")
print("{:,.2f}".format(milesTotal), end=" ")
print("miles(", end=" ")
print("{:,.2f}".format(kmTotal), end=" ")
print("km /", end=" ")
print("{:,.2f}".format(auTotal), end=" ")
print("AU) away from Earth. It would take", end=" ")
print("{:,.2f}".format(roundTripTimeHours), end=" ")
print("hours to reach it using radio communication.")