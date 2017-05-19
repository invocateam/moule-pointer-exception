import socket

class NetwaorkInterface():
    def __init__(self, host, port):
        self.responseSize= 999999
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def action(self, message):
        print("Send --> ", message)
        self.socket.send(message)
        r = self.socket.recv(self.responseSize)
        return r

    def __del__(self):
        self.socket.close()

