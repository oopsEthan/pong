from turtle import *

# Paddle is for shared variables
class Paddle:
    def __init__(self) -> None:
        self.solid = True

class Player(Paddle):
    pass

class Opponent(Paddle):
    pass

class Ball:
    def __init__(self) -> None:
        self.ball_manager = Turtle()
        self.set_up_turtle()

    def set_up_turtle(self):
        self.ball_manager.pu()
        self.ball_manager.shape("square")
        self.ball_manager.shapesize(0.5, 0.5)
        self.ball_manager.color("white")
    
    def check_for_collision(self):
        pass