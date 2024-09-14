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

        self.ball_radius = 5

    def set_up_turtle(self):
        self.ball_manager.pu()
        self.ball_manager.shape("square")
        self.ball_manager.shapesize(0.5, 0.5)
        self.ball_manager.color("white")

    def travel(self):
        # check_for_collision()
        # move forward
        pass

    def set_possible_collisions(self, possible_collisions):
        self.collisions = possible_collisions
    
    def check_for_collision(self):
        for col in self.collisions:
            if col.solid:
                distance = self.ball_manager.distance(col)

                # Code may need to change to consider the wall at bottom too
                if distance <= self.ball_radius + col.paddle_width:
                    self.bounce()
    
    def bounce(self):
        # reverse 180
        pass