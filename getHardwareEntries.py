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
	service.GetFile(fileId, fileType, fileDestination)
	result = "{\n\t\"entries\": [\n\t\t"
	with open(fileDestination, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			result += json.dumps(row)
			result += ",\n\t\t"
		result = result[0:len(result)-4] + "\n\t]\n}"

	os.remove(fileDestination)
	return result

if __name__ == '__main__': #Debug code
	print('Start debug code')
	libpath = '../iGEM-RotterdamHR-2018/lib/'
	data = GetHardwareEntries(libpath)
	print(data)
	print(json.loads(data))