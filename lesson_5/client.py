import socket
import sys
__author__ = 'sekely'


class SimpleClient(object):
    def __init__(self, addr='localhost', port=50000, buf=1024):
        self.buf = buf
        server_address = (addr, port)

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print 'connecting to %s port %s' % server_address
        self.sock.connect(server_address)

    def send(self, message=None):
        try:
            # Send data
            message = message or 'This is the default message. It will be repeated.'
            print 'sending "%s"' % message
            self.sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(self.buf)
                amount_received += len(data)
                print 'received "%s"' % data
        except Exception as e:
            print 'caught exception: %s' % str(e)
            self.sock.close()

    def close(self):
        print 'closing socket'
        self.sock.close()

if __name__ == '__main__':
    client = SimpleClient()
    msg = sys.argv[1]
    client.send(msg)
    client.close()
