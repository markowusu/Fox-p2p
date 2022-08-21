import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    print(f'This is the server address {host}')
    port = 4000  # initiate port no above 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together


    
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    try:
        #  getting the connected clients ip address 
        # peer_name = server_socket.getpeername()
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

    finally:
        conn.close()  # close the connection


if __name__ == '__main__':
    server_program()