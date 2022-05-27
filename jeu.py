import json
with open("joueurs_bdd.json","r") as f:
    data=json.loads(f.read())
    #data=json.loads(f)
for joueurs in data:
   #print(joueurs)
   print(joueurs.keys())
   #print(joueurs["name"])
   print("bbbbb")
#    for joueur in joueurs:
#        print(joueur.keys())
   
   
#    for name in joueur:
#        print("bbbbb")
#        print(name[range(0,int(len(name)))])
   