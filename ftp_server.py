# Ref: 
# https://pyftpdlib.readthedocs.io/en/latest/tutorial.html
# https://pyftpdlib.readthedocs.io/en/latest/api.html

# Need to pip install pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer() # handle permission and user

# Define an anonymous user and home directory having read permissions
authorizer.add_anonymous('./' , perm='elradfmw') # you should specify your own home directory

# Instantiate FTP handler class
handler = FTPHandler #  understand FTP protocol
handler.authorizer = authorizer

# Instantiate FTP server class and listen on 127.0.0.1:2121
address = ('127.0.0.1', 2121)
server = FTPServer(address, handler)

# start ftp server
server.serve_forever()


