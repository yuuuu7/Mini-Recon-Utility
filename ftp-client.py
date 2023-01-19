# Ref: https://pythonspot.com/ftp-client-in-python/

import ftplib, os, socket
from ftplib import FTP

ftp = ftplib.FTP()
ftp.connect('localhost', 2121)
ftp.login()

FTP_PORT = 2121
FTP_DIRECTORY_server = "./ftpServerData"
FTP_DIRECTORY_client = './ftpClientData'
FTP_ADDRESS = socket.gethostbyname(socket.gethostname())

# Download file from folder defined in ftp-server.py
def getFile(ftp, filename):
  try:
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    return(True)
  except:
    return(False)

def putFile(ftp, filepath):

  # Open the file to be uploaded in binary mode
  with open(filepath, 'rb') as file:
      ftp.storbinary(f'STOR {filepath}', file)
  




while True:
    os.system('cls')
    choice = int(input("\n1. Download File\n2. Upload File\n\n>>"))
    if choice == 1:
        file_download = 'ftpServerData-file.txt' # you should specify your own file
        if (getFile(ftp,file_download)):
            os.system('cls')
            print(f'Downloaded file: {file_download}\n')
            break
        else:
            os.system('cls')
            print(f'Error in downloading: {file_download}\n')
            break
    elif choice == 2:
        file_upload = 'ftpClientData-file.txt'
        if (putFile(ftp, file_upload)):
            os.system('cls')
            print(f'Successfully uploaded file: {file_upload}\n')
            break
        else:
            os.system('cls')
            print(f'Error in uploading: {file_upload}\n')
            break
