import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sever_address = '/tmp/socket_file'

try:
    os.unlink(sever_address)
except FileNotFoundError:
    pass

sock.bind(sever_address)

print('Starting up on {}'.format(sever_address))

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    
    try:
        print(f'connection from', client_address)

        while True:
            data = connection.recv(16)
            data_str = data.decode('utf-8')
            print('Received {}'.format(data_str))

            if data:
                fake = Faker()
                fake_text = fake.text()
                connection.sendall(fake_text.encode())
            else:
                print('no data from {}'.format(client_address))

    finally:
        print('Closing current connection')
        connection.close()