import time
from gstswitch import *


audioPort = 3000
videoPort = 4000
composePort = 3500
previewPort = 5000


KEY = '7Y78HUIH786T67H78TY78'


def main():

	server = dbusClass() #initialization of the class server started

	server.authenticate(KEY)

	server.setAudioPort(audioPort)
	server.setComposePort(composePort)
	server.setPreviewPort(previewPort)

	server.setPIPMode(2)

	server.startRecording()
	time.sleep(10)
	server.stopRecording()



main()