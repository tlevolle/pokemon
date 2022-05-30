import json
import random

# class Base():
#     def __init__(self, hp, attack, defense, speed):
#         self.hp = hp
#         self.attack = attack
#         self.defense = defense
#         self.speed = speed

#     def get_hp():
#         return self.hp

#     def set_hp(hp):
#         self.hp = hp

#     def get_attack():
#         return self.attack

#     def set_attack(attack):
#         self.attack = attack

#     def get_defense():
#         return self.defense

#     def set_defense(defense):
#         self.defense = defense

#     def get_speed():
#         return self.speed

#     def set_speed(speed):
#         self.speed = speed


class Pokemon():
    def __init__(self, id_pokemon, nom_pokemon, type_pokemon, hp, attack, defense, speed):
        self.id_pokemon = id_pokemon
        self.nom_pokemon = nom_pokemon
        self.type_pokemon = type_pokemon
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    # def get_id_pokemon():
    #     return self.get_id_pokemon

    # def set_id_pokemon(id_pokemon):
    #     self.id_pokemon = id_pokemon

    # def get_nom_pokemon():
    #     return self.get_nom_pokemon

    # def set_nom_pokemon(nom_pokemon):
    #     self.nom_pokemon = nom_pokemon

    # def get_type_pokemon():
    #     return self.type_pokemon

    # def set_type_pokemon(type_pokemon):
    #     self.type_pokemon = type_pokemon

## ATTENTION : l'attribut liste_pokemons est un DICTIONNAIRE !!!
class Joueur():
    def __init__(self, nom_joueur, liste_pokemons):
        self.nom_joueur = nom_joueur
        self.liste_pokemons = liste_pokemons

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    # def get_nom_joueur():
    #     return self.nom_joueur

    # def set_nom_joueur(nom_joueur):
    #     self.nom_joueur = nom_joueur

    # def get_liste_pokemons():
    #     return self.liste_pokemons

    # def set_liste_pokemons():
    #     self.liste_pokemons = liste_pokemons

    def add_pokemon(pokemon):
        self.liste_pokemons[pokemon.get_nom_pokemon()] = pokemon

# Ouverture bdd des joueurs
with open("joueurs_bdd.json", "r") as f:
    data = json.load(f)

# Initialisation du joueur ; besoin d'intialiser ses paramètres
pokemons = {}
joueur1 = Joueur("", pokemons)
input_nom_joueur = input("Quel nom de joueur ? :")

# Si le joueur existe, on passe dans cette boucle.
joueur_existe = False
for joueur in data:
    if joueur["Joueur"] == input_nom_joueur:
     # on envoie dans la variable joueur1 le nom du joueur1 trouvé en bdd qui match avec l'input
        joueur_existe = True
        joueur1.nom_joueur = input_nom_joueur
        # on parcourt la liste des pokemons du joueur trouvé en bdd
        for pokemonJSON in joueur["Liste_Pokemons"]:
            types = []
            # on cree notre variable pokemon en récupérant les valeurs dans l'objet pokemon du fichier json
            pokemon = Pokemon(pokemonJSON['id'],
                              pokemonJSON['name'], types, pokemonJSON['HP'], pokemonJSON['Attack'], pokemonJSON['Defense'], pokemonJSON['Speed'])
            # on parcourt le tableau des types du pokemon trouvé dans
            # la liste de pokemons du joueur
            for typesJSON in pokemonJSON['type']:
                types.append(typesJSON)
            pokemon.type_pokemon = types
            # on envoie notre pokemon dans le dictionnaire de pokemon du joueur1
            joueur1.liste_pokemons[pokemon.nom_pokemon] = pokemon
        f.close()
#TODO

# liste_pokemons = []
# for i in range 3 {
# poke1 = random.choice(data)
# liste_pokemons.append(Pokemon(poke1[id] etc)) 
# }
#
# Si le joueur n'existe pas, on passe dans cette boucle
if joueur_existe == False:
    # on ouvre le pokedex pour récupérer trois pokemon alétoires
    with open("pokedex.json", "r") as f:
        data = json.load(f)
    # on choisit 3 random représentant nos trois pokemons
    id_random_1 = random.randrange(1, 809)
    id_random_2 = random.randrange(1, 809)
    id_random_3 = random.randrange(1, 809)
    # on initialise nos trois objets pokemon avec des valeurs nulles
    pokemon1 = Pokemon(0, "", [], 0, 0, 0, 0)
    pokemon2 = Pokemon(0, "", [], 0, 0, 0, 0)
    pokemon3 = Pokemon(0, "", [], 0, 0, 0, 0)
    # on parcout les pokemons du pokedex.json pour trouver des correspondances entre nos id randomisés et les id des pokemons
    for pokemonJSON in data:
        # si match entre le 1er random et l'id itéré, on récupère les informations du pokemon actuel et on envoie dans pokemon1
        if pokemonJSON['id'] == id_random_1:
            pokemon1.id_pokemon = pokemonJSON['id']
            pokemon1.nom_pokemon = pokemonJSON['name']['french']
            for typePokemonJSON in pokemonJSON['type']:
                pokemon1.type_pokemon.append(typePokemonJSON)
            pokemon1.hp = pokemonJSON['base']['HP']
            pokemon1.attack = pokemonJSON['base']['Attack']
            pokemon1.defense = pokemonJSON['base']['Defense']
            pokemon1.speed = pokemonJSON['base']['Speed']
        # si match entre le 2e random et l'id itéré, on récupère les informations du pokemon actuel et on envoie dans pokemon2
        if pokemonJSON['id'] == id_random_2:
            pokemon2.id_pokemon = pokemonJSON['id']
            pokemon2.nom_pokemon = pokemonJSON['name']['french']
            for typePokemonJSON in pokemonJSON['type']:
                pokemon2.type_pokemon.append(typePokemonJSON)
            pokemon2.hp = pokemonJSON['base']['HP']
            pokemon2.attack = pokemonJSON['base']['Attack']
            pokemon2.defense = pokemonJSON['base']['Defense']
            pokemon2.speed = pokemonJSON['base']['Speed']
        # si match entre le 3e random et l'id itéré, on récupère les informations du pokemon actuel et on envoie dans pokemon3
        if pokemonJSON['id'] == id_random_3:
            pokemon3.id_pokemon = pokemonJSON['id']
            pokemon3.nom_pokemon = pokemonJSON['name']['french']
            for typePokemonJSON in pokemonJSON['type']:
                pokemon3.type_pokemon.append(typePokemonJSON)
            pokemon3.hp = pokemonJSON['base']['HP']
            pokemon3.attack = pokemonJSON['base']['Attack']
            pokemon3.defense = pokemonJSON['base']['Defense']
            pokemon3.speed = pokemonJSON['base']['Speed']
    # on envoie le nom du joueur dans joueur1
    joueur1.nom_joueur = input_nom_joueur
    # on ajoute nos pokemons au dictionnaire de pokemon
    pokemons = {pokemon1.nom_pokemon: pokemon1,
                pokemon2.nom_pokemon: pokemon2, pokemon3.nom_pokemon: pokemon3}
    # on ajoute le dictionnaire au joueur1
    joueur1.liste_pokemons=pokemons
    f.close()


    with open("joueurs_bdd.json", "r") as f:
        data=json.load(f)
    
    f.close()

    # for pokemon_name, pokemon in joueur1.liste_pokemons.items():
    #     data.append
    print(data)
    print("")
    string=joueur1.toJSON()
    print(string)

    

    

    # file_open=open("joueurs_bdd.json", "w")
    # file_open.write(data)



