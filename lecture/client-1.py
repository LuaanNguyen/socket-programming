import socket

# Create a socket object for the client
# AF_INET: Use IPv4 addressing
# SOCK_STREAM: Use TCP (stream-oriented, reliable communication)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at the specified IP ('localhost') and port (12345)
# This establishes a connection to the server that is listening on port 12345
client_socket.connect(('localhost', 12345))

# Receive a message from the server
# The argument 1024 specifies the maximum number of bytes to receive at once
# The server's message will be received and stored in the 'message' variable
message = client_socket.recv(1024)

# Print the message received from the server
# 'decode()' is used to convert the byte string to a regular string for display
print(f"Message from server: {message.decode()}")

# Close the connection once the message is received and printed
# This releases the resources used by the client socket
client_socket.close()
