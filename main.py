from colorama import Fore,Style
import os
from nmap_scanner import Scanner
from send_custom_packet import PacketSender
from ftp_client import run_ftp_client

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("** PSEC Info Security Apps **")
    userChoice = int(input("\n1. Scan Network\n2. Upload/Downlaod file using FTP\n3. Send Custom Packet\n" + Fore.RED + "4. Quit" + Style.RESET_ALL + "\n\n>>"))

    if userChoice == 1:

        IP = 'localhost scanme.nmap.org'
        options = '-p 22-443 -sTU --top-ports 10 -O -sV -sC'
        os.system('cls' if os.name == 'nt' else 'clear')
        nm_scan = Scanner(IP, options)
        nm_scan.scan_ports()

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
