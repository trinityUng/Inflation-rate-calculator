##
#author: Trinity Ung
#date: September 26th, 2022
#This program calculate the users inflation rate and notifies them the type of inflation

#variables are declared and gets some of the information needed form the user to start the program
year = (int(input("Please enter the year that you want to calculate the personal interest rate for: ")))
categories = (int(input("Please enter the number of expenditure categories: ")))
interest = 0
arrayPreviousYear = []
arrayCurrentYear = []
totalPrevious = 0.0
totalCurrent = 0.0

#for loop created so that the program can run as many times the user has indicated
for i in range (0, categories):

    #information from user is inputed into a list so that the values are ready to be calculated
    previousYear = (float(input("Please enter expenses for previous year: ")))
    arrayPreviousYear.append(previousYear)
    totalPrevious = totalPrevious + arrayPreviousYear[i]

    currentYear = (float(input("Please enter expenses for year of interest: ")))
    arrayCurrentYear.append(currentYear)
    totalCurrent = totalCurrent + arrayCurrentYear[i]

#calculations for the inflation rate
total = ((totalCurrent - totalPrevious) / totalCurrent) * 100

#this prints out the inflation rate and rounds the total to one decimal point
print("Personal inflation rate for",year,"is %.1f" %total,"%")

#tells the user the type of inflation
if (total < 3):
    print("Type of Inflation: Low")
elif (total >= 3 and total < 5):
    print("Type of Inflation: Moderate")
elif (total >= 5 and total < 10):
    print("Type of Inflation: High")
elif (total >= 10):
    print("Type of Inflation: Hyper")
