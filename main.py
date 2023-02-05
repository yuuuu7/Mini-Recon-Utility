from colorama import Fore,Style
from tabulate import tabulate
import os, threading
from nmap_scanner import Scanner
from send_custom_packet import PacketSender
from ftp_client import run_ftp_client

scan_done = False 

IP = 'localhost scanme.nmap.org'
options = '-p 22-443 -sTU --top-ports 10 -O -sV -sC'
check_options = '-sn'

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + '''
██████╗ ███████╗███████╗ ██████╗
██╔══██╗██╔════╝██╔════╝██╔════╝
██████╔╝███████╗█████╗  ██║     
██╔═══╝ ╚════██║██╔══╝  ██║     
██║     ███████║███████╗╚██████╗
╚═╝     ╚══════╝╚══════╝ ╚═════╝\n''' + Style.RESET_ALL)
    print("** PSEC Info Security Apps **")
    try:
        userChoice = int(input("\n1. Port Scanner\n2. Upload/Download file using FTP\n3. Send Custom Packet\n" + Fore.RED + "4. Quit" + Style.RESET_ALL + "\n\n>>"))
        if userChoice == 1:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.YELLOW + '''
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                    ''' + Style.RESET_ALL)
                data = [['target', IP],
                        ['options', options]]

                print(tabulate(data, tablefmt="fancy_grid")) 
                print('\n1. Scan Network\n2. View PREVIOUS Scan Summary & Report\n3. Edit Targets\n4. Edit Scan Options\n5. Reset Targets and Options to Default\n' + Fore.RED + "6. Quit\n" + Style.RESET_ALL)
                try:
                    # User input to choose the scanning option
                    userChoice_Scan = int(input(">> ")) 
                    # If the user selects option 1
                    if userChoice_Scan == 1:
                        # Check if the target and options are not empty
                        if IP.strip == '' or options.strip == '' or IP == '' or options == '':
                            # If the target or options are empty, prompt user
                            print("\nYou can't leave the fields for Target and Options empty!")
                            input("\nPress Enter to continue...")

                        # If the scan has not been completed yet
                        elif not scan_done:
                            # Clear the screen
                            os.system('cls' if os.name == 'nt' else 'clear')
                            # Prompt user about checking host statuses
                            print("Checking Hosts' Statuses...\n")
                            # Check the status of the hosts
                            nm_alive = Scanner
                            any_alive_hosts = nm_alive.check_hosts(IP)

                            # If there are any live hosts
                            if any_alive_hosts:
                                # Prompt user to proceed with scanning
                                input("\nPress Enter to proceed with scanning...")
                                # Clear the screen
                                os.system('cls' if os.name == 'nt' else 'clear')
                                # Start the scan using the Scanner class
                                nm_scan = Scanner(IP, options)
                                scan_thread = threading.Thread(target=nm_scan.scan_ports)
                                scan_thread.start()
                                # Prompt user to exit while the scan runs
                                input("\nEnter any key to exit while the scan runs asynchronously...")
                                # Set scan_done to True
                                scan_done = True
                            # If there are no live hosts
                            else:
                                # Break from the loop
                                break

                        # If the scan has already been completed
                        else:
                            # If the scan is still running
                            if scan_thread.is_alive():
                                # Clear the screen
                                os.system('cls' if os.name == 'nt' else 'clear')
                                # Prompt user to wait for the scanning to complete
                                print("Scan is still running...")
                                # Prompt user to exit while the scan runs
                                input("\nEnter any key to exit while the scan is still running...")
                            # If the scan has completed
                            else:
                                # Set scan_done to False
                                scan_done = False
                                # Clear the screen
                                os.system('cls' if os.name == 'nt' else 'clear')
                                # Print the scan results
                                print(nm_scan.scan_results())
                                # Call the summary report function
                                nm_scan.summary_report()

                    elif userChoice_Scan == 2:
                        # Try to show the summary report of the last scan, if there was any.
                        try:
                            nm_scan.summary_report()
                        except AssertionError:
                            print("No Results could be found. Looks like you haven't done a Scan recently!")
                            input("\nPress Enter to continue...")

                    elif userChoice_Scan == 3:
                        # Get the IPs of the target to scan
                        IP = input("\nEnter targets (separated by a space): ")

                    elif userChoice_Scan == 4:
                        # Get the options to scan with
                        options = input("\nEnter scan options (seperated by a space): ")

                    elif userChoice_Scan == 5:
                        # Set the default IPs and options for scanning
                        IP = 'localhost scanme.nmap.org'
                        options = '-p 22-443 -sTU --top-ports 10 -O -sV -sC'

                    elif userChoice_Scan == 6:
                        break
                    else:
                        print("\nPlease choose from options " + Fore.GREEN + "1-6" + Style.RESET_ALL + " only!")
                        input("\nPress Enter to continue...")

                except ValueError:
                    print("\nPlease choose from options " + Fore.GREEN + "1-6" + Style.RESET_ALL + " only!")
                    input("\nPress Enter to continue...")

        elif userChoice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            run_ftp_client()
        elif userChoice == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            PacketSender.send_custom_packet_menu()
        elif userChoice == 4:
            break
        else:
            print("\nPlease select from options" + Fore.GREEN + " 1-4 " + Style.RESET_ALL + "only!")
            input("\nPress Enter to continue...")

    except ValueError:
        print("\nPlease choose from options " + Fore.GREEN + "1-4" + Style.RESET_ALL + " only!")
        input("\nPress Enter to continue...")
