#!/usr/bin/python3

# Groupe 5 :  Jenny, Thomas A, Cyril M, Thomas L, ,Thuy Tran,
# Date de réalisation : 25/05/22

# script qui sera sur le serveur et écoutera les demandes des clients

# un socket est un objet qui permet d'ouvrir une connexion avec une machine, locale ou distante, et d'échanger avec elle.


# import des modules
import socket ,sys

# création d'un canal de communication - socket - de type serveur
# 2 paramètres -> la famille d'adresses avec socket.AF_INET = adresses de type IPv4
#              -> le type du socket avec socket.SOCK_STREAM = protocole TPC

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket crée")

#while True?
# association à l'adresse à laquelle la socket sera liée
# syntaxe : serveur.bind((nom_d_hote,port))
# on met une chaîne vide ('') comme nom d'hôte, ce qui est équivalent à l'adresse IP '0.0.0.0'
# cela signifie que le socket est lié à toutes les interfaces locales(pour rappel: une machine peut avoir plusieurs interfaces réseau)

hostname = ''
port = 8080

try:
    serversocket.bind((hostname,port))
    print ("Socket lié à l'IP" +str(hostname) + " et au port" +str(port))

except socket.error:
    print("La liaison du socket a échoué")
    sys.exit()


# mettre le socket à l'état d'écoute / en attente de la requête de connexion d'un client
# syntaxe : server.listen(backlog)
# le backlog '5' représente le nb de connexions entrantes que nous sommes prêts à mettre en file d'attente avant d'en refuser 
# il désigne le nb max de connexions non acceptées que le système autorisera avt de refuser de nvelles connexions

print("Serveur prêt, en attente de requêtes...")
serversocket.listen(5)
    
# accepter une demande de connexion
# lorsqu'un client se connecte, le serveur est sensé accepter la connexion 
# syntaxe : connexion_client, adresse_client = serveur.accept()
# connexion_client : un nouveau socket = le socket de communication, celui qui permet l'échange de données avec le client
# adresse_client: l'adresse, au format (nom_d_hote,port), du client

connexion_client, adresse_client = serversocket.accept()
print ("Connexion établie avec " +str(adresse_client))


# dialogue avec le client
msg = connexion_client.recv(1024).decode("Utf8")
if not connexion_client:
    print("Erreur de réception")

else:
    #msg = connexion_client.recv(1024).decode("Utf8")
    print("Message reçu du client: " + str(msg))
    # print(msg)
    msg_out = "Message bien reçu. Merci" .format(1024).encode("Utf8")
    connexion_client.send(msg_out)
    
    
# fermeture des canaux de communication
print("Fermeture de la connexion avec le client")
connexion_client.close()
    
print("Arrêt du serveur")
serversocket.close()

