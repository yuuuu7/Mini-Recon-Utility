import os

file_path = 'C:/PSEC-CA2/PSEC-CA2/ftpServerData'
if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
    print("The file is readable and writable.")
else:
    print("The file is not readable and writable.")