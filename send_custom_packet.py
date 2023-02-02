from scapy.all import send, IP, TCP, ICMP, UDP  
import re 
from colorama import Fore,Style
# srp and sr1 is for layer 2, send for layer 3


def valid_URL(str):

    # IP address pattern
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    # www.example.com pattern
    www_pattern = re.compile(r'^www\.[a-zA-Z0-9]+\.[a-z]{2,}$')
    # http://ww.example.com pattern
    http_pattern = re.compile(r'^http://www\.[a-zA-Z0-9]+\.[a-z]{2,}$')
    # https://example.com pattern
    https_pattern = re.compile(r'^https://[a-zA-Z0-9]+\.[a-z]{2,}$')

    if re.match(ip_pattern, str):
        return "IP address"
    elif re.match(www_pattern, str):
        return "Plain address"
    elif re.match(http_pattern, str):
        return "HTTP address"
    elif re.match(https_pattern, str):
        return "HTTPS address"
    else:
        return "Invalid address"

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

def get_valid_src_addr():
    while True:
        src_addr = input("Enter Source address of Packet: ")
        if valid_URL(src_addr) == False:
            print("Invalid Input, please try again.")
        else:
            return src_addr

def get_valid_dest_addr():
    while True:
        dest_addr = input("Enter Destination address of Packet: ")
        if valid_URL(dest_addr) == False:
            print("Invalid Input, please try again.")
        else:
            return dest_addr

def get_valid_source_port():
  while True:
    try:
      src_port = int(input("Enter Source Port of Packet: "))
      if src_port in range(0, 65536):
        return src_port
      else:
        print("Please enter only ports from 0-65536!")
    except ValueError:
      print("Enter an integer only!")

def get_valid_dest_port():
  while True:
    try:
      dest_port = int(input("Enter Destination Port of Packet: "))
      if dest_port in range(0, 65536):
        return dest_port
      else:
        print("Please enter only ports from 0-65535!")
    except ValueError:
      print("Enter Integer values only!")

def get_valid_pkt_type():
  while True:
    pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ")
    if pkt_type == 'T' or pkt_type == 'U':
      return pkt_type
    elif pkt_type == "I":
      print(" Note: Port number for ICMP will be ignored")
      return pkt_type
    else:
      print("Please enter only Type (T) TCP, (U) UDP, (I) ICMP!")


        
class PacketSender:
  def send_custom_packet_menu():

    """Obtain inputs to create custom packet

    Returns: Nil
    """    
    print("************************")
    print("* Custom Packet        *")
    print("************************\n")

    src_addr = get_valid_src_addr()
    src_port = get_valid_source_port()
    dest_addr = get_valid_dest_addr()
    dest_port = get_valid_dest_port()
    pkt_type = get_valid_pkt_type()

          
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

    print("\n", count , "packet(s)" + Fore.GREEN + " sent" + Style.RESET_ALL + "!\n" )
    input("Press any key to continue...")

