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

# Data to send (can be a message or file data)
data = [0b1110011001100110, 0b1101010101010101]  # Example binary data

# Compute checksum at sender
checksum = compute_checksum(data)

# Create a socket and connect to the server
host = '127.0.0.1'  # Localhost
port = 12345  # Server port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Send the data and checksum to the server
message = struct.pack('!2H', *data)  # Pack two 16-bit integers
client_socket.send(message + struct.pack('!H', checksum))

print(f"Sent Data: {data}")
print(f"Sent Checksum: {bin(checksum)}")

client_socket.close()
