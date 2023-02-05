from scapy.all import send, IP, TCP, ICMP, UDP  
import re, os
from colorama import Fore,Style
# srp and sr1 is for layer 2, send for layer 3


def valid_URL(str):

    # IP address pattern
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    # www.example.com pattern
    www_pattern = re.compile(r'^www\.[a-zA-Z0-9]+\.[a-z]{2,}$')
    # http://ww.example.com pattern
    http_pattern = re.compile(r'^http?://www\.[a-zA-Z0-9]+\.[a-z]{2,}$')
    # https://example.com pattern
    https_pattern = re.compile(r'^https?://www\.[a-zA-Z0-9]+\.[a-z]{2,}$')

    if re.match(ip_pattern, str):
        return True
    elif re.match(www_pattern, str):
        return True
    elif re.match(http_pattern, str):
        return True
    elif re.match(https_pattern, str):
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

def get_valid_src_addr():
  """
    Prompts the user to enter a source address of a packet.

    Returns:
    -------
    str : A string containing the source address of the packet.
  """
  while True:
      src_addr = input("Enter Source address of Packet (Accepts IP-Addr/www/http/https)\n>> ")
      if valid_URL(src_addr) == False:
          print("\nInvalid Input, please try again.\n")
      else:
          return src_addr

def get_valid_dest_addr():

    """
    Prompts the user to enter a destination address of a packet.

    Returns:
    -------
    str : A string containing the destination address of the packet.
    """

    while True:
        dest_addr = input("Enter Destination address of Packet (Accepts IP-Addr/www/http/https)\n>> ")
        if valid_URL(dest_addr) == False:
            print("\nInvalid Input, please try again.\n")
        else:
            return dest_addr

def get_valid_source_port():
  """
    Prompts the user to enter a source port of a packet.

    Returns:
    -------
    int : An integer containing the source port of the packet.
    """
  while True:
    try:
      src_port = int(input("Enter Source Port of Packet (1-65535)\n>> "))
      if src_port in range(1, 65536):
        return src_port
      else:
        print("\nPlease enter only ports from 1-65535!\n")
    except ValueError:
      print("\nEnter Integer values only!\n")

def get_valid_dest_port():

  """
    Prompts the user to enter a destination port of a packet.

    Returns:
    -------
    int : An integer containing the destination port of the packet.

    Raises:
    ValueError: If the user inputs a non-integer value.

    """

  while True:
    try:
      dest_port = int(input("Enter Destination Port of Packet (1-65535)\n>> "))
      if dest_port in range(1, 65536):
        return dest_port
      else:
        print("\nPlease enter only ports from 1-65535!\n")
    except ValueError:
      print("\nEnter Integer values only!\n")

def get_valid_pkt_type():

  """
    Prompts the user to enter the type of packet.

    Returns:
    -------
    str : A string containing the type of packet ('T' - TCP, 'U' - UDP, 'I' - ICMP).
    """

  while True:
    pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I)\n>> ").upper()
    if pkt_type == 'T':
      return pkt_type
    if pkt_type == 'U':
      return pkt_type
    elif pkt_type == "I":
      print("\n*Note: Port number for ICMP will be ignored*")
      input("\nPress Enter to continue...")
      return pkt_type
    else:
      print("\nPlease enter only Types (T) TCP, (U) UDP, (I) ICMP!\n")


def get_valid_pkt_count():
  
  """
    Prompts the user to enter the number of packets to send, and returns the number if it's a valid integer between 1 and 65535 (inclusive).
    
    Returns:
    int : Number of packets to send
    """
  while True:
    try:
      pkt_count = int(input("How many Packets to send? (1-65535)\n>> " ))
      if pkt_count in range(1,65536):
        return pkt_count
      else:
        print("\nPlease enter only numbers from 1-65535!\n")
    except ValueError:
      print("\nEnter Integer values only!\n")

        
class PacketSender:
  def send_custom_packet_menu():

    """Obtain inputs to create custom packet

    Returns: Nil
    """    

    options = {
        'Source Address': '',
        'Source Port': '',
        'Destination Address': '',
        'Destination Port': '',
        'Packet Type': '',
        'Packet Data': '',
    }


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("************************")
        print("* Custom Packet        *")
        print("************************\n")
        
        for i, (key, value) in enumerate(options.items(), start=1):
          print(f'{i}. {key}: ' + Fore.GREEN + f'{value}\n' + Style.RESET_ALL)

        if options['Source Address'] == '':
          src_addr = get_valid_src_addr()
          options['Source Address'] = src_addr

        elif options['Source Port'] == '':
          src_port = get_valid_source_port()
          options['Source Port'] = src_port
          
        elif options['Destination Address'] == '':
          dest_addr = get_valid_dest_addr()
          options['Destination Address'] = dest_addr

        elif options['Destination Port'] == '':
          dest_port = get_valid_dest_port()
          options['Destination Port'] = dest_port

        elif options['Packet Type'] == '':
          pkt_type = get_valid_pkt_type()

          if pkt_type == 'T':
            pkt_type_name = 'TCP'
            options['Packet Type'] = pkt_type_name
          if pkt_type == 'U':
            pkt_type_name = 'UDP'
            options['Packet Type'] = pkt_type_name
          elif pkt_type == "I":
            pkt_type_name = 'ICMP'
            options['Packet Type'] = pkt_type_name

        elif options['Packet Data'] == '':
          pkt_data = input("Packet RAW Data (optional, DISM-DISM-DISM-DISM when left blank): ")
          if pkt_data == "":
            pkt_data = "DISM-DISM-DISM-DISM"
          options['Packet Data'] = pkt_data
        
        else:
          break

    while True:      
      pkt_count = get_valid_pkt_count()       
      start_now = input("\nAre you sure you want to send " + Fore.RED + f"{pkt_count}" + Style.RESET_ALL+ " packets to " + Fore.GREEN + f"{dest_addr}" + Style.RESET_ALL + "? [Y/N]\n>> ")

      if start_now.upper() == "Y": 
        count = 0
        for i in range(pkt_count):
          if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
            count  = count + 1

        print("\n",count , "packet(s)" + Fore.GREEN + " sent" + Style.RESET_ALL + "!\n" )
        input("Press any key to continue...")
        break
      elif start_now.upper() == "N":
        break
      else:
        print("Please enter [Y/N] only.")


