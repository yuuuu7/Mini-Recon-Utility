from test import portScanner

hosts = "localhost"
options = "-sU -sT --top-ports 10"
ps = portScanner(targets = hosts, options = options)
ps.run()