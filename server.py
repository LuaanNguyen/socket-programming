import socket
import threading
from datetime import datetime

maximum_clients = 10 # Allow up to 10 clients
port = 12345 # Must have the same port address with client
ip_address = 'localhost'

# ------------- FUNCTION TO HANDLE CLIENT MESSAGES -------------
def handle_client_messages(client_socket, client_address):
    current_time = datetime.now()
    
    message = f"Hello, Client {client_address[1]}!"
    
    client_socket.sendall(message.encode('utf-8'))
    print(f"[{current_time.strftime('%a %d %b %Y, %I:%M%p')}] Connection established with Client {client_address[1]}")

    try:
        while True:
            client_message = client_socket.recv(1024)
            client_message_decoded =  client_message.decode()
            if not client_message_decoded:
                break  

            current_time = datetime.now()
            print(f"[{current_time.strftime('%a %d %b %Y, %I:%M%p')}] Client {client_address[1]}'s message: {client_message_decoded}")

            response = f"Received: {client_message_decoded}"
            client_socket.sendall(response.encode('utf-8'))

    except ConnectionResetError:
        print(f"Client {client_address[1]} disconnected unexpectedly.")

    finally:
        client_socket.close()
        print(f"[{datetime.now().strftime('%a %d %b %Y, %I:%M%p')}] Connection with Client {client_address[1]} is closed.")

# ------------- START SERVER -------------
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.bind((ip_address, port))
    
    server_socket.listen(maximum_clients)

    print(f"Server is listening on {ip_address}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client_messages, args=(client_socket, client_address))
        client_thread.start()

except KeyboardInterrupt:
    print("Keyboard Interupted, Server shutting down...\n")

finally:
    server_socket.close()
    print("Server Closed.\n")
