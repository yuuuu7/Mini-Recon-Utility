from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Host", "Hostname", "Protocol", "Port ID", "State", "Product", "Extra Info", "Reason", "CPE"]

import nmap
nm = nmap.PortScanner()

nm.scan('scanme.nmap.org', '22-443')
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport[:10]:
            x.add_row([host, nm[host].hostname(), proto, port, nm[host][proto][port]['state'], nm[host][proto][port].get('name',""), nm[host][proto][port].get('product',""), nm[host][proto][port].get('reason',""), nm[host][proto][port].get('cpe',"")])
print(x)

