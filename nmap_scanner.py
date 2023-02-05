import nmap,os, socket
from tabulate import tabulate
from colorama import Fore,Style


class Scanner:
    def __init__(self, IP, options):
        """ 
        Also initializes the PortScanner object 'nm' using nmap module.

        Args:
        IP (str): a string containing the IP or hostname of the target to be scanned
        options (str): a string containing options for nmap command line tool
        
        Returns:
        None

        """
        self.ip = IP
        self.options = options
        self.nm = nmap.PortScanner()
        
    def generate_summary(self):

        """
        Generates the summary of the scan results by counting the number of hosts scanned, open ports and 
        the scan duration.

        Args:
        None

        Returns:
        str: a string containing the summary of the scan results.

        """

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

        """
        Generates a report of the scan results by adding the host, protocol, port, state and product 
        information of each host. 

        Args:
        None

        Returns:
        str: a string containing the report of the scan results.

        """
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
        """
        Scans the target IP or hostname with the specified options. 
        Prints the type of the 'nm' object and the target IP/hostname being scanned.

        Args:
        None

        Returns:
        None

        """
        print(f"Type of nmScan: {type(self.nm)}")
        print(f"Scanning hosts: {self.ip}")
        print("Scanning...")
        self.nm.scan(hosts=self.ip, arguments=self.options)
    
    def check_hosts(host_str):
        """
        Checks the status of the specified hosts by trying to connect to port 80 using the socket module.
        Prints the status of each host as alive or dead.

        Args:
        host_str (str): a string containing one or more IP addresses or hostnames separated by spaces.

        Returns:
        bool: True if there are alive hosts, False otherwise.

        """
        # Split the string into a list of hosts
        hosts = host_str.split()
        # List to store alive hosts
        alive_hosts = []
        # List to store dead hosts
        dead_hosts = []
        
        # Iterate over the list of hosts
        for host in hosts:
            # Check if host is localhost
            if host == "localhost":
                # Add it to the alive hosts list
                alive_hosts.append(host)

            try:
                # Check if host is reachable by connecting to port 80
                socket.create_connection((host, 80), timeout=2)
                # If the connection is successful, add the host to the alive hosts list
                alive_hosts.append(host)
            except socket.error as e:
                # If the host is not localhost, add it to the dead hosts list
                if host != "localhost":
                    dead_hosts.append(host)
                    pass
        # Check if there are any alive hosts
        if alive_hosts:
            # Print the status of each alive host
            for host in alive_hosts:
                print(f"Host '{host}' is " + Fore.GREEN + "Alive" + Style.RESET_ALL)
            # Print the status of each dead host
            for host in dead_hosts:
                print(f"Host '{host}' is " + Fore.RED + "Dead" + Style.RESET_ALL)
            # Return True if there are alive hosts
            return True
        elif dead_hosts:
            # Print the status of each dead host
            for host in dead_hosts:
                print(f"Host '{host}' is " + Fore.RED + "Dead" + Style.RESET_ALL)
            # Print a message indicating that all hosts are dead
            print("\nHosts are either " + Fore.RED + "Dead " + Style.RESET_ALL + "or have blocked off incoming NMAP Scans.")
            # Wait for user input
            input("\nPress Enter to continue...")
            # Return False if there are no alive hosts
            return False

    def scan_results(self):
        """
        Prints a table of the 'nm' object and the target IP/hostname being scanned. Containing Host, Hostname, Protocol, Port ID, State, Product, Extra Info, Reason, CPE

        Args:
        None

        Returns:
        None
        """
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
        """
        Asks the user if they want the Scan Summary and Report, and if yes, prints the generated summary and report.

        Returns:
        None
        
        """

        while True:
            do_you_want = input("\nDo you want the Scan Summary and Report? [Y/N]")
            if do_you_want.upper() == 'Y':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(self.generate_summary())
                print(self.generate_report())
                input("\nEnter any key to continue...")
                break
            elif do_you_want.upper() == 'N':
                input("\nEnter any key to continue...")
                break
            else:
                print("Please select Y/N")
