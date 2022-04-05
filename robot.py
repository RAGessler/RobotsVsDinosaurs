from weapon import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = weapon_one
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} has {dinosaur.health} hitpoints remaining!')
    def choose_weapon(self):
        print(f'Choose a weapon for {self.name}')
        weapon_input = int(input(f"Weapon options are 1{weapon_one.name}, 2{weapon_two.name}, 3{weapon_three.name}.  Enter 1 2 or 3 to select"))
        if weapon_input == 1:
            self.active_weapon = weapon_one
        elif weapon_input == 2:
            self.active_weapon = weapon_two
        elif weapon_input == 3:
            self.active_weapon == weapon_three
        else:
            print('Invalid Input Try Again')
            self.choose_weapon()




weapon_one = Weapon('Pulse Rifle', 30)
weapon_two = Weapon('Scatter Blaster', 60)
weapon_three = Weapon('Auto Lance', 45)

