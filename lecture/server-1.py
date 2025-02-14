import socket

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#AF_INET tells Python to use IPv4.
#SOCK_STREAM tells Python to use the TCP protocol 
#(a reliable, stream-oriented protocol).

# Bind the socket to a specific IP (localhost) and port (12345)
server_socket.bind(('localhost', 12345))

#The server socket is being bound to localhost (127.0.0.1) and port 12345.
#This means the server will listen for client 
#connections only from the local machine on port 12345.

# Listen for incoming connections, maximum 1 client at a time
server_socket.listen(1)

# Print a message to indicate that the server is ready to accept connections
print("Server is listening on port 12345...")

# Accept an incoming connection from the client
# This blocks until a client connects
client_socket, client_address = server_socket.accept()

# Print the address of the client that has connected
print(f"Connection established with {client_address}")

# Send a welcome message to the connected client
# The message is sent as a byte string
client_socket.sendall(b'Hello, client! You are connected to the server.')

# Close the connection with the client
client_socket.close()

# Close the server socket after the communication is done
server_socket.close()
