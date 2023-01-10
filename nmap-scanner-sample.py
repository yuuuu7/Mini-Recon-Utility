# Ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
# Ref: https://pypi.org/project/python-nmap/
# Name of script: nmap-scan-sample.py
"""
Purpose:
  Script to print results of port scan

Run: 
  Nil

Args:
  Nil

Output:
  Prints items such as host, protocol, port and state after a port scan
"""  

# main starts here
import nmap

# initialize the port scanner
nmScan = nmap.PortScanner()
print(f'Type of nmScan : {type(nmScan)}')

# scan multiple hosts/specify options
IP = 'localhost'                                     # IPs separated by a space
print(f'Target IP      : {IP}')

options = '-p 22-443 -sTU -T5'                        # scanning TCP and UDP ports from 22-443
results = nmScan.scan(hosts=IP, arguments=options)

# print items in dict. Nmap has provided several methods.
print(f'***** NMAP methods *****')
print(f'Command Line: {nmScan.command_line()}')
print(f'Scaninfo    : {nmScan.scaninfo()}')

# You have to explore other methods to do your assignment, especailly those below
print(f' All hosts    : {nmScan.all_hosts()}')
print(f' All protocols: {nmScan["127.0.0.1"].all_protocols()}')
print(f' All ports tcp: {nmScan["127.0.0.1"]["tcp"].keys()}')   # May have run-time error is no tcp port is open
print(f' All ports udp: {nmScan["127.0.0.1"]["udp"].keys()}')   # May have run-time error is no udp port is open
print('**********')

# Review the structure of the dict [initial scan] - scan-tcp-udp-dict.pdf
for host in nmScan.all_hosts():
  for proto in nmScan[host].all_protocols():
    # print(nmScan[host][proto].keys())
    for port in nmScan[host][proto].keys():
      print(f'Hostname    : {host}')
      print(f'Protocol    : {proto}')
      print(f'Port        : {port}')
      print(f'State       : {nmScan[host][proto][port]["state"]}')
      print(f'**********')