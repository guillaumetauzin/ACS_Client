import random
from socket import socket, AF_INET, SOCK_STREAM
from struct import pack, unpack
from threading import Thread, Event

PORT = 0x2BAD
players = []
is_head = False
ready_event = Event()
nb = random.randint(0, 100)
a_ete_devine = -1
print("DEBUG: le nombre est " + str(nb))

class Player(Thread):
    def __init__(self, num, sock):
        Thread.__init__(self)
        self._id = num
        self._sock = sock

    def run(self):
        global is_head, ready_event, a_ete_devine
        self._sock.send(pack('!i', self._id))
        while True:
            if a_ete_devine != -1:
                self._sock.send(pack('!i', a_ete_devine))
                self._sock.send(pack('!i', nb))
            else:
                self._sock.send(pack('!i', 0))
            data = self._sock.recv(10)
            data = unpack("!i", data)[0]
    
            if data < nb:
                self._sock.send(pack('!i', 1)) #plus
            if data > nb:
                self._sock.send(pack('!i', -1))#moins
            if data == nb:
                self._sock.send(pack('!i', 0))
                a_ete_devine = self._id

def find_player_id():
    global players

    for i in range(len(players)):
        if players[i] is None:
            return i+1
    players.append(None)
    return len(players)


if __name__ == '__main__':
    with socket(AF_INET, SOCK_STREAM) as sock_listen:
        sock_listen.bind(('', PORT))
        sock_listen.listen(5)
        print(f"Listening on port {PORT}")
        while True:
            sock_service, client_addr = sock_listen.accept()
            index = find_player_id()
            print(f"- Player {index} arrived")
            players[index-1] = Player(index, sock_service)
            players[index-1].start()
