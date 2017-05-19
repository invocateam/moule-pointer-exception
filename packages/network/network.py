import socket

from config import SERVER_IP, SERVER_PORT, RESPONSE_SIZE


class NetworkInterface:
    def __init__(self, host, port):
        self.responseSize = RESPONSE_SIZE
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SERVER_IP, SERVER_PORT))

    def action(self, message):
        print("Send --> ", message)
        self.socket.send(message)
        r = self.socket.recv(self.responseSize)
        return r

    def __del__(self):
        self.socket.close()
