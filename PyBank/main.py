'''
Import libraries, Open File, and Analysis
'''
# Import Libraries
import os
import csv

# Directory Path to Financial Data
csvpath = os.path.join("PyBank/Resources","budget_data.csv")

# Open File and Create Empty List Variables to Store Data
with open(csvpath) as csvfile:
    banks = csv.reader(csvfile, delimiter=',')
    header = next(banks)
    months = []
    profits = []
    firstProfit = []
    secondProfit = []
    totalDifference = []

    # Save Data to Lists and Format Profits/Losses as Integers
    for row in banks:
        months.append(row[0])
        profits.append(int(row[1]))
        firstProfit.append(int(row[1]))
        secondProfit.append(int(row[1]))

    ### Financial Data Analysis of Total Months, Total Profits, Average Change, and Greatest Increase/Decrease Number and Date Values
    def averageChange():
        """
        Calculate the Average Change of profits/posses over the time periods, using two same length lists with an offset of a month difference and then append the difference to a new list, and then use the new list of differences to calculate the average changes over the time periods
        """
        del firstProfit[-1]
        del secondProfit[0]
        for rowNumber in range(len(firstProfit)):
            difference = secondProfit[rowNumber] - firstProfit[rowNumber]
            totalDifference.append(difference)
        averageChange = round(sum(totalDifference)/len(firstProfit),2)
        return averageChange
    
    TotalMonths = len(months)
    TotalProfits = sum(profits)
    AverageChange = averageChange()
    GreatestIncrease = max(totalDifference)
    GreatestIncreaseMonth = months[totalDifference.index(GreatestIncrease)+1]
    GreatestDecrease = min(totalDifference)
    GreatestDecreaseMonth = months[totalDifference.index(GreatestDecrease)+1]


    ### Print Financial Analysis Summary Table
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
# Directory Path to Output Text File
output_path = os.path.join("PyBank/Analysis","PyBank_Analysis.txt")

# Write Text File 
with open(output_path, 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Total Months: {TotalMonths}" + "\n")
    text.write(f"Total: {TotalProfits}" + "\n")
    text.write(f"Average Change: ${AverageChange}" + "\n")
    text.write(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})" + "\n")
    text.write(f"Greatest Increase in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})" + "\n")
