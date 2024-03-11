import socket
from threading import Thread
import logging

logging.basicConfig(filename='logname', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_ip(ip):
    # Проверяем, является ли адрес локальным или некорректным
    if ip.startswith("127.") or ip.startswith("0.") or ip.startswith("255."):
        return False
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    if octets[0] == '10':
        return False
    if octets[0] == '192' and octets[1] == '168':
        return False
    if octets[0] == '172' and 16 <= int(octets[1]) <= 31:
        return False
    return True

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            logging.info(f"Port {port} is open on {target_ip}")
        s.close()
    except Exception as e:
        logging.info(f"Error scanning port {port}: {e}")

def scan_ports(target_ip):
    threads = []
    for port in range(1, 1025):
        t = Thread(target=scan_port, args=(target_ip, port))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

  
for ip1 in range(1, 256):
    for ip2 in range(1, 256):
        for ip3 in range(1, 256):
            for ip4 in range(1, 256):
                target_ip = f"{ip1}.{ip2}.{ip3}.{ip4}"
                if is_valid_ip(target_ip):
                    logging.info(f"Scanning {target_ip}...")
                    scan_ports(target_ip)
