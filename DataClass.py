import pandas as pd
import logging

#Wrapper/decorator class to handle Pandas dataframe 
class DataModel():

	#initialize object;
	#inputs: parameter of filePath which is a path to the related summary CSV, and colsToKeep which is a list of the columns to import from the summary file. 
	#output: none
	def __init__(self, filePath:str, colsToKeep:list, startDate:str, endDate:str):
		self.data = pd.read_csv(filePath, usecols=colsToKeep)
		self.filename = filePath
		self.startDate = startDate
		self.endDate = endDate

	#function to remove a specified column from the dataframe. 
	# inputs: colToDrop which is a string matching the name of the column to be removed from the dataframe
	# outputs: none
	def removeColumn(self, colToDrop:str):
		try:
			self.data = pd.drop(colToDrop, axis=1)
		except KeyError:
			print("Column not found in dataframe.")


	#not sure if the summary df needs to be re-read from memory to add the column or what
	def addColumn(self, colToAdd:str):
		colToAdd = pd.read_csv(self.filePath, usecols=colToAdd)
		self.data[colToAdd] = colToAdd

	#function to filter the dataframe for a specified date range - need to make sure the 'date' column name is correct
	#inputs: startDate and endDate, both strings. These determine the range of dates the observation must fall between to be included
	#outputs: none
	def updateTimeWindows(self, startDate:str, endDate: str):
		self.data = self.data[(self.data['date'] > self.startDate) & (self.data['date'] < self.endDate)]

	#function to aggregate a column based on another
	#inputs: none
	#outputs: table of description stats (mean, median, variance, standard deviation, quartiles)
	def aggregate(self):
		summaryStats = self.data.describe()
		return summaryStats

