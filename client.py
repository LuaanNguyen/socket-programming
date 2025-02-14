import socket

port = 12345 # Must have the same port address with server
ip_address = 'localhost'

# ------------- START CLIENT -------------
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port))

    welcome_message = client_socket.recv(1024).decode()
    print(f"Message from Server: {welcome_message}")

    while True:
        client_message = input("Enter your message: ")

        if client_message.lower() == "exit":
            client_socket.send(client_message.encode())  
            break

        client_socket.send(client_message.encode())

        server_message = client_socket.recv(1024).decode()
        print(f"Message from Server: {server_message}")
        
except ConnectionRefusedError:
    print("Error: Unable to connect to Server.")

finally:
    client_socket.close()
    print("Client Closed.\n")
