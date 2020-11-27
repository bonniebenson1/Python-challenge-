#importing the modules
import os
import csv

#Set file path


##create an object out of the csv file
budget_data = os.path.join('budget_data.csv') 
#  Read input file csv file  
with open(budget_data,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Set variables 
    Monthcount = 0
    total_pl = 0
    pl = []
    monthlist = []
    Monthlychanges= []
    firstpl = 0
    dates = []

    # Read the header row first (skip this step if there is now header)
    header = next(csvreader)
    print(header)

    for row in csvreader:
        Monthcount +=1
        total_pl +=int(row[1])
        pl.append(row[1])
        monthlist.append(row[0])

        #First month P&L value 
        firstpl = int(pl[0])
        dates.append(row[0])

        #This loop creates a list of monthly changes 
    for i in range(1, len(pl)):
        Monthlychanges.append(int(pl[i])-firstpl)
        firstpl = int(pl[i])
        i +=1

    Avgchange = sum(Monthlychanges) /len (Monthlychanges)
    
    greatest_increase = max(Monthlychanges)
    greatest_index = Monthlychanges.index(greatest_increase)
    greatest_date = dates [greatest_index]
    greatest_decrease = min (Monthlychanges)
    worst_index = Monthlychanges.index(greatest_decrease)
    worst_date = dates [worst_index]
# # Read each row of data after the header
#  #   for row in csvreader:
#      print(row) 
#  
# #print(csvreader[0])    for row in csvreader:
#  #       for cell in row:
#             print(cell)
   
# #Go through each row of data after the header & first row 
# for row in csvreader: 
#         #keeping track of the dates 
#         

#         #Calculate the change, then add it to the list of changes 
#         change = int(row[1])-value
#         profits.append(change)
#         value - int(row[1])

#         #total net amount of "profit/losses" over entire period"
#         total_pl = total_pl +int(row [1])

#         #greatest increase in profits 
#         greatest_increase = max(profits)
#        

#         #greatest decrease in profits 
#        

#         #Average change in "profit/losses between months over entire period"
#         avg_change =sum (profits)/len (profits)

        #Displaying information 
    print ("Financial Analysis")
    print ("-------------------------------")
    print (f"Total months: {str (Monthcount)}")
    print (f"total: ${str(total_pl)}")
    print (f"Average Change:${(str(Avgchange))}")
    print (f"Greatest increase in profits: {greatest_date} (${str(greatest_increase)})")
    print (f"Greatest decrease in profit: {worst_date} (${str(greatest_decrease)})")

    # Exporting to .txt file 
    # output = open("analysis.txt")

    # Line1 = "Financial Analysis"
    # Line2 = "_-----------------"
    # Line3 = str(f"Totalmonths: {str(Monthcount)}")
    # Line4 = (f"{str(total_pl)}")
    # Line5 = str(f"Average Change: ${str(round(avg_change,2))}")
    # Line6 = str(f"Greatest increase in profits: {greatest_date} (${greatest_increase)})")
    # Line7 = str(f"Greatest decrease in profits: {worst_date} (${str(greatest_decrease)})")
    # output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.fotmat(line1,line2,line3,line4,line5,line6,line7))



    

