import socket  # For creating and using sockets for communication
import sys     # For printing errors to the console
import time    # For adding timestamps to the data
import json    # For handling JSON data


# This code runs on the  middle layer(laptop)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port and the node ID (for identifying the device)
com_port = 5556  # Communication port to listen on
node_id = "fc:69:47:c:2f:3"  # Unique identifier for the Raspberry Pi

# Bind the socket to an IP address and port
server_address = ('', int(com_port))  # '' means the server listens on all available interfaces
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections (up to 5 clients can queue for a connection)
sock.listen(5)

try:
    while True:
        # Wait for a client connection
        print("Waiting for a connection...")
        s, addr = sock.accept()  # Accept a connection from a client
        print("Connection established!")

        # Read data sent by the client
        data = s.recv(100)  # Receive up to 100 bytes of data from the client
        print(data)  # Print the received raw data

        # Parse the received data as JSON
        data_dict = json.loads(data)

        # Add the current timestamp to the received data
        data_dict['datetime'] = time.strftime("%Y-%m-%d %H:%M:%S")

        # Check if the node_id matches the expected Raspberry Pi node ID
        if data_dict["node_id"] == "fc:69:47:c:2f:3":
            # Store the received data with timestamp in a text file
            with open("received_data.txt", "a") as f:  # Open the file in append mode
                f.write(json.dumps(data_dict))  # Write the JSON data as a string
                f.write("\n")  # Add a newline for the next entry

        # Wait for 1 second before closing the connection
        time.sleep(1)

        # Close the socket for this client connection
        s.close()

# Ensure the main socket is closed in case of any exceptions or program termination
finally:
    sock.close()
