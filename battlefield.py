from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('T-1000', placeholder)
        self.dinosaur = Dinosaur('Jeff', 40)
    def run_game(self):
        self.display_welcome()
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase()
        self.display_winner()
    def display_welcome(self):
        print('Welcome to the robot dino SHOWDOWN')
        print(f'{self.robot.name} has picked a fight with {self.dinosaur.name}!')
    def battle_phase(self):
        self.robot.choose_weapon()
        self.dinosaur.attack(self.robot)
        self.robot.attack(self.dinosaur)
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} has defeated {self.robot.name}!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} has defeated {self.dinosaur.name}!')
        else:
            pass

    