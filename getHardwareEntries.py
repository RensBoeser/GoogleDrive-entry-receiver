from driveAPIHandler import DriveService
import os

def GetEntries():
	# Designate entries file
	dirname  = os.path.dirname
	libpath = dirname(os.path.realpath(__file__)) + '/lib/'
	print(libpath)
	fileId = '1AVZwyLwWoGhELpZ5hwOA3FQ_NxxKq40I4csJ8F4neYs'
	fileType = 'text/csv'
	fileDestination = 'entries.csv'

	# Download file
	service = DriveService(libpath)
	service.GetFile(fileId, fileType, fileDestination)

if __name__ == '__main__': #Debug code
	print('Start debug code')
	GetEntries()