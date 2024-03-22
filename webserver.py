#Task 1: Making a simple webserver
# To develop a web server that handles one HTTP request at a time. 
# Web server should: 1) accept and parse the HTTP request, 2) get the requested file from the server’s file system, 
# 3) create an HTTP response message consisting of the requested file preceded by header lines, 
# 4) send the response directly to the client. 
# If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client.

from socket import *                # import socket module from socket
import sys                          # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 8080                   
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)                                          # A server socket will listen the port 8080

while True:                                                 	# Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()

    try:                                                    # To encapsulate the code responsible for handling the HTTP request, reading the requested file, and sending the response.
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() 
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())        # Send one HTTP header line into socket
                                        
        # The for loop from the teacher's file (I mean - for i in range(0, len(outputdata)):...) should be placed within the try block. 
        # Otherwise, it will run (and send the content of the requested file to the client) even if an exception occurs.
        # In addition, we try to iterate over the length of outputdata there, but outputdata is a string, so it doesn't need to be indexed. 
        # We can directly send outputdata without iterating over its characters.
        
        connectionSocket.send(outputdata[i].encode())                   # Send the content of the requested file to the client        
        #connectionSocket.send("\r\n".encode())  
        connectionSocket.close()                                        # The connection is closed at the end.
    
    except IOError:             # In case of error (e.g., the file not being found), the server sends a "404 Not Found" message to the client.                             
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\nFile Not Found".encode())
        connectionSocket.close()                    # The connection/client socket is closed if an exception occurs.

serverSocket.close()                        # To close the connection after the loop: to be sure that all data is sent before closing the connection
sys.exit()                                  # Terminate the program after sending the data




