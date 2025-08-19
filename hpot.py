#!user/bin/env python3

import socket

#main
def main():
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
    server_socket.bind(('',2222))
    server_socket.listen(223)
    
    client_socket, client_address = server_socket.accept()
    print(f"got connection from {client_address[0]}:{client_address[1]}")
    client_socket.send(b"hi\n")
    print(client_socket.recv(256).decode())

if __name__=="__main__":
    main()