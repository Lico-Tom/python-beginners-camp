import socket
import time
from threading import Thread
import multiprocessing


def countdown(n, name):
    while n > 0:
        print('T-minus', n, name)
        n -= 1
        time.sleep(2)


class CountDownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


class IOTask:
    def __init__(self):
        self._running = None

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue


if __name__ == '__main__':
    # t = Thread(target=countdown, args=(10, 'Thread-name'))
    # t.start()
    # while True:
    #     print(t.is_alive())
    #    time.sleep(10)
    #    if not t.is_alive():
    #       break
    c = CountDownTask()
    t = Thread(target=c.run, args=(10,), daemon=True)
    t.start()
    # c.terminate()
    t.join()
    c = CountDownTask(5)
    p = multiprocessing.Process(target=c.run)
    p.start()
    
