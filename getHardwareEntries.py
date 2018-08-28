from driveAPIHandler import DriveService
import os

def GetEntries(libpath):
	# Designate entries file
	fileId = '1AVZwyLwWoGhELpZ5hwOA3FQ_NxxKq40I4csJ8F4neYs'
	fileType = 'text/csv'
	fileDestination = 'entries.csv'

	# Download file
	service = DriveService(libpath)
	service.GetFile(fileId, fileType, fileDestination)

dirname  = os.path.dirname
libpath = dirname(dirname(os.path.realpath(__file__))) + '\\lib\\'

GetEntries(libpath)