DATA2410: Networking and Cloud Computing (Spring 2024

Assignment 2: Develop and test a web server

# Task 1: Simple HTTP Server
Overview
This Python script implements a basic HTTP server capable of handling GET requests for file resources. It listens on a specified port for incoming connections, reads the requested file, and sends an appropriate HTTP response to the client.

Variables
- `serverSocket`: Socket object for the server.
- `serverPort`: Port number for the server.
- `serverHost`: Host address for the server.
- `connectionSocket`: Socket object for client connections.
- `addr`: Address of the connected client.
- `message`: Message received from the client.
- `filename`: Name of the requested file.
- `f`: File object for reading the requested file.
- `data`: Content of the requested file.
- `outputdata`: HTTP response to be sent to the client.

Functions

Main Function
`while True:`
- Functionality: Accepts incoming connections and handles client requests.
- Inputs: None
- Outputs: None
- Returns: None
- Exception Handling: Catches IOError when the requested file is not found and sends a "404 Not Found" response to the client.

Exception Handling

- Functionality: Handles exceptions that may occur during the execution of the server.
- Inputs: None
- Outputs: None
- Returns: None

How Functions Are Used
- `while True:`Continuously listens for incoming connections and processes client requests.
- `try...except IOError:` Handles exceptions that occur during file I/O operations, such as file not found errors.


  # Task 2: HTTP Web client
This simple HTTP client script sends an HTTP GET request to a specified server and retrieves the response.

Functions
1) http_get_request(serverHost, serverPort, path)  :     
Sends an HTTP GET request to the specified server and retrieves the response.

Parameters:
  `serverHost` (str): The IP address or hostname of the server.
  `serverPort` (int): The port number of the server.
  `path` (str): The path to the requested object on the server.
Returns: None
Exceptions: Any exceptions raised during socket operations are handled by closing the socket gracefully.

2) main()  : 
Handles command-line arguments and calls the `http_get_request()` function.   
Parameters: None    
Returns: None    
Exceptions: None handled within this function.

Usage:  
To use this script, run it from the command line with the following arguments: python3 webserver.py 127.0.0.1 8080 /index.html


# Task 3: A multi-threaded HTTP Server
This is an HTTP server implemented in Python using sockets and threading. 
It listens for incoming connections on port 8080, processes client requests, and sends back a basic HTML response.

Dependencies: Python 3.x
Installation: No installation is required, except of Python 3.x.

Functions
1) `manage_client(client_socket)`
- Description: This function handles each client connection by receiving the client's request, generating an HTML response, and sending it back to the client.
- Input Parameters: 
    - `client_socket`: The socket object representing the connection to the client.
- Output Parameters: N/A
- Returns: N/A
- Exception Handling: No explicit exception handling is implemented in this function. Any exceptions raised during socket operations or threading may lead to program termination or unexpected behavior.
2) `main()`
- Description: This function is the entry point of the program. It creates a server socket, listens for incoming connections, and initiates a new thread to handle each client connection.
- Input Parameters: N/A
- Output Parameters: N/A
- Returns: N/A
- Exception Handling: No explicit exception handling is implemented in this function. Any exceptions raised during socket operations or threading may lead to program termination or unexpected behavior.

Usage
1. Run the script `python3 multithreaded.py` in cmd.
2. Once the server is running, it will listen for incoming connections on port 8080.
3. You can send HTTP requests to `http://127.0.0.1:8080` to receive the predefined HTML response (In other words: to open the browser and to type the address: http://localhost:8080/index.html. To press Enter, and the server will send the requested file, which will be desplayed with updated/new content).

