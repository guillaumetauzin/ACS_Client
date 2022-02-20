import socket
import time
from random import randint
def request(verb, url, value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("127.0.0.1", 5000))
        sock.send(f"{verb} /{url} HTTP/1.1\r\n".encode())
        sock.send("Content-Type: text/plain\r\n".encode())
        sock.send(f"Content-Length: {len(value)}\r\n\r\n".encode())
        sock.send(f"{value}\r\n".encode())
        reponse = ""
        while True:
            s = sock.recv(4096).decode('utf-8')
            if s == '':
                break;
            reponse = reponse + s
        sock.close()
        return reponse

# request("POST", items[0], items[1])
# request("GET", "", "")

if __name__ == '__main__':
    i = 1
    joueur = 0
    serveur = False
    while True:
        if str(request("GET", i, "").split("\n")[6]) == "Not found":
            request("POST", i, "ok")
            print(f"Vous etes le joueur {i}")
            joueur = i
            if(joueur == 1):
                serveur = True
            break
        i = i + 1
    #Jeu
    if(serveur):
        nb = randint(0, 100)
        request("POST", i, str(nb))
        request("POST", "winner", "?")
        print("DEBUG: le nombre est " + str(nb))
    else:
        nb = int(request("GET", 1, "").split("\n")[6])
    while True:
        nb_input = int(input("Entrez un nombre entre 0 et 100: "))
        if str(request("GET", "winner", "").split("\n")[6]) != "?":
            print("Le joueur n°"+ str(request("GET", "winner", "").split("\n")[6]) + " a été le premier a trouver le nombre "+ str(nb))
            break
        if nb_input < nb:
            print("C'est plus !")
        if nb_input > nb:
            print("C'est moins !")
        if nb_input == nb:
            print("Bravo vous avez trouvé le nombre en premier !")
            request("POST", "winner", str(i))
            break

