from scapy.all import send, IP, TCP, ICMP, UDP  
import re 
# srp and sr1 is for layer 2, send for layer 3

def valid_URL(str):
 
    # Regex to check valid URL 
    regex = ("(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty 
    # return false
    if (str == None):
        return False
 
    # Return if the string 
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

def send_packet(src_addr:str , src_port:int , dest_addr:str, 
                 dest_port:int, pkt_type:str, pkt_data:str)  -> bool:
  """Create and send a packet based on the provided parameters

  Args:
      src_addr(str) : Source IP address
      src_port(int) : Source Port
      dest_addr(str): Destination IP address
      dest_port(int): Destination Port
      pkt_type(str) : Type of packet (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
      pkt_data(str) : Data in the packet
  Returns:
      bool: True if send successfull, False otherwise
  """    

  if pkt_type == "T":
    pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
  elif  pkt_type == "U":
    pkt = IP(dst=dest_addr,src=src_addr)/UDP(dport=dest_port,sport=src_port)/pkt_data
  else:
    pkt = IP(dst=dest_addr,src=src_addr)/ICMP()/pkt_data
  try:
    send(pkt ,verbose = False)   # Hide "Send 1 packets" message on console
    return True
  except:
    return False
        
def print_custom_menu():
  """Obtain inputs to create custom packet

  Returns: Nil
  """    
  print("************************")
  print("* Custom Packet        *")
  print("************************\n")

  while True:
    src_addr = input("Enter Source address of Packet: ")
    valid_URL(src_addr)
    if valid_URL(src_addr) == False:
      print("Invalid Input, please try again.")
    else:
      break

  src_port = int(input("Enter Source Port of Packet: "))
  while True:
    dest_addr= input("Enter Destination address of Packet: ")
    valid_URL(dest_addr)
    if valid_URL(dest_addr) == False:
      print("Invalid Input, please try again.")
    else:
      break

  dest_port= int(input("Enter Destination Port of Packet: "))
  pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ")

  if pkt_type == "I":
    print("  Note: Port number for ICMP will be ignored")
        
  pkt_data = input("Packet RAW Data (optional, DISM-DISM-DISM-DISM left blank): ")
  if pkt_data == "":
    pkt_data = "DISM-DISM-DISM-DISM"
    
  pkt_count = int(input("No of Packet to send (1-65535): " ))
  start_now = input("Enter Y to Start, Any other return to main menu: ")

  if start_now == "": 
    return
  count = 0
  for i in range(pkt_count):
    if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
      count  = count + 1

  print(count , " packet(s) sent" )
  exit()

print_custom_menu()