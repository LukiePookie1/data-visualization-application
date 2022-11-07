from tkinter import *
import pandas as pd
import sys
from pathlib import Path


#Might be a better way to do this - this was more or less how I was taught
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(path_root)
from Utils.DataFrame_Windowed import DataFrame_Windowed


 #TKinter table frame class
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial',12,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, summaryStats[i][j])
 




#Not sure how exactly this will be pulled in from file manager - so leaving this hard coded for now
data = DataFrame_Windowed('summary.csv',colsToKeep=['Datetime (UTC)', 'Timezone (minutes)', 'Unix Timestamp (UTC)',
       'Acc magnitude avg', 'Eda avg', 'Temp avg', 'Movement intensity',
       'Steps count', 'Rest', 'On Wrist'])

#Get aggregated data frame
summaryStats = data.Aggregate()

#Store columns to access later
dfCols = summaryStats.columns

# find total number of rows and columns in list...will be adding 1 column to the dataset for the stat names
total_rows = summaryStats.shape[0]
total_columns = summaryStats.shape[1]+1

#Convert to appropriate format - add column for the count type names in the 0th column
titles = ['count','mean','std','min','25%','50%','75%','max']
summaryStats.insert(loc= 0, column = 'type', value=titles)

#Convert data to list - easier to import into Tkinter frame
summaryStats = summaryStats.values.tolist()

#Add row for column names in dataset. 1st one must be blank to match style of table
summaryStatsTest = ['']
for col in dfCols:
    summaryStatsTest.append(col)

#Set 1st row to be the column names
summaryStats[0] = summaryStatsTest

# create root window
root = Tk()

#create table
t = Table(root)

#run loop
root.mainloop()
