import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sever_address = '/tmp/socket_file'

try:
    sock.connect(sever_address)
except socket.error as err:
    print(err)
    sys.exit(1)

print('connecting to {}'.format(sever_address))

try:
    while True:
        message = input()
        encod_message = message.encode('utf-8')
        sock.sendall(encod_message)

        data = sock.recv(32).decode('utf-8')
        if data:
            print('sever response: {}'.format(data))
        else:
            break

finally:
    print('closing socket')
    sock.close()