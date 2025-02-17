"""
Luan Nguyen
CSE434 
Homework 01
Sunday, Feb 16, 2025
"""
import socket
import threading
from datetime import datetime

maximum_clients = 10 # Allow up to 10 clients
port = 12345 # Must have the same port address with client
ip_address = 'localhost'

# ------------- FUNCTION TO HANDLE CLIENT MESSAGES -------------
def handle_client_messages(client_socket, client_address):
    current_time = datetime.now() #get current time
    
    # Greet the client with a welcome message (e.g., "Hello, Client X!")
    message = f"Hello, Client {client_address[1]}!" 
    encoded_message = message.encode('utf-8') #encode the message to send

    client_socket.sendall(encoded_message)
    
    # Log interaction to the console.
    print(f"[{current_time.strftime('%a %d %b %Y, %I:%M%p')}] Connection established with Client {client_address[1]}")

    # Loop to keep receving message from client
    while True:
        # Receive message from client and decode it
        client_message = client_socket.recv(1024)
        client_message_decoded =  client_message.decode()
        
        if not client_message_decoded:
            break  

        #Get the current time and format it appropriately (documentation: https://docs.python.org/3/library/datetime.html)
        current_time = datetime.now()
        
        # Log all interactions (e.g., timestamps and messages) to the console.
        print(f"[{current_time.strftime('%a %d %b %Y, %I:%M%p')}] Client {client_address[1]}'s message: {client_message_decoded}")

        # Accept and echo any messages received from the client.
        response = f"Received: {client_message_decoded}"
        client_socket.sendall(response.encode('utf-8'))

    # Close client socket when done and log the message that client is closing.
    client_socket.close()
    print(f"[{datetime.now().strftime('%a %d %b %Y, %I:%M%p')}] Connection with Client {client_address[1]} is closed.")

# ------------- START SERVER -------------

#AF_INET tells Python to use IPv4.
#SOCK_STREAM tells Python to use the TCP protocol 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP and port 
server_socket.bind((ip_address, port))

# Listen for incoming connections with maximum amount of clients (10) at a time
server_socket.listen(maximum_clients)

print(f"Server is listening on {ip_address}:{port}...")

# Loop to handle multiple clients using Threading
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client_messages, args=(client_socket, client_address))
    client_thread.start()

# Close the server socket after the communication is done
server_socket.close()
print("Server Closed.\n")
