# Name of script: nmap-pretty-print-IPs-options-items.py
"""
Purpose:
  Script to print results of port scan
  Ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap

Run: 
  Nil

Args:
  Nil

Output:
  Prints items such as host, protocol, port and state after a port scan
  File: nmap-pretty-print-IPs-options-items.txt (Redirect standard output write to file)
"""  

def pretty_dict_json(print_dict: dict):
  """
  Python has a built-in package called json , which can be used to work with JSON data. The json library can parse JSON from strings or files. 
  The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

  Convert dict to json format print it to show the dict structure
  Ref: https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

  Args:
      print_dict (dict): result of port scan
  """  
  import json
  print('\n')
  print('*** print json format*****')
  print(json.dumps(print_dict, indent = 2))

def pretty_print(print_dict: dict):
  """
  The pprint module in Python is a utility module that you can use to print data structures in a readable, pretty way. It's a part of the 
  standard library that's especially useful for debugging code dealing with API requests, large JSON files, and data in general.
  
  Use the pprint library to show the dict structure

  Args:
      print_dict (dict): result of port scan
  """  
  import pprint
  print('\n')
  print('*** pretty print dict: results *****')
  pprint.pprint(print_dict)

# main starts here
import nmap

# initialize the port scanner
nmScan = nmap.PortScanner()
print(f'Type of nmScan : {type(nmScan)}')

# scan multiple hosts/specify options
IP = 'localhost scanme.nmap.org'                        # IPs separated by a space
print(f'Target IP      : {IP}')

options = '-p 80-90 -sTU'                        # scanning TCP and UDP ports
results = nmScan.scan(hosts=IP, arguments=options)
# print(f'Type of results: {type(results)}')

# print using pretty print library
# pretty_print(print_dict=results)

# convert dict to json and pretty print
# pretty_dict_json(print_dict=results)

"""
{
  "nmap": {
    "command_line": "nmap -oX - --top-ports 3 -sTU localhost",
    "scaninfo": {
      "tcp": {
        "method": "connect",
        "services": "23,80,443"
      },
      "udp": {
        "method": "udp",
        "services": "137,161,631"
      }
    },
    "scanstats": {
      "timestr": "Sun Aug 14 16:54:42 2022",
      "elapsed": "4.62",
      "uphosts": "1",
      "downhosts": "0",
      "totalhosts": "1"
    }
  },
  "scan": {
    "127.0.0.1": {
      "hostnames": [
        {
          "name": "localhost",
          "type": "user"
        },
        {
          "name": "lmlicenses.wip4.adobe.com",
          "type": "PTR"
        }
      ],
      "addresses": {
        "ipv4": "127.0.0.1"
      },
      "vendor": {},
      "status": {
        "state": "up",
        "reason": "localhost-response"
      },
      "tcp": {
        "23": {
          "state": "filtered",
          "reason": "no-response",
          "name": "telnet",
          "product": "",
          "version": "",
          "extrainfo": "",
          "conf": "3",
          "cpe": ""
        },
        "80": {
          "state": "open",
          "reason": "syn-ack",
          "name": "http",
          "product": "",
          "version": "",
          "extrainfo": "",
          "conf": "3",
          "cpe": ""
        },
        "443": {
          "state": "filtered",
          "reason": "no-response",
          "name": "https",
          "product": "",
          "version": "",
          "extrainfo": "",
          "conf": "3",
          "cpe": ""
        }
      },
      "udp": {
        "137": {
          "state": "open|filtered",
          "reason": "no-response",
          "name": "netbios-ns",
          "product": "",
          "version": "",
          "extrainfo": "",
          "conf": "3",
          "cpe": ""
        },
        "161": {
          "state": "closed",
          "reason": "port-unreach",
          "name": "snmp",
          "product": "",
          "version": "",
          "extrainfo": "",
          "conf": "3",
          "cpe": ""
        },
        "631": {
          "state": "closed",
          "reason": "port-unreach",
          "name": "ipp",
          "product": "",
          "version": "",
          "extrainfo": "",
          "conf": "3",
          "cpe": ""
        }
      }
    }
  }
}
"""
# print items in dict. Nmap has provided several methods.
# Ref: https://pypi.org/project/python-nmap/
print(f'***** NMAP methods *****')
print(f'Command Line: {nmScan.command_line()}')
print(f'Scaninfo    : {nmScan.scaninfo()}')
print(f'Hostname    : {nmScan["127.0.0.1"].hostname()}')
# pretty_dict_json(nmScan["127.0.0.1"])
print(f'hostname    : {nmScan["127.0.0.1"].hostname()}')
print(f'hostname    : {nmScan["127.0.0.1"]["hostnames"]}')
print(f'State       : {nmScan["127.0.0.1"].state()}')

# You have to explore other methods to do your assignment, especailly those below
print(f' All host     : {nmScan.all_hosts()}')
print(f' All protocol : {nmScan["127.0.0.1"].all_protocols()}')
print(f' All ports    : {nmScan["127.0.0.1"]["tcp"].keys()}')
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