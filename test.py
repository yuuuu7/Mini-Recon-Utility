class nmapScanner:
    """
    This class is used to scan a list of hosts using nmap.
    Args:
        targets (str): A string of hosts to scan. (e.g "localhost scanme.nmap.org")
        options (str): A string of nmap options to use. (e.g "-sU -sT --top-ports 10 -sV -sC --traceroute -O")
    """

    def __init__(self, targets: str, options: str):
        self.targets = targets
        self.options = options
    
    def run(self):
        """
        Starts the scan
        """
        print("Checking status of hosts...")
        live_hosts = self.is_alive()
        if(live_hosts is not False):
            scan_results = self.perform_scan()
            self.generate_table(scan_results)