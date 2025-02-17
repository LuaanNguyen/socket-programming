"""
Luan Nguyen
CSE434 
Homework 01
Sunday, Feb 16, 2025
"""
import socket

port = 12345 # Must have the same port address with server
ip_address = 'localhost'

# ------------- START CLIENT -------------

#AF_INET tells Python to use IPv4.
#SOCK_STREAM tells Python to use the TCP protocol 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((ip_address, port))

# Receive a welcome message from server
welcome_message = client_socket.recv(1024).decode()
print(f"Message from Server: {welcome_message}")

# This loop is intended to keep getting messages to send to server
while True:
    client_message = input("Enter your message: ")

    # Break out of loop if there's an exit message
    if client_message.lower() == "exit":
        client_socket.send(client_message.encode())  
        break

    # Send message
    client_socket.send(client_message.encode())

    # Receive response from server
    server_message = client_socket.recv(1024).decode()
    print(f"Message from Server: {server_message}")
    
# Close the client socket after the communication is done
client_socket.close()
print("Client Closed.\n")
