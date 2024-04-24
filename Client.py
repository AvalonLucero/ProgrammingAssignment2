import socket
import sys

# Define server address and port
SERVER_HOST = '127.0.0.1'

# Function to handle file upload
def upload_file(filename):
    with open(f'uploads/{filename}', 'rb') as file:
        file_content = file.read()
    client_socket.send("upload".encode())
    client_socket.recv(1024).decode()
    client_socket.send(filename.encode())
    client_socket.recv(1024).decode()
    client_socket.send(file_content)
    response = client_socket.recv(1024).decode()
    print(response)

# Function to handle login
def login(username, password):
    client_socket.send("login".encode())
    client_socket.recv(1024).decode()
    client_socket.send(username.encode())
    client_socket.recv(1024).decode()
    client_socket.send(password.encode())
    response = client_socket.recv(1024).decode()
    print(response)

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, int(sys.argv[1])))

# Main function for interactive client
def interactive_client():
    print("Available options:")
    print("1. Login as user57")
    print("2. Login as user42")
    print("3. Upload CUSR0000SEHA.xls")
    print("4. Upload PCU481481.csv")
    print("5. Upload USSTHPI.xls")
    print("6. Exit")

    while True:
        option = input("Enter option: ")
        if option == '1':
            login('user57', 'password57')
        elif option == '2':
            login('user42', 'password42')
        elif option == '3':
            upload_file('CUSR0000SEHA.xls')
        elif option == '4':
            upload_file('PCU481481.csv')
        elif option == '5':
            upload_file('USSTHPI.xls')
        elif option == '6':
            print("Exiting...")
            client_socket.close()
            exit(0)
        else:
            print("Invalid option. Please try again.")

# Main function
def main():
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_port>")
        exit(1)
    interactive_client()

if __name__ == "__main__":
    main()
