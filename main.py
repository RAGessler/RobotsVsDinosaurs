from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
robot_test = Robot('T1000')
dinosaur_test = Dinosaur('Ron', 25)
robot_test.attack(dinosaur_test)
dinosaur_test.attack(robot_test)