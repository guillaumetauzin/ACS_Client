# ACS_Client-serveur
Architecture Clients/Serveur / Atelier1

# Blackjack
Le dictionnaire contient des entrées au format :

Clé = Nom du joueur
Valeurs = score, round, cartes_joueur, carte_croupier

Lorsqu'un joueur joue,
Si le joueur a deja une carte
  il pioche une carte: on ajoute une carte a la valeur de cartes_joueur
  Le croupier pioche a son tour: on ajoute une carte a la valeur de carte_croupier
Sinon on a le choix de reprendre des cartes ou de valider: on ajoute une carte a la valeur de cartes_joueur ou tour du croupier
si la sommme des cartes de depasse pas 16 le croupier pioche une carte jusqu'a 16 ou plus
Si il depasse 21 le joueur gagne sinon on compare avec le joueur celui qui se raproche le plus de 21.
