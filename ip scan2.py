import socket
import csv

# Define the IP range to scan
start_ip = '192.168.21.1'
end_ip = '192.168.21.255'

# Open a file for writing
with open('E:\\data2\\ip_scan_results.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['IP Address', 'Hostname'])

    # Loop over each IP address in the range
    for ip in range(int.from_bytes(socket.inet_aton(start_ip), byteorder='big'),
                    int.from_bytes(socket.inet_aton(end_ip), byteorder='big') + 1):
        # Convert the IP address from integer to dotted-quad format
        ip_address = socket.inet_ntoa(ip.to_bytes(4, byteorder='big'))

        try:
            # Attempt to get the hostname for the IP address
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            # If the hostname can't be found, set it to "Unknown"
            hostname = "Unknown"

        # Write the IP address and hostname to the CSV file
        writer.writerow([ip_address, hostname])
