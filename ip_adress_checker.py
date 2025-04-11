import socket
import subprocess
import platform
import ipaddress
maintext = """

   _____                                  _     _____ _____  
  / ____|                                | |   |_   _|  __ \ 
 | |     ___  _ __   __ _ _   _  ___  ___| |_    | | | |__) |
 | |    / _ \| '_ \ / _` | | | |/ _ \/ __| __|   | | |  ___/ 
 | |___| (_) | | | | (_| | |_| |  __/\__ \ |_   _| |_| |     
  \_____\___/|_| |_|\__, |\__,_|\___||___/\__| |_____|_|     
                       | |                                   
                       |_|                                   


Telegram channel: @conquestcoder

Github: https://github.com/Conquestcoder

"""
infoabout = """ 
This project was made by Telegram: @Conquestcoder
"""

def get_ip_info(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return None

def ping_ip(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', ip_address]
    
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e}"

def traceroute_ip(ip_address):
    command = ['tracert', ip_address] if platform.system().lower() == 'windows' else ['traceroute', ip_address]
    
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except FileNotFoundError:
        return "Traceroute command not found. Please install it or use a different service."
    except subprocess.CalledProcessError as e:
        return f"Traceroute failed: {e}"

def whois_lookup(ip_address):
    command = ['whois', ip_address]
    
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        return output
    except FileNotFoundError:
        return "Whois command not found. Please install it or use a different service."
    except subprocess.CalledProcessError as e:
        return f"Whois lookup failed: {e}"

def validate_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return True, ip
    except ValueError:
        return False, None

def subnet_info(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        subnet = ipaddress.ip_network(f"{ip}/24", strict=False)  # Assuming a /24 subnet for simplicity
        return f"Subnet: {subnet}, Network Address: {subnet.network_address}, Broadcast Address: {subnet.broadcast_address}"
    except ValueError:
        return "Invalid IP address for subnet calculation."

def main():
    print(maintext)
    
    while True:
        ip_address = input("\nEnter an IP address (or 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            print("Exiting the program.")
            break
        
        is_valid, ip_obj = validate_ip(ip_address)
        if not is_valid:
            print("Invalid IP address. Please try again.")
            continue
        
        print("\nChoose a service:")
        print("1. Get Hostname")
        print("2. Ping Test")
        print("3. Traceroute")
        print("4. Whois Lookup")
        print("5. Nothing Lol")
        print("6. Subnet Information")
        print("7. About this Project")  # Added option for project info
        
        choice = input("Enter the number of the service you want to use: ")
        
        if choice == '1':
            hostname = get_ip_info(ip_address)
            if hostname:
                print(f"Hostname for {ip_address}: {hostname}")
            else:
                print("Hostname not found.")
        
        elif choice == '2':
            print("Pinging...")
            ping_result = ping_ip(ip_address)
            print(ping_result)
        
        elif choice == '3':
            print("Performing traceroute...")
            traceroute_result = traceroute_ip(ip_address)
            print(traceroute_result)
        
        elif choice == '4':
            print("Performing whois lookup...")
            whois_result = whois_lookup(ip_address)
            print(whois_result)
        
        elif choice == '5':
            print("Nothing...")
            
        
        elif choice == '6':
            print("Getting subnet information...")
            subnet_result = subnet_info(ip_address)
            print(subnet_result)
        elif choice == '7':
            print(infoabout)  # Display project info
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()