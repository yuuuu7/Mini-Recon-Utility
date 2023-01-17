import nmap
from tabulate import tabulate

class Scanner:
    def __init__(self, IP, options):
        self.ip = IP
        self.options = options
        self.nm = nmap.PortScanner()

    def scan_ports(self):
        print(f"Type of nmScan: {type(self.nm)}")
        print(f"Scanning hosts: {self.ip}")
        print("Scanning...")
        self.nm.scan(hosts=self.ip, arguments=self.options)
        table_data = []
        for host in self.nm.all_hosts():
            hostname = self.nm[host].hostname()
            for protocol in self.nm[host].all_protocols():
                for port in self.nm[host][protocol]:
                    port_id = port
                    state = self.nm[host][protocol][port]["state"]
                    product = self.nm[host][protocol][port]["name"]
                    extra_info = self.nm[host][protocol][port]["extrainfo"]
                    reason = self.nm[host][protocol][port]["reason"]
                    cpe = self.nm[host][protocol][port]["cpe"]
                    table_data.append([host, hostname, protocol, port_id, state, product, extra_info, reason, cpe])
        print(tabulate(table_data, headers=["Host", "Hostname", "Protocol", "Port ID", "State", "Product", "Extra Info", "Reason", "CPE"], tablefmt="fancy_grid"))


