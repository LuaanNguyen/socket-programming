import socket
import struct

def ones_complement_sum(a, b):
    """Perform one's complement addition of two 16-bit integers."""
    result = a + b
    carry = result >> 16  # Extract carry
    result = (result & 0xFFFF) + carry  # Wrap around carry
    return result & 0xFFFF

def compute_checksum(data):
    """Compute one's complement checksum for a list of 16-bit integers."""
    checksum = 0
    for word in data:
        checksum = ones_complement_sum(checksum, word)
    return ~checksum & 0xFFFF  # One's complement of the sum

# Create a server socket
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server listening on port 12345...")

# Accept client connection
connection, address = server_socket.accept()
print(f"Connection established with {address}")

# Receive the data and checksum from the client
data = connection.recv(4)  # Expecting 2 16-bit integers (4 bytes)
checksum_received = struct.unpack('!H', connection.recv(2))[0]  # Expecting checksum (2 bytes)

# Unpack the received data
data_values = struct.unpack('!2H', data)

# Compute the checksum at server
checksum_computed = compute_checksum(data_values)

print(f"Received Data: {data_values}")
print(f"Received Checksum: {bin(checksum_received)}")
print(f"Computed Checksum at Server: {bin(checksum_computed)}")

# Verify the checksum
if checksum_computed == checksum_received:
    print("Data is VALID (Checksum matched).")
else:
    print("Data is INVALID (Checksum mismatch).")

connection.close()
server_socket.close()
