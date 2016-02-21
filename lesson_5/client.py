import socket
import sys
__author__ = 'sekely'


class SimpleClient(object):
    def __init__(self, addr='localhost', port=50000, buf=1024):
        self.buf = buf
        server_address = (addr, port)

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print >>sys.stderr, 'connecting to %s port %s' % server_address
        self.sock.connect(server_address)

    def send(self, message=None):
        try:
            # Send data
            message = message or 'This is the default message. It will be repeated.'
            print >>sys.stderr, 'sending "%s"' % message
            self.sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(self.buf)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data
        except Exception as e:
            print >>sys.stderr, 'caught exception: %s' % str(e)
            self.sock.close()

    def close(self):
        print >>sys.stderr, 'closing socket'
        self.sock.close()
