# Task 3: Making a multi-threaded web server

# Currently, your web server handles only one HTTP request at a time.
# You should implement a multithreaded server that is capable of serving multiple requests simultaneously. 
# Using threading, first create a main thread in which your modified server listens for clients at a fixed port. 
# When it receives a TCP connection request from a client, it will set up the TCP connection through another port and
# services the client request in a separate thread. There will be a separate TCP connection in a separate thread for each request/response pair.

# Here, it is important to create a separate thread for each client connection.

import socket
import threading

def manage_client(client_socket):                            # The function: 1) processes the client's request, 2) sends the response, 3) runs in a separate thread for each client connection.
    request = client_socket.recv(4096).decode()              # the recv() method for receiving the client's data, which should be no more than 4096 bytes.
                                                             # decode() converts the received bytes into a string. Assigning the decoded string to the variable "request". 
                                                             # So, "request" will contain the data sent by the client, in string format. 
    client_socket.send(response.encode())                                       # Send the HTTP response back to the client
    client_socket.close()                                                       # Close the client socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creates a TCP socket object (server_socket) using the 'socket' module 
                                                                                # 'socket.socket' refers to the socket class within the socket module.  
                                                                                # The used arguments are: the address family (AF_INET) and the socket type (SOCK_STREAM). 
                                                                                # So, the new socket object configured to use IPv4 addresses and the TCP protocol for communication.  
                                                                                
    server_socket.bind(('127.0.0.1', 8080))                                     # Bind the socket to the localhost adress 127.0.0.1 on a port 8080 (endpoint for communication). 
                                                                                # So, the server will listen for incoming connections on 127.0.0.1, port 8080.
    server_socket.listen(5)                                                     # Listen for incoming connections. The server can handle simultaneously 5 queued connections. 
                                                                                # In addition, up to 5 queued connections can be waiting to be accepted by the server.
    print('Server is listening on port 8080...')
    
    while True:
        client_socket, addr = server_socket.accept()                            # Accept a new client connection.
        print(f'Connection from {addr}')                                        # To print a message that a connection has been established with a client: 
                                                                                # 'addr' variable should give information about the client's address (IP address and port number).
        
        # Creates a new thread 'client_thread' to handle the client connection.
        client_thread = threading.Thread(target=manage_client, args=(client_socket,))   # 'Thread'-class allows to create and manage threads.
                                                                                # As a target function is used 'manage_client', which will be executed by a new thread.
                                                                                # (client_socket,) - an argument for a function 'manage_client'. 
                                                                                # It is written in a form of a tuple (comma after 'client_socket' ensures that).
                                                                                # Generally speaking, executaion of 'manage_client' can be done in a separate thread, while the main thread is executing its tasks.
        client_thread.start()                               # Starts execution of the new thread, which was created above. 
                                                            # So, the program will handle multiple clients simultaneously, each in their own separate thread.
if __name__ == "__main__":
    main()