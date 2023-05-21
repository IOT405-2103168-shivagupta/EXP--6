import socket
import csv

# Define the IP range to scan
start_ip = '192.168.1.1'
end_ip = '192.168.1.255'

# Open a file for writing
with open('ip_scan_results.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['IP Address', 'Hostname'])

    # Loop over each IP address in the range
    for ip in range(int(socket.inet_aton(start_ip).hex(), 16), int(socket.inet_aton(end_ip).hex(), 16) + 1):
        # Convert the IP address from hex to dotted-quad format
        ip_address = socket.inet_ntoa(hex(ip)[2:].zfill(8).decode('hex'))

        try:
            # Attempt to get the hostname for the IP address
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            # If the hostname can't be found, set it to "Unknown"
            hostname = "Unknown"

        # Write the IP address and hostname to the CSV file
        writer.writerow([ip_address, hostname])
