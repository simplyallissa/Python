def main():

class Pokemon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
    def pokemon_attacks(self):
        print(self.name, ' used ', self.attack, '!')

Pikachu = Pokemon('Pikachu', 'thunderbolt')
Pikachu.pokemon_attacks()

main()
