from driveAPIHandler import DriveService
import os, csv, json

def GetHardwareEntries(libpath):
	# Designate entries file
	print(libpath)
	fileId = '1AVZwyLwWoGhELpZ5hwOA3FQ_NxxKq40I4csJ8F4neYs'
	fileType = 'text/csv'
	fileDestination = 'entries.csv'

	# Download file
	service = DriveService(libpath)
	service.GetFile(fileId, fileType, '../' + fileDestination)
	result = "{\"entries\":[\n"
	with open(fileDestination, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			result += json.dumps(row)
			result += ",\n"
		result = result[0:len(result)-2] + "\n]}"

	os.remove(fileDestination)
	return result

if __name__ == '__main__': #Debug code
	print('Start debug code')
	dirname  = os.path.dirname
	libpath = dirname(os.path.realpath(__file__)) + '/lib/'
	print(GetHardwareEntries(libpath))