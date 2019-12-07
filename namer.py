import os
def name():
	
	arr=os.listdir()
	return arr
def writer(arr):
	with open("files_with_namer.txt","w") as txt:
		for line in arr:
			if(line!="namer.py"):
				txt.write("".join(line) + "\n")

writer(name())
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
y=os.getcwd()
#1st authentification
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles 
#authentication.
drive = GoogleDrive(gauth)

file1 = drive.CreateFile()
file1.SetContentFile(os.path.join(y,"files_with_namer.txt"))
file1.Upload()
