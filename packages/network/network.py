import socket
from config import *


class NetworkInterface:
    def __init__(self):
        self.responseSize = 999999
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP_SERVEUR, PORT_SERVEUR))

    def action(self, message):
        print("Send --> ", message)
        self.socket.send(message)
        r = self.socket.recv(self.responseSize)
        print(r, "<-- Response")
        return r

    def __del__(self):
        self.socket.close()
