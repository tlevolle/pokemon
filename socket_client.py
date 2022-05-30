#!/usr/bin/python3

# Exercice pokémon 
# Script client ; partie connexion serveur/client
# Groupe 5 : Thuy Tran, Thomas A, Cyril M, Thomas L, Jenny. 
# Date de réalisation : 25/05/22

import socket 

hote, port = ('192.168.1.12', 8080)
#port = 8080  #pour connexsion http

# Creation socket cote client qui va donner l'acces au serveur
# socket.AF_INET : adresses internet de type IPv4
# socket.SOCK_STREAM : protocole TCP
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Demande de connexion au serveur avec .connect()
# connexion_serveur.connect((nom_hote_serveur, port_d_ecoute_serveur))
try:
    connexion_serveur.connect((hote, port))
    print("Connexion au serveur etablie")

    # Envoi message au serveur .send()
    # utilisation UTF-8 pour encoder/decoder le message envoye/recu du serveur
    # envoi message -> (message.encode("utf-8"))
    # reception message -> .recv  -> (reponse.decode("utf-8"))
    data = "Hoolaaaaa, je suis le client :)"
    data = data.encode("utf8")
    connexion_serveur.sendall(data)
 
    reponse=connexion_serveur.recv(1024)
    print(reponse.decode("utf-8"))

except ConnectionRefusedError:  # echec qd le serveur n'est pas en ecoute
    print("Connexion au serveur échouée !")

finally:
    # Fermer la connexion 
    print("Connexion interrompue")
    connexion_serveur.close()
