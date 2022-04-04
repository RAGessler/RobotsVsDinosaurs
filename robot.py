from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('ScatterBlaster', 30) 
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(dinosaur.health)

