import pandas as pd
import logging
"""Revisit this class after prototype"""
class DataFrame_Windowed():
	def __init__(self, filePath, colsToKeep=None):
		"""Initialize a windowed dataframe"""
		if colsToKeep:
			if 'Datetime (UTC)' not in colsToKeep:
				colsToKeep.append('Datetime (UTC)')
			self.data = pd.read_csv(filePath, usecols=colsToKeep, parse_dates=['Datetime (UTC)'])
			self.data.set_index('Datetime (UTC)', inplace=True, drop=False)


		else:
			self.data = pd.read_csv(filePath, parse_dates=['Datetime (UTC)']).set_index('Datetime (UTC)', inplace=True, drop=False)
			self.data.set_index('Datetime (UTC)', inplace=True, drop=False)


		self.data = self.data.rename(columns={'Datetime (UTC)': 'Datetime'})
		self.filePath = filePath
		self.startDate_min = self.data['Datetime'].min()
		self.endDate_max = self.data['Datetime'].max()
		self.startDate = self.startDate_min
		self.endDate = self.endDate_max
		self.localTime = False

	
	def RemoveColumn(self, colToDrop):
		if colToDrop == 'Datetime':
			raise Exception('Cannot remove Datetime column from data frame. Required for Time Series.')

		try:
			self.data.drop(colToDrop, inplace=True, axis=1)
		except KeyError:
			print('Column ' + colToDrop + ' not found in dataframe.')


	def AddColumn(self, colToAdd):
		colToAddDF = pd.read_csv(self.filePath, usecols=[colToAdd, 'Datetime (UTC)'])
		self.data[colToAdd] = colToAddDF[colToAdd]

	def UpdateTimeWindows(self, startDate, endDate):
		self.data = self.data.loc[startDate:endDate]

	def Aggregate(self):
		summaryStats = self.data.describe()
		summaryStats = summaryStats[['Acc magnitude avg','Eda avg','Temp avg', 'Movement intensity', 'Steps count','Rest']]
		return summaryStats


