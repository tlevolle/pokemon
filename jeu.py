import json


class Base():
    def __init__(self, hp, attack, defense, speed):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def get_hp():
        return self.hp

    def set_hp(hp):
        self.hp = hp

    def get_attack():
        return self.attack

    def set_attack(attack):
        self.attack = attack

    def get_defense():
        return self.defense

    def set_defense(defense):
        self.defense = defense

    def get_speed():
        return self.speed

    def set_speed(speed):
        self.speed = speed

class Pokemon():
    def __init__(self, id_pokemon, nom_pokemon, type_pokemon, base_pokemon):
        self.id_pokemon = id_pokemon
        self.nom_pokemon = nom_pokemon
        self.type_pokemon = type_pokemon
        self.base_pokemon = base_pokemon

    def get_id_pokemon():
        return self.get_id_pokemon

    def set_id_pokemon(id_pokemon):
        self.id_pokemon = id_pokemon

    def get_nom_pokemon():
        return self.get_nom_pokemon

    def set_nom_pokemon(nom_pokemon):
        self.nom_pokemon = nom_pokemon

    def get_type_pokemon():
        return self.type_pokemon

    def set_type_pokemon(type_pokemon):
        self.type_pokemon = type_pokemon

    def get_base_pokemon():
        return self.base_pokemon

    def set_base_pokemon(base_pokemon):
        self.base_pokemon = base_pokemon

class Joueur():
    def __init__(self, nom_joueur, liste_pokemons):
        self.nom_joueur = nom_joueur
        self.liste_pokemons = liste_pokemons

    def get_nom_joueur():
        return self.nom_joueur

    def set_nom_joueur(nom_joueur):
        self.nom_joueur = nom_joueur

    def get_liste_pokemons():
        return self.liste_pokemons

    def set_liste_pokemons():
        self.liste_pokemons = liste_pokemons

    def add_pokemon(pokemon):
        self.liste_pokemons[pokemon.get_nom_pokemon()] = pokemon






# with open("joueurs_bdd.json", "r") as f:
#     data = json.load(f)

# for joueur in data:

#     for liste_pokemons in joueur["Liste_Pokemons"]:
#         print(liste_pokemons['name'])
#         print(liste_pokemons['type'])
#         print(liste_pokemons['base'])
#         print("")
