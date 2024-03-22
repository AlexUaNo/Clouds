# Task 2: Making a web client
# Write your own HTTP client to test your server. 
# Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output.
# You can assume that the HTTP request sent is a GET method.
# The client should take command line arguments specifying the server IP address or host name, 
# the port at which the sever is listening, and the path at which the requested object is stored at the server (use argparse module). 

import socket
import argparse

def http_get_request(server_host, server_port, path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creates a TCP socket
    client_socket.connect((server_host, server_port))                           # Connects to the server
    
    request = "GET " + path + " HTTP/1.1\r\nHost: " + server_host + "\r\n\r\n"             # Sends HTTP GET request
    client_socket.sendall(request.encode())
    
    response = client_socket.recv(4096).decode()                                # Receives and display server response
    print(response)
    
    client_socket.close()                                                         # Closes the socket

def main():
    parser = argparse.ArgumentParser(description="Simple HTTP client")               # Creates ArgumentParser object
    
    # Add arguments host, port and path
    parser.add_argument("server_host", type=str, help="Server IP address")
    parser.add_argument("server_port", type=int, help="Server port")
    parser.add_argument("path", type=str, help="Path to the requested object")
    
    args = parser.parse_args()                                                           # Parse command-line arguments
    
    http_get_request(args.server_host, args.server_port, args.path)                     # Calls function to send HTTP GET request

if __name__ == "__main__":
    main()