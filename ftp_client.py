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
        """
        Downloads a file from the FTP server.
        
        Parameters:
        ftp (ftplib.FTP): The FTP object.
        file_from_user (str): The name of the file to download.
        
        Returns:
        bool: True if the file was downloaded successfully, False otherwise.

        """
        # Get all file names from the FTP directory that start with `file_from_user`
        file_names = [file for file in os.listdir(FTP_DIRECTORY_server) if file.startswith(file_from_user)]

        # If no file names are found, print a message and return False
        if not file_names:
            os.system('cls')
            print(f"\nFile '{file_from_user}' does not exist on the FTP server\n")
            input("Press Enter to continue...")
            return False
        # If multiple file names are found, display them and ask the user to select one
        elif len(file_names) > 1:
            os.system('cls')
            print(Fore.RED + "Multiple " + Style.RESET_ALL + "files starting with '" + Fore.GREEN +  f"{file_from_user}" + Style.RESET_ALL + "' found on the FTP server:\n")
            for index, file_name in enumerate(file_names):
                print(f"{index + 1}. {file_name}")
            while True:
                try:
                    # Ask the user to enter the number of the file they want to download
                    file_download = int(input("\nEnter the number of the file you want to download (Enter '0' to exit)\n>> "))
                    # If the user enters 0, break the loop
                    if file_download == 0:
                        return False
                    else:
                        # Otherwise, set `file_download` to the selected file name and `file_from_user` to the same value
                        file_download = file_names[int(file_download) - 1]
                        file_from_user = file_download
                        break
                # If the user presses Ctrl-C, exit the program
                except KeyboardInterrupt:
                    os.system('cls')
                    print(Fore.RED + 'Exited' + Style.RESET_ALL)
                    exit()
                # If the user enters an invalid value, print an error message
                except:
                    print(f"\nEnter Integer values from 1 - {index+1} only!")
        # If there is only one file name found, set `file_download` and `file_from_user` to that file name
        else:
            file_download = file_names[0]
            file_from_user = file_download


        # Use FTP's `retrbinary` method to download the selected file to the client's FTP directory
        ftp.retrbinary(f"RETR {file_from_user}", open(f"{FTP_DIRECTORY_client}/{file_from_user}", 'wb').write)
        # Clear the screen and print a success message
        os.system('cls')
        print(f'Successfully Downloaded file: {file_from_user}\n')
        input("Press Enter to continue...")
        # Return True to indicate that the file was successfully downloaded
        return True


    def putFile(ftp, file_from_user):
        
        """
        Uploads a file to the FTP server.
        
        Parameters:
        ftp (ftplib.FTP): The FTP object.
        file_from_user (str): The name of the file to upload.
        
        Returns:
        bool: True if the file was uploaded successfully, False otherwise.

        """
        # Create a list of filenames that match the filename entered by the user
        file_names = [file for file in os.listdir(FTP_DIRECTORY_client) if file.startswith(file_from_user)]

        # If no file was found with the name entered by the user
        if not file_names:
            # Clear the console
            os.system('cls')

            # Print an error message indicating the file does not exist on the FTP server
            print(f"\nFile '{file_from_user}' does not exist on the FTP server\n")

            # Wait for the user to press enter
            input("Press Enter to continue...")

            # Return False to indicate the file upload was unsuccessful
            return False

        # If multiple files were found with a name starting with the name entered by the user
        elif len(file_names) > 1:
            # Clear the console
            os.system('cls')
            # Print a message indicating multiple files were found on the FTP server with a name starting with the name entered by the user
            print(Fore.RED + "Multiple " + Style.RESET_ALL + "files starting with '" + Fore.GREEN +  f"{file_from_user}" + Style.RESET_ALL + "' found on the FTP server:\n")
            # Loop through the list of filenames
            for index, file_name in enumerate(file_names):
                # Print each file name with a number in front of it
                print(f"{index + 1}. {file_name}")
            # Continue to loop until the user selects a file to upload
            while True:
                try:
                    # Prompt the user to enter the number of the file they want to upload
                    file_download = int(input("\nEnter the number of the file you want to upload (Enter '0' to quit)\n>> "))
                    # If the user enters 0, break the loop
                    if file_download == 0:
                        return False
                    else:
                        # Set the file to upload to the selected file
                        file_download = file_names[int(file_download) - 1]
                        file_from_user = file_download
                        break
                # If the user presses ctrl + c, exit the program gracefully
                except KeyboardInterrupt:
                    # Clear the console
                    os.system('cls')
                    # Print an error message indicating the user has exited the program
                    print(Fore.RED + 'Exited' + Style.RESET_ALL)
                    # Exit the program
                    exit()
                # If the user does not enter an integer value from 1 - the number of files found
                except:
                    # Print an error message indicating to enter an integer value from 1 - the number of files found
                    print(f"\nEnter Integer values from 1 - {index+1} only!")
        # If only one file was found with the name entered by the user
        else:
            # Set the file to download to the single file found
            file_download = file_names[0]
            file_from_user = file_download


        # Get the binary content of the file from the FTP server using the "RETR" FTP command
        # Open a local file in write binary mode and write the content from the FTP server
        ftp.retrbinary(f"RETR {file_from_user}", open(f"{FTP_DIRECTORY_server}/{file_from_user}", 'wb').write)

        # Clear the terminal screen
        os.system('cls')

        # Print a success message indicating that the file was successfully uploaded
        print(f'Successfully Uploaded file: {file_from_user}\n')

        # Wait for the user to press enter to continue
        input("Press Enter to continue...")

        # Return True to indicate success in uploading
        return True

    while True:
        try:
            os.system('cls')
            # Display the options for the user to choose from: Download File, Upload File, and Quit.
            choice = int(input("Welcome to the FTP Client Menu!\n\n1. Download File\n2. Upload File\n" + Fore.RED + "3. Quit" + Style.RESET_ALL + "\n\n>>"))

            # If the user chooses 1, navigate to the FTP server's directory.
            if choice == 1:
                ftp.cwd(FTP_DIRECTORY_server)

                # Get the list of files in the FTP server's directory.
                files = os.listdir(FTP_DIRECTORY_server)

                # Clear the screen and display the list of files present in the FTP server's directory available for download.
                os.system('cls')
                print("List of Files" + Fore.GREEN + " present " + Style.RESET_ALL + "in the FTP Server's Directory available for download:\n")
                for index, filename in enumerate(files):
                    print(f"{index + 1}. {filename}")
                
                # Ask the user to enter the file name they want to download, allowing them to omit file extensions (e.g. '.txt').
                print("\nEnter the" + Fore.RED + " file name" + Style.RESET_ALL + " that you want to download (Allowed to Omit file extensions e.g. '.txt'). Enter '!' to exit.\n")

                while True:
                    try:
                        # Get the file name input from the user.
                        user_file_input = input(">> ")

                        if user_file_input == '!':
                            # change to the parent directory of FTP_DIRECTORY_server
                            ftp.cwd("..")
                            break
                        # Check if the user has entered something, and display a message if they haven't.
                        if user_file_input == "" or user_file_input.strip() == '':
                            print("\nPlease input something!")
                            input("\nPress Enter to continue...")
                            break
                        # Call the getFile() function to download the file. If the file was successfully downloaded, navigate back to the parent directory.
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
                # change to FTP_DIRECTORY_client
                ftp.cwd(FTP_DIRECTORY_client)

                # list the files in FTP_DIRECTORY_client
                files = os.listdir(FTP_DIRECTORY_client)

                # clear the console
                os.system('cls')
                # display the list of files in the FTP Client's Directory available for upload
                print("List of Files" + Fore.GREEN + " present " + Style.RESET_ALL + "in the FTP Client's Directory available for upload:\n")
                for index, filename in enumerate(files):
                    print(f"{index + 1}. {filename}")

                # prompt the user to enter the file name to upload
                print("\nEnter the" + Fore.RED + " file name" + Style.RESET_ALL + " that you want to upload (Allowed to Omit file extensions e.g. '.txt'). Enter '!' to exit.\n")

                # loop until the user uploads a file or quits
                while True:
                    try:
                        # get the user's input file name
                        user_file_input = input(">> ")

                        if user_file_input == '!':
                            # change to the parent directory of FTP_DIRECTORY_client
                            ftp.cwd("..")
                            break
                        # if the user input is empty
                        if user_file_input == "" or user_file_input.strip() == '':
                            # display an error message
                            print("\nPlease input something!")
                            # prompt the user to press Enter to continue
                            input("\nPress Enter to continue...")
                            # break the loop
                            break
                        # upload the file
                        if(putFile(ftp,user_file_input)):
                            # change to the parent directory of FTP_DIRECTORY_client
                            ftp.cwd("..")
                            # break the loop
                            break
                        else:
                            # change to the parent directory of FTP_DIRECTORY_client
                            ftp.cwd("..")
                            # break the loop
                            break
                    except KeyboardInterrupt:
                        # clear the console
                        os.system('cls')
                        # display a message that the program has exited
                        print(Fore.RED + 'Exited' + Style.RESET_ALL)
                        # exit the program
                        exit()
            elif choice == 3:
                ftp.cwd("./scripts")
                break
            else:
                print("Please choose from options " + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")

        except ValueError:
            print("Please choose from options " + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")

