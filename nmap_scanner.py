import nmap,os
from tabulate import tabulate
from colorama import Fore,Style


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
        return (f"================================\n\nScan Summary:\n\n"
                f"Hosts Scanned: {hosts_scanned}\n"
                f"Open Ports: {open_ports}\n"
                f"Scan Duration: {scan_duration}s"
                "\n\n")
        
    def generate_report(self):
        report = "=====================================\n\nScan Report:\n\n"
        for host in self.nm.all_hosts():
            hostname = self.nm[host].hostname()
            report += Fore.GREEN + f"\nHost: " + Style.RESET_ALL + f"{host} ({hostname})\n\n"
            for protocol in self.nm[host].all_protocols():
                report += Fore.GREEN + f"\nProtocol: " + Style.RESET_ALL + f"{protocol.upper()}\n\n\tPort | State | Protocol\n\t---- ----- ---------\n"
                for port in self.nm[host][protocol]:
                    state = self.nm[host][protocol][port]["state"]
                    product = self.nm[host][protocol][port]["name"]
                    if state == 'open':
                        report += f"\t{port} |" + Fore.GREEN + f" {state}" + Style.RESET_ALL + f" | {product}\n"
                    elif state == 'closed':
                        report += f"\t{port} |" + Fore.RED + f" {state}" + Style.RESET_ALL + f" | {product}\n"
                    elif state == 'filtered':
                        report += f"\t{port} |" + Fore.YELLOW + f" {state}" + Style.RESET_ALL + f" | {product}\n"
                    elif state == 'open|filtered':
                        report += f"\t{port} |" + Fore.BLUE + f" {state}" + Style.RESET_ALL + f" | {product}\n"
                    else:
                        report += f"\t{port} | {state} | {product}\n"
        return report

    def scan_ports(self):
        print(f"Type of nmScan: {type(self.nm)}")
        print(f"Scanning hosts: {self.ip}")
        print("Scanning...")
        self.nm.scan(hosts=self.ip, arguments=self.options)
        
    def scan_results(self):
        print(f"Type of nmScan: {type(self.nm)}")
        print(f"Scanning hosts: {self.ip}")
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
        scan_table = tabulate(table_data, headers=["Host", "Hostname", "Protocol", "Port ID", "State", "Product", "Extra Info", "Reason", "CPE"], tablefmt="fancy_grid")
        return scan_table

    def summary_report(self):
        do_you_want = input("\nDo you want the Scan Summary and Report? [Y/N]")
        if do_you_want.upper() == 'Y':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.generate_summary())
            print(self.generate_report())
            input("\nEnter any key to continue...")
        else:
            input("\nEnter any key to continue...")
