from socketserver import BaseRequestHandler, TCPServer
from socket import socket, AF_INET, SOCK_STREAM


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Get connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


def simple_tcp_client_0():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect('localhost', 20000)
    s.send(b'hello')
    s.recv(8192)


if __name__ == '__main__':
    # simple tcp server
    # serv = TCPServer(('', 20000), EchoHandler)
    # serv.serve_forever()
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()
