import pandas as pd

class Data():

	#initialize
	def __init__(self, filePath:str, colsToKeep:list):
		self.data = pd.read_csv(filePath, usecols = colsToKeep)
		#self.fp = ??
		self.filename = filePath

	#function to remove a specified column from the dataframe
	def removeColumn(self, colToDrop:str):
		self.data = pd.drop(colToDrop, axis=1)

	#not sure if the summary df needs to be re-read from memory to add the column or what
	def addColumn(self, colToAdd:str):
		pass

	#function to filter the dataframe for a specified date range - need to make sure the 'date' column name is correct
	def updateTimeWindows(self, startDate:str, endDate: str):
		self.data = data[(data['date'] > startDate) & (data['date'] < endDate)]

	#function to aggregate a column based on another
	def aggregate(self):
		summaryStats = self.data.describe()
		return summaryStats

