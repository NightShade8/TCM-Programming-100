# Importing Sockets

In Python, sockets are a fundamental networking concept used for communication between computers over a network. Sockets enable programs to establish connections, send data, and receive data over various network protocols, such as TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). Here's an explanation of sockets in Python:

## 🌐 Socket Programming in Python

Socket programming is a key concept in networking that allows communication between computers over a network. Python's `socket` module provides tools to create and manage sockets for network communication using protocols like TCP and UDP.

### 🛠️ Socket Creation

To create a socket in Python, you need to import the `socket` module. Use the `socket.socket()` function, specifying the address family (e.g., `socket.AF_INET` for IPv4) and the socket type (e.g., `socket.SOCK_STREAM` for TCP or `socket.SOCK_DGRAM` for UDP). Here's an example:

```python
import socket

# 🌐 Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket for reliable communication

# 🌐 Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket for faster, connectionless communication
```

### 🔄 Socket Communication

Once a socket is created, you can use various methods to establish connections and exchange data. Below are some commonly used methods:

- `socket.connect(address)`: Connects to a remote address.
- `socket.bind(address)`: Binds the socket to a specific address and port.
- `socket.listen(backlog)`: Listens for incoming connections (TCP only).
- `socket.accept()`: Accepts an incoming connection and returns a new socket object.
- `socket.send(data)`: Sends data over the socket.
- `socket.recv(buffer_size)`: Receives data from the socket.

#### Example: Basic TCP Server

The following example demonstrates a simple TCP server that listens for incoming connections:

```python
import socket

# 🌐 Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket for server

# 📍 Bind the socket to a specific address and port
server_address = ('localhost', 1234)  # Address and port for the server
server_socket.bind(server_address)

# 👂 Listen for incoming connections
server_socket.listen(5)  # Allow up to 5 pending connections

while True:
    # 🤝 Accept a client connection
    client_socket, client_address = server_socket.accept()  # Wait for a client to connect

    # 📥 Receive data from the client
    data = client_socket.recv(1024)  # Receive up to 1024 bytes of data

    # 📤 Send a response back to the client
    client_socket.send(b"Received: " + data)  # Send acknowledgment

    # ❌ Close the client socket
    client_socket.close()  # End communication with the client
```

### 🚀 Applications

Socket programming enables the creation of client-server applications, networked tools, and other networking tasks. Python's `socket` module provides a robust and flexible way to handle network communication efficiently.