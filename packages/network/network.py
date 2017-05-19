import socket
from config import SERVER_IP, SERVER_PORT, RESPONSE_SIZE, TEAM_NAME


class NetworkInterface:
    def __init__(self):
        self.team_num = -1
        self.responseSize = RESPONSE_SIZE
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SERVER_IP, SERVER_PORT))
        self.init_name()

    def receive(self):
        r = self.socket.recv(RESPONSE_SIZE).decode()
        print("<-- Receive --", r)
        return r.rstrip()

    def send(self, msg):
        print("Send --> ", msg)
        encoded_msg = str(msg + "\n").encode()
        self.socket.send(encoded_msg)

    def init_name(self):
        self.send(TEAM_NAME)
        r = self.receive()
        self.team_num = int(r)
        print("Team number", self.team_num)

    def action(self, message):
        self.send(message)

    def __del__(self):
        self.socket.close()
