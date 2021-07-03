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
    GreatestIncrease = max(totalDifference)
    GreatestIncreaseMonth = months[totalDifference.index(GreatestIncrease)+1]
    GreatestDecrease = min(totalDifference)
    GreatestDecreaseMonth = months[totalDifference.index(GreatestDecrease)+1]

    #Print Financial Analysis Summary Table
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: {TotalProfits}")
    print(f"Average Change: ${AverageChange}")
    print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})")
    print(f"Greatest Increase in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})")

'''
Export to Text File
''' 
output_path = os.path.join("PyBank/Analysis","PyBank_Analysis.txt")

with open(output_path, 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Total Months: {TotalMonths}" + "\n")
    text.write(f"Total: {TotalProfits}" + "\n")
    text.write(f"Average Change: ${AverageChange}" + "\n")
    text.write(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})" + "\n")
    text.write(f"Greatest Increase in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})" + "\n")
