import socketserver
from common import make_can_frame
from random import randint


class Handler_TCPServer(socketserver.BaseRequestHandler):
    """
    The TCP Server class for demonstration.

    Note: We need to implement the Handle method to exchange data
    with TCP client.

    """

    def handle(self):
        # self.request - TCP socket connected to the client
        while True:
            self.data = self.request.recv(1024).strip()
            #print("{} sent:".format(self.client_address[0]))
            print(self.data)
            # just send back ACK for data arrival confirmation
            self.request.sendall(make_can_frame(node=3, index=0x305, data=randint(-350,350)))


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 10001

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()