# ProgrammingAssignment2

COSC-6325 Two part program; Observing an application through ptrace and shared libraries

This assignment has three goals:

1. To implement a C/C++ application which traces system calls using ptrace.
2. Determine what shared libraries and functions from those shared libraries a process
   uses.
3. Learning to modify a shared library to force an application to run user-defined code.

PART 1:
I will be writing single-threaded server and client applications which permit the client to
perform two actions: ‘login’ and ‘upload’ to the server. The server and client can be
written in a programming language of your choice. You will then create a tracer
application which will utilize ptrace to monitor and even redirect system calls made by the
server and the client. The tracer will be written in C or C++.

Program should accept 4 parameters. If your program (compiled executable) is called
tracer then running it to trace and analyze the client executable
“tracer -c <path_to_client_executable> <server_port>” should output the required
client information. Running it to trace and analyze the server executable
“tracer -s <path_to_server_executable> <server_port>” should output the required
server information. Running it to trace and analyze the redirect server executable
“tracer -rs <path_to_server_executable> <server_port>” should output the
required redirect server information.

PART 2:
Your goals for this part are as follows:

1. Use the ldd, nm, and objdump commands on your server to see what shared libraries it
   uses.
2. Open the source code for the libcosc_6325_hash.so shared object in the server_lib
   folder then find and examine the function that the server is using.
3. Modify the function so that each call to it dumps the username (can be gotten from the
   users_and_passwords.csv file), plaintext password, the comparison hash, and whether
   the comparison was a success to a csv file in the format seen in the provided example csv
   file.
4. Compile the updated shared object and replace the old one (it might be wise to save a
   copy of the original as well).
5. Restart the server, open the client executable in interactive mode, and run the option
   to log in all users.
6. View the exported file where you dumped the data to verify that it worked.
   When finished, please include your modified shared object source code and header file in a
   separate directory in the root of your project.

Overview
This repository contains a simple server-client application implemented in Python. The server handles login requests and file uploads from clients, while the client provides options for logging in as different users and uploading files to the server.

Server
To run the server, use the following command:
python Server.py <server_port>
Replace <server_port> with desired. Ex: python Server.py 1234

Client
To run the client, use the following command:
python Client.py <server_port>
Replace <server_port> with the port number where the server is running. Ex: python Client.py 1234

Client will be presented with options, choose the one desired.
