#!user/bin/env python3

import socket
import threading
import paramiko

class SSHServer(paramiko.ServerInterface):
     def check_auth_password(self, username: str, password: str) -> int:
          print(f"{username}:{password}")
          return paramiko.AUTH_FAILED

def handle_connection(client_socket):
    #use to test TCP connection
     #client_socket.send(b"hi\n")
        #print(client_socket.recv(256).decode())

        #use paramiko to run ssh server with the client socket
        transport=paramiko.Transport(client_socket)
        #key=paramiko.RSAKey.generate(2048)
        key=paramiko.RSAKey.from_private_key_file('key')
        transport.add_server_key(key)
        ssh=SSHServer()
        transport.start_server(server=ssh)

#main
def main():
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
    server_socket.bind(('',2222))
    server_socket.listen(223)
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"got connection from {client_address[0]}:{client_address[1]}")
        t = threading.Thread(target=handle_connection, args=(client_socket,))
        t.start()

if __name__=="__main__":
    main()