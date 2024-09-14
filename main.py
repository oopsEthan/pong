from turtle import *
from paddles_and_ball import *
from game_settings import Game

game = Game()
ball = Ball()
player = Player()
opponent = Opponent()

collisions = [player, opponent]
ball.set_possible_collisions(collisions)

game.run()