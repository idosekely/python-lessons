import socket
import sys
__author__ = 'sekely'

class SimpleServer(object):

    def __init__(self, addr='localhost', port=50000, buf=1024):
        self.buf = buf
        self.server_address = (addr, port)
        print('setting up server up on %s port %s' % self.server_address)
        self._bind()

    def _bind(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.server_address)

    def _listen(self):
        # Listen for incoming connections
        self.sock.listen(1)

    def _accept(self):
        print('waiting for a connection')
        # Wait for a connection
        connection, client_address = self.sock.accept()
        return connection, client_address

    def start(self):
        self._listen()
        while True:
            connection, client_address = self._accept()
            try:
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(self.buf)
                    print('received "%s"' % data)
                    if data:
                        print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print('no more data from', client_address)
                        break
            finally:
                # Clean up the connection
                connection.close()

    def stop(self):
        print("\nclosing server")
        self.sock.close()

if __name__ == '__main__':
    server = SimpleServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
