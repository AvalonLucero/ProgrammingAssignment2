import socket
import os
import signal
import csv
import sys

# Define server address and port
SERVER_HOST = '127.0.0.1'

# Function to handle SIGINT signal
def signal_handler(sig, frame):
    print("\n[*] Server shutting down...")
    server_socket.close()
    exit(0)

# Register signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Function to verify password
def verify_password(username, password):
    with open('users/users_and_passwords.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

# Function to handle client login
def handle_login(client_socket):
    data = client_socket.recv(1024).decode()
    if data == 'login':
        client_socket.send("Enter username:".encode())
        username = client_socket.recv(1024).decode()
        client_socket.send("Enter password:".encode())
        password = client_socket.recv(1024).decode()
        if verify_password(username, password):
            client_socket.send(f"Login successful for user '{username}'".encode())
        else:
            client_socket.send(f"Login unsuccessful for user '{username}'".encode())

# Function to handle file upload
def handle_upload(client_socket):
    data = client_socket.recv(1024).decode()
    if data == 'upload':
        client_socket.send("Enter file name:".encode())
        filename = client_socket.recv(1024).decode()
        client_socket.send("Enter file content:".encode())
        file_content = client_socket.recv(20480).decode()
        if filename.endswith('.xls') and len(file_content) <= 20480:
            client_socket.send(f"File '{filename}' uploaded successfully".encode())
        else:
            client_socket.send(f"File upload failed for '{filename}'".encode())

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to server address and port
server_socket.bind((SERVER_HOST, int(sys.argv[1])))

# Listen for incoming connections
server_socket.listen(1)
print(f"[*] Server listening on {SERVER_HOST}:{sys.argv[1]}")

# Accept incoming connections and handle them
while True:
    client_socket, client_address = server_socket.accept()
    print("[*] A client has joined")
    handle_login(client_socket)
    handle_upload(client_socket)
    client_socket.close()
    print("[*] A client has exited")
