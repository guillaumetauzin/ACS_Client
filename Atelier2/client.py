from socket import socket, AF_INET, SOCK_STREAM
from struct import pack, unpack

PORT = 0x2BAD
SERVER = "127.0.0.1"

if __name__ == '__main__':
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((SERVER, PORT))
        num = unpack('!i', sock.recv(4))[0]
        print(f"Tu es le joueur n°{num}")
        while True:
            nb_input = int(input("Entrez un nombre entre 0 et 100: "))
            a_ete_devine = unpack('!i', sock.recv(4))[0]
            if a_ete_devine != 0:
                nb = unpack('!i', sock.recv(4))[0]
                print(f"Le joueur n°{int(a_ete_devine)} a deviné en permier le nombre {nb}")
                sock.close()
                break

            sock.send(pack('!i', nb_input))

            retour = unpack('!i', sock.recv(4))[0] # 1=plus -1=mois 0=bon numero
            if retour == 1:
                print("C'est plus !")
            if retour == -1:
                print("C'est moins !")
            if retour == 0:
                print("Bravo vous avez trouvé le nombre en premier !")
                break
        sock.close()