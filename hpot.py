#!user/bin/env python3

import socket

#main
def main():
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
    server_socket.bind(('',2222))
    server_socket.listen(223)
    input()

if __name__=="__main__":
    main()