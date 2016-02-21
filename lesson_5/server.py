import socket
import sys
__author__ = 'sekely'


class SimpleServer(object):
    def __init__(self, addr='localhost', port=50000, buf=1024):
        self.buf = buf
        server_address = (addr, port)
        print >>sys.stderr, 'setting up server up on %s port %s' % server_address

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(server_address)

    def start(self):
        # Listen for incoming connections
        self.sock.listen(1)

        while True:
            print >>sys.stderr, 'waiting for a connection'
            # Wait for a connection
            connection, client_address = self.sock.accept()

            try:
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(self.buf)
                    print >>sys.stderr, 'received "%s"' % data
                    if data:
                        print >>sys.stderr, 'sending data back to the client'
                        connection.sendall(data)
                    else:
                        print >>sys.stderr, 'no more data from', client_address
                        break

            finally:
                # Clean up the connection
                connection.close()
