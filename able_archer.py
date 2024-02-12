import socket

def handle_client(client_socket):
    try:
        # Send the initial message
        message = "Good day Mr. President!\nIt's Monday, 7th November, 1983. Welcome to Able Archer!\nEnter the SILO 73C password: Bye\n"
        client_socket.sendall(message.encode('utf-8'))
        
        # Receive the password from the client
        password_input = client_socket.recv(1024).strip()  # Adjust buffer size if necessary
        
        # Check the input and respond
        if password_input.decode('utf-8') == "00000000":
            response = "CODE_CTF{COLd_WAR_iS_ovEr}\n"
        else:
            response = "wrong password\n"
        
        client_socket.sendall(response.encode('utf-8'))
    finally:
        # Close the connection to the client
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a public host, and a well-known port
    server_socket.bind(('0.0.0.0', 8888))  # Replace 8888 with your chosen port
    server_socket.listen(10)  # Adjust the backlog (number of pending connections) if necessary
    
    print("Server is running on port 8888...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Shutting down the server...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
