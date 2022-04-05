from dinosaur import Dinosaur
class Heard:
    def __init__(self):
        self.name = 'The Boys'
        self.dino_one = Dinosaur('Chet', 20)
        self.dino_two = Dinosaur('Archduke Franz Ferdiand', 35)
        self.dino_three = Dinosaur('Sean', 60)
        self.health = self.dino_one.health + self.dino_two.health + self.dino_three.health
        self.attack_power = self.dino_one.attack_power + self.dino_two.attack_power + self.dino_three.attack_power
    def attack(self, fleet):
        fleet.health -= self.attack_power
        print(f'{fleet.name} has {fleet.health} hitpoints remaining!')