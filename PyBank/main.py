'''
Import libraries and Open File
'''
import os
import csv

csvpath = os.path.join("PyBank/Resources","budget_data.csv")

with open(csvpath) as csvfile:
    banks = csv.reader(csvfile, delimiter=',')
    next(banks)
    months = []
    profits = []
    firstProfit = []
    secondProfit = []
    totalDifference = []

    #Save Data to Lists
    for row in banks:
        months.append(row[0])
        profits.append(int(row[1]))
        firstProfit.append(int(row[1]))
        secondProfit.append(int(row[1]))
    
    #Analyze Financial Data 
    TotalMonths = len(months)
    TotalProfits = sum(profits)
    def averageChange():
        del firstProfit[-1]
        del secondProfit[0]
        for rowNumber in range(len(firstProfit)):
            difference = secondProfit[rowNumber] - firstProfit[rowNumber]
            totalDifference.append(difference)
        averageChange = round(sum(totalDifference)/len(firstProfit),2)
        return averageChange
    AverageChange = averageChange()
    GreatestIncrease = 1
    GreatestDecrease = 1

    #Print Financial Analysis Summary Table
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: {TotalProfits}")
    print(f"Average Change: ${AverageChange}")
    print(f"Greatest Increase in Profits: {GreatestIncrease}")
    print(f"Greatest Increase in Profits: {GreatestDecrease}")


