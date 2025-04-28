import socket

def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        
        # Try to connect to the port
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()
    except socket.error as err:
        print(f"Error scanning port {port}: {err}")

def scan_ports(host, ports):
    for port in ports:
        scan_port(host, port)

if __name__ == "__main__":
    host = '127.0.0.1'  
    ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]
    
    scan_ports(host, ports)
