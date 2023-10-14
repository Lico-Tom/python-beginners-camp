from socketserver import BaseRequestHandler, UDPServer
import time


class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('go connection from: ', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascill'), self.client_address)


from socket import socket, AF_INET, SOCK_DGRAM


def socket_client():
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(b'hello', ('localhost', 20000))
    s.recvfrom(8192)


if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()
