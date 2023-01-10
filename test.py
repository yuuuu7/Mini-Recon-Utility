import nmap

def scan(host, ports, protocols):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host, ports, protocols, arguments='-O -sC -sV --traceroute')
    return nm_scan

def main():
    # Set target IP and top 10 ports
    target_ip = 'localhost scanme.nmap.org'
    ports = ','.join(str(i) for i in range(1, 11))

    # Set protocols to scan for
    protocols = ['tcp', 'udp']

    # Run the scan and store the results
    results = scan(target_ip, ports, protocols)

    # Print scan results
    print(results)

if __name__ == '__main__':
    main()


