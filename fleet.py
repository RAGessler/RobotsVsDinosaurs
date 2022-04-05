from robot import Robot
from weapon import Weapon
weapon_one = Weapon('Pulse Rifle', 30)
weapon_two = Weapon('Scatter Blaster', 60)
weapon_three = Weapon('Auto Lance', 45)

class Fleet:
    def __init__(self):
        self.name = 'Terminators'
        self.robot_one = Robot('T1001')
        self.robot_one.active_weapon = weapon_one
        self.robot_two = Robot('T1002')
        self.robot_two.active_weapon = weapon_two
        self.robot_three = Robot('T1002')
        self.robot_three.active_weapon = weapon_three
        self.health = self.robot_one.health + self.robot_two.health + self.robot_three.health
        self.attack_power = self.robot_one.active_weapon.attack_power + self.robot_two.active_weapon.attack_power + self.robot_three.active_weapon.attack_power
    def choose_weapon(self):
        pass
    def attack(self, heard):
        heard.health -= self.attack_power
        print(f'{heard.name} has {heard.health} hitpoints remaining!')

