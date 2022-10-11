import pandas as pd
import logging

class DataFrame_Windowed():
	def __init__(self, filePath, colsToKeep, startDate, endDate):

		if 'Datetime (UTC)' not in colsToKeep:
			colsToKeep.append('Datetime (UTC)')

		self.data = pd.read_csv(filePath, usecols=colsToKeep, parse_dates=['Datetime (UTC)'], index_col='Datetime (UTC)')

		self.data.rename(columns={'Datetime (UTC)': 'Datetime'})
		self.updateTimeWindows(startDate, endDate)

		self.filePath = filePath
		self.startDate = startDate
		self.endDate = endDate
		self.localTime = False

	
	def removeColumn(self, colToDrop):
		try:
			self.data.drop(colToDrop, axis=1)
		except KeyError:
			print('Column ' + colToDrop + ' not found in dataframe.')


	def addColumn(self, colToAdd):
		colToAddDF = pd.read_csv(self.filePath, usecols=[colToAdd, 'date'])


		self.data[colToAdd] = colToAddDF[colToAdd]

	def updateTimeWindows(self, startDate, endDate):
		self.data = data.loc[startDate:endDate]

	def aggregate(self):
		summaryStats = self.data.describe()
		return summaryStats

