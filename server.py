import socketserver
from random import randint


def make_can_frame(node, index, sub_index=0, data=0, write=True):
    frame = bytearray(2)
    protocol_payload = bytearray([3])
    node_payload = bytearray([node])

    if write:
        mode_payload = bytearray([0x22])
    else:
        mode_payload = bytearray([0x40])

    index_payload = bytearray([index & 0xFF, (index >> 8) & 0xFF])
    sub_index_payload = bytearray([sub_index])
    data_payload = bytearray([data & 0xFF, (data >> 8) & 0xFF, (data >> 16) & 0xFF, (data >> 24) & 0xFF])
    payload = frame + protocol_payload + node_payload + mode_payload + index_payload + sub_index_payload + data_payload
    payload.append(0x08)

    return payload


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
            #self.request.sendall(make_can_frame(node=5, index=0x305, data=randint(-350,350)))


if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 10001

    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()