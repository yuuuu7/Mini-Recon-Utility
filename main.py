from nmap_scanner import Scanner

IP = 'localhost scanme.nmap.org'
options = '-p 22-443 -sTU --top-ports 10 -O -sV -sC'

nm_scan = Scanner(IP, options)
nm_scan.scan_ports()

