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
    pass