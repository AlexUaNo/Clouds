# Obligatory Assignment 2: Develop and test a web server
# DATA2410: Networking and Cloud Computing (Spring 2024)

# Task 2: Making a web client
# Write your own HTTP client to test your server. 
# Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output.
# You can assume that the HTTP request sent is a GET method.
# The client should take command line arguments specifying the server IP address or host name, 
# the port at which the sever is listening, and the path at which the requested object is stored at the server (use argparse module). 

import socket                                                           # For network programming: particularly, for creating and interacting with network sockets. 
import argparse                                                         # For parsing command-line arguments and options. Parsing simplifies the process of understanding and manipulating structured data by breaking them down into the basic elements.    

def http_get_request(serverHost, serverPort, path):                             # To send an HTTP GET request to a specified server and retrieve the response.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Creates a TCP socket with the address, where (AF_INET) is for IPv4 and the TCP socket type (SOCK_STREAM).
    client_socket.connect((serverHost, serverPort))                             # Connects the client socket to the specified (serverHost) and (serverPort).
    
    request = "GET " + path + " HTTP/1.1\r\nHost: " + serverHost + ":" + str(serverPort) + "\r\n\r\n"           # Constructs the HTTP GET request, which includes:  
                                                                                                                # the request method (GET), the requested path, the HTTP version (HTTP/1.1), and the Host header specifying the server host and port.
    print(request)                                                              # Debugging: prints the constructed HTTP request.
    client_socket.sendall(request.encode())                                     # Sends the HTTP request to the server after encoding it as bytes.  
    
    response = client_socket.recv(4096).decode()                                # Receives server response (which should have max 4096 bytes) & decpdes it. 
    print(response)                                                             # Debugging: displays the server response.
    
    client_socket.close()                                                       # Closes the client's socket.

def main():                                                                     # This function is responsible for handling command-line arguments using the argparse module. 
                                                                                # At the end, it calls above mentioned function "http_get_request()" for sending the HTTP GET request to the specified server.
    parser = argparse.ArgumentParser(description="Simple HTTP client")          # Creates "parser", as the ArgumentParser object. It will handle parsing command-line arguments. 
                                                                                # Parameter "description" includes a short description of the program, which is displayed in the help message.        
    # Add arguments "host", "port" and "path"  to the parser.
    parser.add_argument("serverHost", type=str, help="Server IP address")
    parser.add_argument("serverPort", type=int, help="Server port")
    parser.add_argument("path", type=str, help="Path to the requested object")
    
    args = parser.parse_args()                                                  
    # A variable "args" stores the parsed arguments. The "parse_args()" method helps to parse above mentioned arguments. 
    
    http_get_request(args.serverHost, args.serverPort, args.path)               # Calls the "http_get_request()" function for sending HTTP GET request to the specified server. 
                                                                                # As parameters, the parsed arguments (serverHost, serverPort, and path) are indicated. 

if __name__ == "__main__":                                                      # It ensures that the main() function is executed, when the script runs directly as the main program.
    main()                                                                      # when *(_name__ == "__main__"), the above mentioned main() function is called.
    