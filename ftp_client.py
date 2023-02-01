# Ref: https://pythonspot.com/ftp-client-in-python/

import ftplib, os, socket
from ftplib import FTP
from colorama import Fore,Style

def run_ftp_client():
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
            ftp.cwd(FTP_DIRECTORY_server)
            ftp.retrbinary(f"RETR {filename}", open(f"{FTP_DIRECTORY_client}/{filename}", 'wb').write)
            return(True)
        except:
            return(False)

    def putFile(ftp, filename):
        try:
            ftp.cwd(FTP_DIRECTORY_client)
            ftp.retrbinary(f"RETR {filename}", open(f"{FTP_DIRECTORY_server}/{filename}", 'wb').write)
            return True
        except:
            return False



    while True:
        try:
            os.system('cls')
            choice = int(input("Welcome to the FTP Client Menu!\n\n1. Download File\n2. Upload File\n" + Fore.RED + "3. Quit" + Style.RESET_ALL + "\n\n>>"))
            if choice == 1:
                #file_download = input("Enter the file name that you want to download: ") <- this is if you want to add in the flexibility of choosing which files you want to download
                file_download = 'ftpServerData-file.txt' 

                if (getFile(ftp,file_download)):
                    os.system('cls')
                    print(f'Successfully Downloaded file: {file_download}\n')
                    input("Enter any key to continue...")
                    break
                else:
                    os.system('cls')
                    print(f'Error in downloading: {file_download}\n')
                    input("Enter any key to continue...")
                    break
            elif choice == 2:
                #file_download = input("Enter the file name that you want to upload: ") <- this is if you want to add in the flexibility of choosing which files you want to upload
                file_upload = 'ftpClientData-file.txt'
                if (putFile(ftp, file_upload)):
                    os.system('cls')
                    print(f'Successfully uploaded file: {file_upload}\n')
                    input("Enter any key to continue...")
                    break
                else:
                    os.system('cls')
                    print(f'Error in uploading: {file_upload}\n')
                    input("Enter any key to continue...")
                    break
            elif choice == 3:
                break
            else:
                print("Please choose from options " + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")

        except ValueError:
            print("Please choose from options " + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")

