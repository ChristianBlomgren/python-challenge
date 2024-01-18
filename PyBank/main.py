#Code for PyBank
import os
import csv

#Set path to dataset
budget_csv = os.path.join("Resources", "budget_data.csv")

#Print title of new document
print("Financial Analysis")
print("------------------")

#Find the total number of months
with open(budget_csv) as csvfile:
    
    #Set csvfile to be read as 'dict'
    csvreader = csv.DictReader(csvfile)
    
    #Create empty list for months
    mdata = {}
    
    #Begin loop to fetch month data
    for row in csvreader:
        
        #Reads over and copies all data past the 'header'
        for header, value in row.items():
            try:
                mdata[header].append(value)
            except KeyError:
                mdata[header] = [value]
                
#Sets the range for the data that the 
#previous loop will copy over    
months = mdata["Date"]

#Print the total months in "Date" column
print("Total Months: " + str(len(months)))

#Find the sum of all values in "Profit/Losses" column
with open(budget_csv) as csvfile:
   
    #Skip the header row
    header = next(csvfile)
    
    #Set the initial total to 0
    total = 0
    
    #Loop through each row in column [1]
    for row in csv.reader(csvfile):
        
        #Add each new value to the total
        total += int(row[1])
        
    #Print the final total
    print("Total: " + "$" + str(total))
    
#Find the average of the changes in "Profit/Losses" column          
with open(budget_csv) as csvfile:
    
    #Set csvfile to be read as 'dict'
    csvreader = csv.DictReader(csvfile)
    
    #Create empty list for change values
    bdata = {}
     
    #Begin loop to convert "Profit/Losses" column into a list
    for row in csvreader:
        
        #Reads over and copies all data past the 'header'
        for header, value in row.items():
            try:
                bdata[header].append(value)
            except KeyError:
                bdata[header] = [value]
                
#Sets the range for the data that the 
#previous loop will copy over    
profitlosses = bdata["Profit/Losses"]

#Creates a new list that populates with the increase/decrease
#in profits for each month over the entire period
#(Successive element difference)
profitlossesdiff = [int(profitlosses[i + 1]) - int(profitlosses[i]) 
                    for i in range(len(profitlosses) - 1)]

#Create function to find the average of the new list
def Average(profitlossesdiff):
    return sum(profitlossesdiff) / len(profitlossesdiff)

#Assign function to variable
average = Average(profitlossesdiff)

#Print average change
print("Average Change: " + "$" + str(round(average, 2)))

#Setting months to match change data list
changemonths = months[1:]

#Finding the max profit and min loss
#and assigning them to variables
profit = (max(profitlossesdiff))
loss =  (min(profitlossesdiff))

#Assigning the index numbers for the max profit and
#min loss to variables
profitindex = profitlossesdiff.index(profit)
lossindex = profitlossesdiff.index(loss)

#Making the index numbers for the max profit and min loss
#months match the "$" value index numbers
maxmonth = changemonths[profitindex]
minmonth = changemonths[lossindex]

#Print results in console
print("Greatest Increase in Profits: " + str(maxmonth) + 
      " (" + "$" + str(profit) + ")")
print("Greatest Decrease in Profits: " + str(minmonth) +
      " (" + "$" + str(loss) + ")")

#Print results in newly created .txt file
import sys
file = open(os.path.join("Analysis", "analysis.txt"), 'w')
sys.stdout = file 
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(len(months)))
print("Total: " + "$" + str(total))
print("Average Change: " + "$" + str(round(average, 2)))
print("Greatest Increase in Profits: " + str(maxmonth) + 
      " (" + "$" + str(profit) + ")")
print("Greatest Decrease in Profits: " + str(minmonth) +
      " (" + "$" + str(loss) + ")")
file.close()
sys.stdout = sys.__stdout__