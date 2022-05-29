#!/usr/bin/python3

# Groupe 5 :  Jenny, Thomas A, Cyril M, Thomas L, ,Thuy Tran,
# Date de réalisation : 27/05/22

# script qui sera sur le serveur et écoutera les demandes des clients


# mise en place d'un serveur réseau gérant un système de chat simplifié

# utilisation des threads pour gérer les connexions clientes en parallèle
# le multithreading est une technique qui permet d'exécuter plusieurs tâches (thread) en même temps et de manière indépendante dans un même processus.
# pour notre jeu, on utilisera 2 threads. Chaque thread gère donc le socket du client.
# le serveur n'est pas utilisé lui-même pour communiquer: ce sont les clients qui communiquent les uns avec les autres, par l'intermédiaire du serveur. Il jour donc le rôle de relais


# import des modules
# la classe ThreadMixIn permet au serveur de créer de nouvexu threads pour prendre en charge chaque nouvelle connexion.
import socket, sys
from threading import Thread 
from socketserver import ThreadingMixIn 

ip = ''
port = 8080

class myThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] Nouveau thread démarré pour " + ip + ":" + str(port))
 
    def run(self): 
        while True : 
            i=1
            msg = connexion_client.recv(1024).decode("Utf8")
            print("Le serveur a reçu des données: ", msg) 
            #msg_out = input("Entrez la réponse du serveur ou exit pour sortir:").format(1024).encode("Utf8")
            #connexion_client.send(msg_out)

            if msg_out == 'exit':
                i=0
                print("Fermeture de la connexion client")
                connexion_client.send("exit".format(1024).encode("utf8"))
                connexion_client.close()
            else: 
                msg_out = input("Entrez la réponse du serveur ou exit pour sortir:").format(1024).encode("Utf8")
                connexion_client.send(msg_out)


serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

HOST = ''
PORT = 8080

try:
    serversocket.bind((HOST,PORT))
    print ("Liaison du socket effectuée")

except socket.error:
    print("La liaison du socket a échoué")
    sys.exit()
    
mythreads = [] 
 
while True: 
    print("Serveur prêt, en attente de requêtes...")
    serversocket.listen(5)

    connexion_client, adresse_client = serversocket.accept()
    print ("Connexion établie avec " +str(adresse_client))

    mythread = myThread(ip,port) 
    mythread.start() 
    mythreads.append(mythread) 

for t in mythreads: 
    t.join()

# fermeture des canaux de communication
#print("Fermeture de la connexion avec le client")
#connexion_client.close()
    
print("Arrêt du serveur")
serversocket.close()

# # création d'un canal de communication - socket - de type serveur
# # 2 paramètres -> la famille d'adresses avec socket.AF_INET = adresses de type IPv4
# #              -> le type du socket avec socket.SOCK_STREAM = protocole TPC

# serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print("Socket crée")

# #while True?
# # association à l'adresse à laquelle la socket sera liée
# # syntaxe : serveur.bind((nom_d_hote,port))
# # on met une chaîne vide ('') comme nom d'hôte, ce qui est équivalent à l'adresse IP '0.0.0.0'
# # cela signifie que le socket est lié à toutes les interfaces locales(pour rappel: une machine peut avoir plusieurs interfaces réseau)

# host = ''
# port = 8080

# try:
#     serversocket.bind((host,port))
#     print ("Liaison du socket effectuée")

# except socket.error:
#     print("La liaison du socket a échoué")
#     sys.exit()


# # mettre le socket à l'état d'écoute / en attente de la requête de connexion d'un client
# # syntaxe : server.listen(backlog)
# # le backlog '5' représente le nb de connexions entrantes que nous sommes prêts à mettre en file d'attente avant d'en refuser 
# # il désigne le nb max de connexions non acceptées que le système autorisera avt de refuser de nvelles connexions

# print("Serveur prêt, en attente de requêtes...")
# serversocket.listen(5)
    
# # accepter une demande de connexion
# # lorsqu'un client se connecte, le serveur est sensé accepter la connexion 
# # syntaxe : connexion_client, adresse_client = serveur.accept()
# # connexion_client : un nouveau socket = le socket de communication, celui qui permet l'échange de données avec le client
# # adresse_client: l'adresse, au format (nom_d_hote,port), du client

# connexion_client, adresse_client = serversocket.accept()
# print ("Connexion établie avec " +str(adresse_client))


# # dialogue avec le client
# msg = connexion_client.recv(1024).decode("Utf8")
# if not connexion_client:
#     print("Erreur de réception")

# else:
#     #msg = connexion_client.recv(1024).decode("Utf8")
#     print("Message reçu du client: " + str(msg))
#     # print(msg)
#     msg_out = "Message bien reçu. Merci" .format(1024).encode("Utf8")
#     connexion_client.send(msg_out)
    
    
# # fermeture des canaux de communication
# print("Fermeture de la connexion avec le client")
# connexion_client.close()
    
# print("Arrêt du serveur")
# serversocket.close()

