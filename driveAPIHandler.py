import time
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaIoBaseDownload
import io

class DriveService:
	def __init__(self, libpath):
		self._libpath = libpath
		self.Scopes = 'https://www.googleapis.com/auth/drive.file'
		self.Storage = file.Storage(self._libpath + 'googleAPIToken.json')
		self.Credentials = self.Storage.get()

	def GetService(self):
		# Get authorization to the drive API
		if not self.Credentials or self.Credentials.invalid:
				flow = client.flow_from_clientsecrets(self._libpath + 'googleAPICredentials.json', self.Scopes)
				self.Credentials = tools.run_flow(flow, self.Storage)
		
		# Return an authorized service object
		return build('drive', 'v3', http=self.Credentials.authorize(Http()))

	def GetFile(self, fileId, fileType, fileDestination='file.txt'):
		# Get authorized service
		service = self.GetService()

		# Download entries file
		request = service.files().export_media(fileId=fileId, mimeType=fileType)

		# fh stores the downloaded file in memory
		fh = io.BytesIO()
		downloader = MediaIoBaseDownload(fh, request)
		done = False
		start = time.time()
		while done is False:
			status, done = downloader.next_chunk()
		
		# Write file
		with io.open(fileDestination, 'wb') as f:
			fh.seek(0)
			f.write(fh.read())
			end = time.time()
			print("[{0}ms] Download complete | {1}".format(int((end - start) * 1000), fileId))