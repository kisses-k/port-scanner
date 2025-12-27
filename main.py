import port_scanner

# Test 1: Scan a website (Verbose mode)
print("--- Scanning scanme.nmap.org ---")
print(port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True))

# Test 2: Scan an IP (Verbose mode)
# Note: 104.26.10.233 is a Cloudflare IP often used for stackoverflow
print("\n--- Scanning IP 104.26.10.233 ---")
print(port_scanner.get_open_ports("104.26.10.233", [80, 443], True))

# Test 3: Invalid Hostname
print("\n--- Testing Invalid Hostname ---")
print(port_scanner.get_open_ports("scanme.nmap", [22, 44], False))

# Test 4: Invalid IP
print("\n--- Testing Invalid IP ---")
print(port_scanner.get_open_ports("266.255.9.9", [22, 42], False))