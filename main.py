from colorama import Fore,Style
import os, threading, time, keyboard
from nmap_scanner import Scanner
from send_custom_packet import PacketSender
from ftp_client import run_ftp_client

scan_done = False 

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("** PSEC Info Security Apps **")
    userChoice = int(input("\n1. Scan Network\n2. Upload/Download file using FTP\n3. Send Custom Packet\n" + Fore.RED + "4. Quit" + Style.RESET_ALL + "\n\n>>"))

    if userChoice == 1:
        if not scan_done:
            IP = 'localhost scanme.nmap.org'
            options = '-p 22-443 -sTU --top-ports 10 -O -sV -sC'
            os.system('cls' if os.name == 'nt' else 'clear')
            nm_scan = Scanner(IP, options)
            scan_thread = threading.Thread(target=nm_scan.scan_ports)
            scan_thread.start()
            input("\nEnter any key to exit while the scan runs...")
            scan_done = True


        else:

            if scan_thread.is_alive():
                os.system('cls' if os.name == 'nt' else 'clear')
                # wait for the scanning to complete
                print("Scan is still running...")
                input("\nEnter any key to exit while the scan runs...")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(nm_scan.scan_results())
                nm_scan.summary_report()
                scan_done = False

    elif userChoice == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        run_ftp_client()
    elif userChoice == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        PacketSender.send_custom_packet_menu()
    elif userChoice == 4:
        break
    else:
        print("Please select from options" + Fore.GREEN + "1-3" + Style.RESET_ALL + " only!")
