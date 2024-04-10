# Obligatory Assignment 2: Develop and test a web server
# DATA2410: Networking and Cloud Computing (Spring 2024)

#Task 1: Making a simple webserver
# To develop a web server that handles one HTTP request at a time. 
# Web server should: 1) accept and parse the HTTP request, 2) get the requested file from the server’s file system, 
# 3) create an HTTP response message consisting of the requested file preceded by header lines, 
# 4) send the response directly to the client. 
# If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client.

from socket import *                # To import socket module from socket.  # For network programming: particularly, for creating and interacting with network sockets. 
import sys                          # In order to terminate the program. To get access to some variables used/maintained by the Python interpreter, and functions that interact closely with the interpreter.To pass values from cmd.
import os                           # os module for interacting with the operating system, like creating files and directories, management of files and directories, environment variables, etc.
                                    # I had problems with the UTF-8 encoding. So, I used os.path-module below for escaping it (link: https://docs.python.org/3/library/os.path.html). 

serverSocket = socket(AF_INET, SOCK_STREAM)                     # To create a socket object that will be used for communication in a TCP/IP network environment.

serverPort = 8080                                               # To specify the port number and the host address for the server. 
serverHost = '127.0.0.1'                                              
serverSocket.bind((serverHost, serverPort))                     # Bind to the port.
serverSocket.listen(5)                                          # A server socket will listen the port 8080, max 5 connections.

print('Server listening on {}:{}'.format(serverHost, serverPort))           # To check that we are in the right direction.

while True:                                                 	# Establish the connection. 
    print('Ready to serve...') 
    # Accept a connection
    connectionSocket, addr = serverSocket.accept()              # Server waits on accept() for onnections.
    print('Got connection from', addr)                          # To check that the code works up to this point.

    try:                                                        # To encapsulate the code responsible for handling the HTTP request, reading the requested file, and sending the response.
        message = connectionSocket.recv(1024).decode()          # Read data from the client and print. 
        print("the message is: " + message)
        print(message.split())
        
        if len(message) > 0:
            filename = message.split()[1]                       # Parses each line in the file to extract content.                      
            # connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())        # Send one HTTP header line into socket
            
            # Here, we have a basic implementation of an HTTP server handling GET requests for file resources: 
            # To check that a requested file exists. If it does, then the file's contents is returned with a 200 OK status. 
            # If the file doesn't exist, "404 Not Found" status is printed out. 
            if os.path.isfile(filename[1:]):                    # To check that the file "filename" exists: "os.path.isfile(path)" returns True if path is an existing regular file. 
                                                                # "The path parameters can be passed as strings, or bytes, or any object implementing the os.PathLike protocol." (link: https://docs.python.org/3/library/os.path.html)
                                                                # Slicing [1:] removes the first character of the filename (a slash in a URL). This ensures that the path is relative and not absolute.
                f = open(filename[1:],'r')                      # To initiate a variable "f" for putting there the opened file in a read mode (in case the file exists). 
                data = f.read()                                 # To initiate a variable "data", where we put the file's content while/after reading it.
                
                outputdata = "HTTP/1.1 200 OK\r\n\r\n" + data       # Indicates that the request was successful and prepares the HTTP response. It is followed by the content of the file.
                
                print(outputdata)                               # Debugging: Prints the HTTP response on the server-side + prints the length of the HTTP response (on the next line). 
                print(len(outputdata))
            else:
                outputdata = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"     # If the file doesn't exist, prepares a 404 Not Found response.
            connectionSocket.sendall(outputdata.encode())                       # Sends the encoded response to the client, because sendall() expects bytes-like objects.
                # for i in range(0, len(outputdata)):                           # I used the logic from the for-loop in a different way above for solving the issue with the UTF-8 encoding.          
                #     print(outputdata[i])
                #     connectionSocket.send(outputdata[i].encode())               
                # connectionSocket.send("\r\n".encode())
        connectionSocket.close()                                        # The connection is closed at the end.
    
    except IOError:                                                     # In case of error (e.g., the file was not found), the server sends a "Not Found" message to the client.                             
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\nFile Not Found".encode())
        connectionSocket.close()                                        # The client socket is closed if an exception occurs.

serverSocket.close()                        # To close the connection after the loop: to be sure that all data is sent before closing the connection.
sys.exit()                                  # Terminate the program after sending the data.
