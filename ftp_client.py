# Ref: https://pythonspot.com/ftp-client-in-python/

import ftplib, os
from ftplib import FTP
from colorama import Fore,Style

def run_ftp_client():
    ftp = ftplib.FTP()
    ftp.connect('localhost', 2121)
    ftp.login()

    FTP_DIRECTORY_server = "./ftpServerData"
    FTP_DIRECTORY_client = './ftpClientData'

    # Download file from folder defined in ftp-server.py
    def getFile(ftp, file_from_user):

        file_names = [file for file in os.listdir(FTP_DIRECTORY_server) if file.startswith(file_from_user)]
        if not file_names:
            os.system('cls')
            print(f"\nFile '{file_from_user}' does not exist on the FTP server\n")
            input("Press Enter to continue...")
            return False
        elif len(file_names) > 1:
            os.system('cls')
            print(Fore.RED + "Multiple " + Style.RESET_ALL + "files starting with '" + Fore.GREEN +  f"{file_from_user}" + Style.RESET_ALL + "' found on the FTP server:\n")
            for index, file_name in enumerate(file_names):
                print(f"{index + 1}. {file_name}")
            while True:
                try:
                    file_download = int(input("\nEnter the number of the file you want to download: "))
                    if file_download == 0:
                        break
                    else:
                        file_download = file_names[int(file_download) - 1]
                        file_from_user = file_download
                        break
                except KeyboardInterrupt:
                    os.system('cls')
                    print(Fore.RED + 'Exited' + Style.RESET_ALL)
                    exit()
                except:
                    print(f"\nEnter Integer values from 1 - {index+1} only!")
        else:
            file_download = file_names[0]
            file_from_user = file_download


        ftp.retrbinary(f"RETR {file_from_user}", open(f"{FTP_DIRECTORY_client}/{file_from_user}", 'wb').write)
        os.system('cls')
        print(f'Successfully Downloaded file: {file_from_user}\n')
        input("Press Enter to continue...")
        return True


    def putFile(ftp, file_from_user):

        file_names = [file for file in os.listdir(FTP_DIRECTORY_client) if file.startswith(file_from_user)]
        if not file_names:
            os.system('cls')
            print(f"\nFile '{file_from_user}' does not exist on the FTP server\n")
            input("Press Enter to continue...")
            return False
        elif len(file_names) > 1:
            os.system('cls')
            print(Fore.RED + "Multiple " + Style.RESET_ALL + "files starting with '" + Fore.GREEN +  f"{file_from_user}" + Style.RESET_ALL + "' found on the FTP server:\n")
            for index, file_name in enumerate(file_names):
                print(f"{index + 1}. {file_name}")
            while True:
                try:
                    file_download = int(input("\nEnter the number of the file you want to download: "))
                    if file_download == 0:
                        break
                    else:
                        file_download = file_names[int(file_download) - 1]
                        file_from_user = file_download
                        break
                except KeyboardInterrupt:
                    os.system('cls')
                    print(Fore.RED + 'Exited' + Style.RESET_ALL)
                    exit()
                except:
                    print(f"\nEnter Integer values from 1 - {index+1} only!")
        else:
            file_download = file_names[0]
            file_from_user = file_download


        ftp.retrbinary(f"RETR {file_from_user}", open(f"{FTP_DIRECTORY_server}/{file_from_user}", 'wb').write)
        os.system('cls')
        print(f'Successfully Uploaded file: {file_from_user}\n')
        input("Press Enter to continue...")
        return True

    while True:
        try:
            os.system('cls')
            choice = int(input("Welcome to the FTP Client Menu!\n\n1. Download File\n2. Upload File\n" + Fore.RED + "3. Quit" + Style.RESET_ALL + "\n\n>>"))
            if choice == 1:
                
                ftp.cwd(FTP_DIRECTORY_server)

                files = os.listdir(FTP_DIRECTORY_server)

                os.system('cls')
                print("List of Files" + Fore.GREEN + " present " + Style.RESET_ALL + "in the FTP Server's Directory available for download:\n")
                for index, filename in enumerate(files):
                    print(f"{index + 1}. {filename}")
                
                print("\nEnter the" + Fore.RED + " file name" + Style.RESET_ALL + " that you want to download (Allowed to Omit file extensions e.g. '.txt')\n")

                while True:
                    try:
                        user_file_input = input(">> ") #<- to add in the flexibility of choosing which files you want to download
                        if user_file_input == "" or user_file_input.strip() == '':
                            print("\nPlease input something!")
                            input("\nPress Enter to continue...")
                            break
                        if(getFile(ftp,user_file_input)):
                            ftp.cwd("..")
                            break
                        else:
                            ftp.cwd("..")
                            break
                    except KeyboardInterrupt:
                        os.system('cls')
                        print(Fore.RED + 'Exited' + Style.RESET_ALL)
                        exit()

            elif choice == 2:

                ftp.cwd(FTP_DIRECTORY_client)
            
                files = os.listdir(FTP_DIRECTORY_client)

                os.system('cls')
                print("List of Files" + Fore.GREEN + " present " + Style.RESET_ALL + "in the FTP Client's Directory available for upload:\n")
                for index, filename in enumerate(files):
                    print(f"{index + 1}. {filename}")
                
                print("\nEnter the" + Fore.RED + " file name" + Style.RESET_ALL + " that you want to upload (Allowed to Omit file extensions e.g. '.txt')\n")

                while True:
                    try:
                        user_file_input = input(">> ") #<- to add in the flexibility of choosing which files you want to download
                        if user_file_input == "" or user_file_input.strip() == '':
                            print("\nPlease input something!")
                            input("\nPress Enter to continue...")
                            break
                        if(putFile(ftp,user_file_input)):
                            ftp.cwd("..")
                            break
                        else:
                            ftp.cwd("..")
                            break
                    except KeyboardInterrupt:
                        os.system('cls')
                        print(Fore.RED + 'Exited' + Style.RESET_ALL)
                        exit()
            elif choice == 3:
                break
            else:
                print("Please choose from options " + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")

        except ValueError:
            print("Please choose from options " + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")

