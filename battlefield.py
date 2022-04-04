from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('T-1000')
        self.dinosaur = Dinosaur('Jeff', 40)
    def run_game(self):
        display_welcome(self)
        # while self.robot.health >= 0 or self.dinosaur.health >=0:
    def display_welcome(self):
        print('Welcome to the robot dino SHOWDOWN')
        print(f'{self.robot.name} has picked a fight with {self.dinosaur.name}!')
    def battle_phase(self):
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur} has defeated {self.robot}')
        elif self.dinosaur <= 0:
            print(f'{self.robot} has defeated {self.dinosaur}')
        else:
            pass
    