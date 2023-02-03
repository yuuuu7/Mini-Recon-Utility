import nmap
from tabulate import tabulate

class Scanner:
    def __init__(self, IP, options):
        self.ip = IP
        self.options = options
        self.nm = nmap.PortScanner()

    def generate_summary(self):
        hosts_scanned = len(self.nm.all_hosts())
        open_ports = 0
        for host in self.nm.all_hosts():
            open_ports += len(self.nm[host].all_tcp())
        scan_duration = self.nm.scanstats()["elapsed"]
        return (f"Scan Summary:\n"
                f"Hosts Scanned: {hosts_scanned}\n"
                f"Open Ports: {open_ports}\n"
                f"Scan Duration: {scan_duration}")
        
    def generate_report(self):
        report = "Scan Report:\n"
        for host in self.nm.all_hosts():
            hostname = self.nm[host].hostname()
            report += f"Host: {host} ({hostname})\n"
            for protocol in self.nm[host].all_protocols():
                report += f"Protocol: {protocol}\n"
                for port in self.nm[host][protocol]:
                    state = self.nm[host][protocol][port]["state"]
                    product = self.nm[host][protocol][port]["name"]
                    report += f"\tPort: {port} ({state}) ({product})\n"
        return report

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
        do_you_want = input("\nDo you want the Scan Summary and Report? [Y/N]")
        if do_you_want.upper() == 'Y':
            print(self.generate_summary())
            print(self.generate_report())
            input("\nEnter any key to continue...")
        else:
            input("\nEnter any key to continue...")
